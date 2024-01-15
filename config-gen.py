# Python 3

import json
from json import JSONDecodeError
import socket
import urllib.request as req
import urllib.parse as p
import re
import requests
from plexapi.server import PlexServer
from plexapi.exceptions import BadRequest, NotFound, Unauthorized
from xml.etree.ElementTree import ParseError
from tmdbapis import TMDbAPIs
import click
from lxml import html
import yaml
from arrapi import RadarrAPI, SonarrAPI
from arrapi.exceptions import ArrException
import requests
import webbrowser
from types import SimpleNamespace
import secrets
import os
from defaults import get_options, get_collection_types, get_boolean_operations

default_config_data = {
    "PLEX_URL": "",
    "PLEX_TOKEN": "",
    "TMDB_KEY": "",
    "TAUTULLI_URL": "",
    "TAUTULLI_KEY": "",
    "OMDB_KEY": "",
    "MDBLIST_KEY": "",
    "NOTIFIARR_KEY": "",
    "ANIDB_USER": "",
    "ANIDB_PASS": "",
    "RADARR_URL": "",
    "RADARR_TOKEN": "",
    "SONARR_URL": "",
    "SONARR_TOKEN": "",
    "TRAKT_CLIENT_ID": "",
    "TRAKT_CLIENT_SECRET": "",
    "MAL_CLIENT_ID": "",
    "MAL_CLIENT_SECRET": "",
}
CONFIG_DATA = default_config_data

def validate_config(config_data):
    for key in default_config_data.keys():
        try:
            tmp=config_data[key]
        except Exception as ex:
            config_data[key]=""
    return config_data

try:
    with open("config.json", "r") as jsonfile:
        CONFIG_DATA = json.load(jsonfile)
        print("Config read successful")
except:
    print("No local config file")

CONFIG_DATA = validate_config(CONFIG_DATA)

class Failed(Exception):
    pass

def get_json(url, json=None, headers=None, params=None):
    return get(url, json=json, headers=headers, params=params).json()

def get(url, json=None, headers=None, params=None):
    return session.get(url, json=json, headers=headers, params=params)

def post(url, data=None, json=None, headers=None):
    return session.post(url, data=data, json=json, headers=headers)

def def_header(language="en-US,en;q=0.5"):
    return {"Accept-Language": "eng" if language == "default" else language, "User-Agent": "Mozilla/5.0 Firefox/102.0"}

def test_url(url):

    try:
        print("I'm going to try to load that.")
        request = req.Request(url, headers={'User-Agent': 'curl/7.64.1'})
        response = req.urlopen(request)
        print("Success.\n==============================\n")
        return True
    except Exception as ex:
        print(f"Issue while loading: {ex}")
        return False

def get_config():
    ret_obj = None
    try:
        print("Let's grab the current config template.")
        url = "https://raw.githubusercontent.com/meisnate12/Plex-Meta-Manager/master/config/config.yml.template"
        request = req.Request(url, headers={'User-Agent': 'curl/7.64.1'})
        response = req.urlopen(request)
        if response.status == 200:
            yaml_content = response.read()
            ret_obj = yaml.safe_load(yaml_content)
            print("Success.\n==============================\n")
    except Exception as ex:
        print(f"Issue while loading: {ex}; using fallback.yml")
        with open('fallback.yml', 'r') as yf:
            ret_obj = yaml.safe_load(yf)
    return ret_obj

def get_lib_skel():
    lib_skel = {
            'metadata_path': [],
            'operations': {},
            'overlay_path': []
        }
    return lib_skel

def convert_to_default_path(files):
    retval = []
    for f in files:
        tmp = {"pmm": f.path}
        retval.append(tmp)
    return retval

def get_std_collections(type):
    retval = None
    std_collections = get_options("collections", type, basics=True, mal=myanimelist, trakt=trakt, tautulli=tautulli)
    # [{'pmm': 'basic'}, {'pmm': 'imdb'}]
    retVal = convert_to_default_path(std_collections)
    return retVal

STOCK_OL_OPS = {"remove_overlays", "reapply_overlays", "reset_overlays"}

def get_overlays_ops():
    retval = []
    for op in STOCK_OL_OPS:
        tmp = {op: False}
        retval.append(tmp)
    return retval

def get_std_overlays(type):
    retval = None
    retval = get_options("overlays", type, basics=True)
    return retval

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def yes_or_no(question):
    answer = click.prompt(f"{question}", type=str, default="n").lower().strip()
    while not(answer == "y" or answer == "yes" or \
    answer == "n" or answer == "no"):
        print("Input yes or no")
        answer = click.prompt(f"{question}", type=str, default="n").lower().strip()
    if answer[0] == "y":
        return True
    else:
        return False

def good_value(question, values):
    ret_val = None
    while ret_val is None:
        answer = click.prompt(f"{question}", type=str).lower().strip()
        print("")
        for x in values:
            if str(answer) == str(x.id):
                ret_val = x
                break
        if not ret_val:
            print("Input a value from the list")
    return ret_val

def process_sections(ps):
    plex_sections = ps.library.sections()
    library_yaml = {}
    for plex_section in plex_sections:
        if plex_section.type != "artist":
            print("\n------------------------------")
            if yes_or_no(f"\nConfigure PMM for the {plex_section.type} library [{plex_section.title}]?"):
                section_yaml = get_lib_skel()

                print("\n------------------------------")
                print(f"Let's start with collections")
                if yes_or_no(f"Add a small standard set of collections to get started?"):
                    section_yaml['metadata_path'] = get_std_collections(plex_section.type)
                else:
                    collections = []
                    collection_types = get_collection_types()
                    # ask about all of them
                    for c_t in collection_types:
                        print(f"Add some of the {c_t['name']} collections?")
                        if yes_or_no(f"These are {c_t['note']}"):
                            colls = get_options("collections", plex_section.type, group=c_t['name'], mal=myanimelist, trakt=trakt, tautulli=tautulli)
                            for c in colls:
                                print(f"Add the {c.name} collections?")
                                if yes_or_no(f"Things like {c.notes}"):
                                    collections.append(c)
                    # now I'm through the collections
                    section_yaml['metadata_path'] = convert_to_default_path(collections)

                # Something about operations
                print("\n------------------------------")
                print(f"Next step, operations.")
                print(f"PMM can perform a lot of different operations on a library.")
                print(f"Most of these operations require some configuration.")
                print(f"Going through them with a tool like this will ask a LOT of questions.")
                print(f"For that reason this will not be a comprehensive list of possibilities.")
                operations = []
                if yes_or_no(f"Do you want to enable any operations on this library?"):
                    print(f"First, yes/no operations.")
                    boolean_ops = get_boolean_operations()
                    for op in boolean_ops:
                        if yes_or_no(f"Should PMM {op.notes}?"):
                            tmp = {op.path: True}
                        else:
                            tmp = {op.path: False}
                        operations.append(tmp)

                    # print(f"Next, mass update operations.")
                    # print(f"Generally speaking, these operations are expensive.")
                    # print(f"Don't just enable enverything here, particularly")
                    # print(f"if you have very large libraries.")
                    # ratings_updates = False

                    # ratings_ops = get_mass_update_operations()
                    # for op in boolean_ops:
                    #     if yes_or_no(f"Should PMM {op.notes}?"):
                    #         tmp = {op.path: True}
                    #     else:
                    #         tmp = {op.path: False}
                    #     operations.append(tmp)

                    # if yes_or_no(f"Do you want to enable any operations on this library?"):
                    #     section_yaml['overlay_path'] = get_std_overlays(plex_section.type)


                if len(operations) > 0:
                    section_yaml['operations'] = operations
                else:
                    section_yaml.pop('operations')

                # Something about overlays
                print("\n------------------------------")
                print(f"Finally, overlays.")
                print(f"Many of these overlays allow customization.")
                print(f"Going through them with a tool like this will ask a LOT of questions.")
                print(f"For that reason this will not be a comprehensive list of possibilities.")
                print(f"The tool will just enable the base overlay.")
                overlays = []
                if yes_or_no(f"Do you want to enable any overlays on this library?"):
                    if yes_or_no(f"Add a small standard set of overlays to get started?  If you answer 'no' I will ask about all possible overlays."):
                        overlays = get_std_overlays(plex_section.type)
                    else:
                        options = get_options("overlays", plex_section.type, mal=myanimelist, trakt=trakt, tautulli=tautulli)
                        for o in options:
                            print(f"Add the {o.name} overlays?")
                            if yes_or_no(f"{o.notes}"):
                                overlays.append(o)

                        
                if len(overlays) > 0:
                    section_yaml['overlay_path'] = get_overlays_ops() + convert_to_default_path(overlays)
                else:
                    section_yaml.pop('overlay_path')

                library_yaml[plex_section.title] = section_yaml
        else:
            print(f"Skipping {plex_section.title}")
    yaml_obj['libraries'] = library_yaml

def prep_config(raw_config):
    yaml_obj = raw_config

    yaml_obj['libraries'] = {}
    yaml_obj['tautulli']['url'] = empty_value
    yaml_obj['tautulli']['apikey'] = empty_value
    yaml_obj['omdb']['apikey'] = empty_value
    yaml_obj['mdblist']['apikey'] = empty_value
    yaml_obj['notifiarr']['apikey'] = empty_value
    yaml_obj['webhooks']['error'] = empty_value
    yaml_obj['webhooks']['version'] = empty_value
    yaml_obj['webhooks']['run_start'] = empty_value
    yaml_obj['webhooks']['run_end'] = empty_value
    yaml_obj['webhooks']['changes'] = empty_value
    yaml_obj['anidb']['username'] = empty_value
    yaml_obj['anidb']['password'] = empty_value
    yaml_obj['radarr']['url'] = empty_value
    yaml_obj['radarr']['token'] = empty_value
    yaml_obj['sonarr']['url'] = empty_value
    yaml_obj['sonarr']['token'] = empty_value
    yaml_obj['trakt']["client_id"] = empty_value
    yaml_obj['trakt']["pin"] = empty_value
    yaml_obj['trakt']["client_secret"] = empty_value
    yaml_obj['trakt']["authorization"]["access_token"] = empty_value
    yaml_obj['trakt']["authorization"]["token_type"] = empty_value
    yaml_obj['trakt']["authorization"]["expires_in"] = empty_value
    yaml_obj['trakt']["authorization"]["refresh_token"] = empty_value
    yaml_obj['trakt']["authorization"]["scope"] = empty_value
    yaml_obj['trakt']["authorization"]["created_at"] = empty_value
    yaml_obj['mal']["client_id"] = empty_value
    yaml_obj['mal']["client_secret"] = empty_value
    yaml_obj['mal']["authorization"]["access_token"] = empty_value
    yaml_obj['mal']["authorization"]["token_type"] = empty_value
    yaml_obj['mal']["authorization"]["expires_in"] = empty_value
    yaml_obj['mal']["authorization"]["refresh_token"] = empty_value

    return yaml_obj

my_ip = get_ip()
config_file_name="config.yml"
empty_value = ""
session = requests.Session()

plex = None
PLEX_URL = None
PLEX_TOKEN = None
tmdb = None
TAUTULLI_URL = None
TAUTULLI_KEY = None

print("We're going to generate a Plex-Meta-Manager config file. \r\n\r\n\
You WILL need these three bits of information: \r\n\
    1. Your Plex URL \r\n\
    2. Your Plex Token \r\n\
    3. Your TMDB API Key \r\n\
     \r\n")
if yes_or_no("Do you have those three required things available?"):
    print("Cool.\n")
else:
    print("I am sorry, but I cannot continue.")
    exit()


print("You MAY need these bits of information, depending on which other services you want to leverage: \r\n\
    1. Your Tautulli URL and API Key\r\n\
    2. Your OMDB API Key\r\n\
    3. Your MDBList API Key\r\n\
    4. Your Notifiarr API Key\r\n\
    5. Your ANIDB username and password\r\n\
    6. Your Radarr URL and API Key\r\n\
    7. Your Sonarr URL and API Key\r\n\
    8. Your Trakt Client ID and Client Secret\r\n\
    9. Your MyAnimeList Client ID and Client Secret\r\n\
     \r\n\
    Every URL referenced above must be a fully-qualified URL:\r\n\
    [https://plex.YOURDOMAIN.COM, http://radarr:8787, http://192.168.1.11:32400, etc.]\r\n\
    This script assumes it is going to be able to connect to those URLs.\r\n")

if yes_or_no("Are you prepared to continue?"):
    print("Cool.\n")
else:
    print("Okey doke, exiting.")
    exit()

raw_config = get_config()

yaml_obj = prep_config(raw_config)

print("Connecting to required services.\n==============================\n")
plex = None

while True:
    PLEX_URL = click.prompt(f"Plex URL", type=str, default=CONFIG_DATA['PLEX_URL'])
    PLEX_TOKEN = click.prompt(f"Plex Token", type=str, default=CONFIG_DATA['PLEX_TOKEN'])
    failed = False

    print(f"Attempting to connect to {PLEX_URL}...")
    try:
        plex = PlexServer(PLEX_URL, PLEX_TOKEN)
        if plex is not None:
            print("Success.\n==============================\n")
            yaml_obj['plex']['url'] = PLEX_URL
            CONFIG_DATA['PLEX_URL'] = PLEX_URL
            yaml_obj['plex']['token'] = PLEX_TOKEN
            CONFIG_DATA['PLEX_TOKEN'] = PLEX_TOKEN
            break
        else:
            raise Exception
    except Unauthorized:
        print("Plex Error: Plex token is invalid")
        failed = True
    except ValueError as e:
        print(f"Plex Error: {e}")
        failed = True
    except (requests.exceptions.ConnectionError, ParseError):
        print("Plex Error: Plex url is invalid")
        failed = True
    except Exception as ex:
        print(f"I was unable to connect to {PLEX_URL}")
        failed = True

    if failed:
        print(f"I was unable to authenticate against {PLEX_URL}")
        print("This may not be a problem, but it will prevent this script")
        print("from automatically configuring libraries.")
        if yes_or_no("Would you like to enter a different URL or token?"):
            print("Cool.\n")
        else:
            print("I will continue with that URL and token.")
#             print("I will ask for library names later.\n")
            print("You will need to configure your libraries manually.\n")
            break

while True:
    TMDB_KEY = click.prompt(f"TMDB API Key", type=str, default=CONFIG_DATA['TMDB_KEY'])

    try:
        tmdb = TMDbAPIs(TMDB_KEY, language="en")
        print("Success.\n==============================\n")
        yaml_obj['tmdb']['apikey'] = TMDB_KEY
        CONFIG_DATA['TMDB_KEY'] = TMDB_KEY
        break
    except:
        print(f"That does not appear to be a valid TMDB key.")
        if yes_or_no("Would you like to enter a different TMDB Key?"):
            print("Cool.\n")
        else:
            print("I cannot continues without a valid TMDB key")
            exit()

print("Required services complete.\n==============================\n")

print("Connecting to optional services.\n==============================\n")

tautulli = False

while True:
    if yes_or_no("Would you like to connect PMM to Tautulli?"):
        TAUTULLI_URL = click.prompt(f"Tautulli URL", type=str, default=CONFIG_DATA['TAUTULLI_URL'])
        TAUTULLI_KEY = click.prompt(f"Tautulli API Key", type=str, default=CONFIG_DATA['TAUTULLI_KEY'])


        try:
            response = get(f"{TAUTULLI_URL}/api/v2?apikey={TAUTULLI_KEY}&cmd=get_library_names").json()
            if response["response"]["result"] != "success":
                print(f"Tautulli Error: {response['response']['message']}")
            else:
                print("Success.\n==============================\n")
                tautulli = True
                yaml_obj['tautulli']['url'] = TAUTULLI_URL
                CONFIG_DATA['TAUTULLI_URL'] = TAUTULLI_URL
                yaml_obj['tautulli']['apikey'] = TAUTULLI_KEY
                CONFIG_DATA['TAUTULLI_KEY'] = TAUTULLI_KEY
                break
        except Exception as ex:
            print(f"I was unable to connect to {TAUTULLI_URL}")
            if yes_or_no("Would you like to enter a different URL or token?"):
                print("Cool.\n")
            else:
                print("I will continue with that URL and token.")
                break
    else:
        break


# omdb:
#   apikey: 9e62df51

OMDB_URL = "http://www.omdbapi.com/"

while True:
    if yes_or_no("Do you have an OMDB API Key?"):
        OMDB_KEY = click.prompt(f"OMDB API Key", type=str, default=CONFIG_DATA['OMDB_KEY'])

        try:
            response = get(OMDB_URL, params={"i": "tt0080684", "apikey": OMDB_KEY})
            if response.status_code < 400:
                print("Success.\n==============================\n")
                yaml_obj['omdb']['apikey'] = OMDB_KEY
                CONFIG_DATA['OMDB_KEY'] = OMDB_KEY
                break
            else:
                raise Failed(f"OMDb Error")
        except Exception as ex:
            print(f"I was unable to connect to {OMDB_URL}")
            if yes_or_no("Would you like to try a different token?"):
                print("Cool.\n")
            else:
                print("OMDB disabled.")
                break
    else:
        break

# mdblist:
#   apikey: #########################

MDB_URL = "https://mdblist.com/api/"

while True:
    if yes_or_no("Do you have an MDBList API Key?"):
        MDBLIST_KEY = click.prompt(f"MDBList API Key", type=str, default=CONFIG_DATA['MDBLIST_KEY'])

        try:
            response = get(MDB_URL, params={"i": "tt0080684", "apikey": MDBLIST_KEY})
            if response.status_code < 400:
                success = bool(response.json()["response"])
                if success:
                    print("Success.\n==============================\n")
                    yaml_obj['mdblist']['apikey'] = MDBLIST_KEY
                    CONFIG_DATA['MDBLIST_KEY'] = MDBLIST_KEY
                    break
                else:
                    raise Failed(response.json()["error"])
            else:
                raise Failed(f"MDBList Error")
        except Exception as ex:
            if response.status_code < 400:
                print(f"I was unable to connect to {MDB_URL}: {ex.args[0]}")
            else:
                print(f"I was unable to connect to {MDB_URL}: {response.status_code}")
            if yes_or_no("Would you like to try a different apikey?"):
                print("Cool.\n")
            else:
                print("MDBList disabled.")
                break
    else:
        break

# notifiarr:
#   apikey: 66fc0993-658c-475f-9827-83a7eeec01fa

NOTIFIARR_URL = "https://notifiarr.com/api/v1/"

while True:

    if yes_or_no("Do you have a Notifiarr API Key?"):
        NOTIFIARR_KEY = click.prompt(f"Notifiarr API Key", type=str, default=CONFIG_DATA['NOTIFIARR_KEY'])

        header = {"X-API-Key": NOTIFIARR_KEY}

        try:
            response = get(f"{NOTIFIARR_URL}user/pmm/", headers=header, params={"fetch": "settings"})
            if response.status_code < 400:
                try:
                    response_json = response.json()
                    print("Success.\n==============================\n")
                    yaml_obj['notifiarr']['apikey'] = NOTIFIARR_KEY
                    CONFIG_DATA['NOTIFIARR_KEY'] = NOTIFIARR_KEY
                    if yes_or_no("Would you like to configure notifications to go through Notifarr?"):
                        yaml_obj['webhooks']['error'] = 'notifiarr'
                        yaml_obj['webhooks']['version'] = 'notifiarr'
                        yaml_obj['webhooks']['run_start'] = 'notifiarr'
                        yaml_obj['webhooks']['run_end'] = 'notifiarr'
                        yaml_obj['webhooks']['changes'] = 'notifiarr'
                    break
                except JSONDecodeError as e:
                    if response.status_code >= 400 or ("result" in response_json and response_json["result"] == "error"):
                        raise Failed(f"({response.status_code} [{response.reason}]) {response_json}")
                    if not response_json["details"]["response"]:
                        raise Failed("Notifiarr Error: Invalid apikey")
            else:
                raise Failed(f"Notifiarr Error")
        except Exception as ex:
            print(f"I was unable to connect to {NOTIFIARR_URL}")
            if yes_or_no("Would you like to enter a different URL token?"):
                print("Cool.\n")
            else:
                print("Skipping Notifiarr.")
                break
    else:
        break

# anidb:
#   username: chazlarson
#   password: yxzPFe3H6WLC4R

ANIDB_BASE_URL = "https://anidb.net"
ANIDB_LOGIN_URL = f"{ANIDB_BASE_URL}/perl-bin/animedb.pl"

while True:
    if yes_or_no("Would you like to connect PMM to AniDB?"):
        ANIDB_USER = click.prompt(f"AniDB User", type=str, default=CONFIG_DATA['ANIDB_USER'])
        ANIDB_PASS = click.prompt(f"AniDB Password", type=str, default=CONFIG_DATA['ANIDB_PASS'])

        try:
            data = {"show": "main", "xuser": ANIDB_USER, "xpass": ANIDB_PASS, "xdoautologin": "on"}
            headers=def_header()
            response = post(ANIDB_LOGIN_URL, data=data, headers=headers)

            if response.status_code < 400:
                try:
                    response_html = html.fromstring(response.content)
                    if response_html.xpath("//li[@class='sub-menu my']/@title"):
                        print("Success.\n==============================\n")
                        yaml_obj['anidb']['username'] = ANIDB_USER
                        CONFIG_DATA['ANIDB_USER'] = ANIDB_USER
                        yaml_obj['anidb']['password'] = ANIDB_PASS
                        CONFIG_DATA['ANIDB_PASS'] = ANIDB_PASS
                        break
                    else:
                        raise Failed("AniDB Error")
                except Exception as e:
                    raise Failed("AniDB Error")
            else:
                raise Failed(f"AniDB Error")
        except Exception as ex:
            print(f"I was unable to connect to {ANIDB_LOGIN_URL}")
            if yes_or_no("Would you like to enter a different user/pass?"):
                print("Cool.\n")
            else:
                print("Skipping AniDB.")
                break
    else:
        break

while True:
    if yes_or_no("Would you like to connect PMM to Radarr?"):
        RADARR_URL = click.prompt(f"Radarr URL", type=str, default=CONFIG_DATA['RADARR_URL'])
        RADARR_TOKEN = click.prompt(f"Radarr API Key", type=str, default=CONFIG_DATA['RADARR_TOKEN'])

        try:
            radarr = RadarrAPI(RADARR_URL, RADARR_TOKEN, session=session)
            print("Success.\n==============================\n")
            yaml_obj['radarr']['url'] = RADARR_URL
            CONFIG_DATA['RADARR_URL'] = RADARR_URL
            yaml_obj['radarr']['token'] = RADARR_TOKEN
            CONFIG_DATA['RADARR_TOKEN'] = RADARR_TOKEN

            RADARR_PROFILES = radarr.quality_profile()
            if len(RADARR_PROFILES) > 1:
                for x in RADARR_PROFILES:
                    print(f"{x.id} - {x.name}")
                RADARR_PROFILE = good_value("Which profile should this Radarr instance use?  Enter the number", RADARR_PROFILES)
            else:
                RADARR_PROFILE = RADARR_PROFILES[0]

            print(f"Setting Quality Profile to: {RADARR_PROFILE.name}")
            yaml_obj['radarr']['quality_profile'] = RADARR_PROFILE.name

            RADARR_ROOTS = radarr.root_folder()
            if len(RADARR_ROOTS) > 1:
                for x in RADARR_ROOTS:
                    print(f"{x.id} - {x.path}")
                RADARR_ROOT = good_value("Which root folder should this Radarr instance use?  Enter the number", RADARR_ROOTS)
            else:
                RADARR_ROOT = RADARR_ROOTS[0]

            print(f"Setting Root Folder to: {RADARR_ROOT.path}")
            yaml_obj['radarr']['root_folder_path'] = RADARR_ROOT.path

            idx = 1
            RADARR_AVS = []
            for x in radarr.minimum_availability_options:
                d = {
                    'id': idx,
                    'name': x
                }
                n = SimpleNamespace(**d)
                RADARR_AVS.append(n)
                idx += 1
            for x in RADARR_AVS:
                print(f"{x.id} - {x.name}")
            RADARR_AV = good_value("Which availability option should this Radarr instance use?  Enter the number", RADARR_AVS)
            yaml_obj['radarr']['availability'] = RADARR_AV.name

            yaml_obj['radarr']['add_missing'] = yes_or_no("Would you like to add missing items to Radarr?  Note: This may add thousands of movies to Radarr. ")
            if yaml_obj['radarr']['add_missing']:
                yaml_obj['radarr']['monitor'] = yes_or_no("Should those items be added as monitored?")
                yaml_obj['radarr']['search'] = yes_or_no("Should Radarr initiate a search when those items are added?")

            # 'add_existing': False
            # 'tag': None
            # 'radarr_path': None
            # 'plex_path': None
            break
        except Exception as ex:
            print(f"I was unable to connect to {RADARR_URL}")
            if yes_or_no("Would you like to enter a different URL token?"):
                print("Cool.\n")
            else:
                print("I will continue with that URL and token.")
#                 print("I will ask for root folder and quality later.\n")
                print("You will need to configure the rest of this section manually.\n")
                break
    else:
        break

while True:
    if yes_or_no("Would you like to connect PMM to Sonarr?"):
        SONARR_URL = click.prompt(f"Sonarr URL", type=str, default=CONFIG_DATA['SONARR_URL'])
        SONARR_TOKEN = click.prompt(f"Sonarr API Key", type=str, default=CONFIG_DATA['SONARR_TOKEN'])

        try:
            sonarr = SonarrAPI(SONARR_URL, SONARR_TOKEN, session=session)

            print("Success.\n==============================\n")
            yaml_obj['sonarr']['url'] = SONARR_URL
            CONFIG_DATA['SONARR_URL'] = SONARR_URL
            yaml_obj['sonarr']['token'] = SONARR_TOKEN
            CONFIG_DATA['SONARR_TOKEN'] = SONARR_TOKEN

            SONARR_PROFILES = sonarr.quality_profile()
            if len(SONARR_PROFILES) > 1:
                for x in SONARR_PROFILES:
                    print(f"{x.id} - {x.name}")
                SONARR_PROFILE = good_value("Which profile should this Sonarr instance use?  Enter the number", SONARR_PROFILES)
            else:
                SONARR_PROFILE = SONARR_PROFILES[0]

            print(f"Setting Quality Profile to: {SONARR_PROFILE.name}")
            yaml_obj['sonarr']['quality_profile'] = SONARR_PROFILE.name

            SONARR_ROOTS = sonarr.root_folder()
            if len(SONARR_ROOTS) > 1:
                for x in SONARR_ROOTS:
                    print(f"{x.id} - {x.path}")
                SONARR_ROOT = good_value("Which root folder should this Sonarr instance use?  Enter the number", SONARR_ROOTS)
            else:
                SONARR_ROOT = SONARR_ROOTS[0]

            print(f"Setting Root Folder to: {SONARR_ROOT.path}")
            yaml_obj['sonarr']['root_folder_path'] = SONARR_ROOT.path

            SONARR_LANGS = sonarr.language_profile()
            if len(SONARR_LANGS) > 1:
                for x in SONARR_LANGS:
                    print(f"{x.id} - {x.name}")
                SONARR_LANG = good_value("Which language profile should this Sonarr instance use?  Enter the number", SONARR_LANGS)
            else:
                SONARR_LANG = SONARR_LANGS[0]

            print(f"Setting language profile to: {SONARR_LANG.name}")
            yaml_obj['sonarr']['language_profile'] = SONARR_LANG.name

            yaml_obj['sonarr']['add_missing'] = yes_or_no("Would you like to add missing items to Sonarr?  Note: This may add thousands of Shows to Sonarr. ")
            if yaml_obj['sonarr']['add_missing']:
                yaml_obj['sonarr']['monitor'] = yes_or_no("Should those items be added as monitored?")
                if yaml_obj['sonarr']['monitor']:
                    idx = 1
                    SONARR_MONS = []
                    for x in sonarr.monitor_options:
                        d = {
                            'id': idx,
                            'name': x
                        }
                        n = SimpleNamespace(**d)
                        SONARR_MONS.append(n)
                        idx += 1
                    for x in SONARR_MONS:
                        print(f"{x.id} - {x.name}")
                    SONARR_MON = good_value("Default monitoring level?  Enter the number", SONARR_MONS)
                    yaml_obj['sonarr']['monitor'] = SONARR_MON.name

                    idx = 1
                    SONARR_TYPES = []
                    for x in sonarr.series_type_options:
                        d = {
                            'id': idx,
                            'name': x
                        }
                        n = SimpleNamespace(**d)
                        SONARR_TYPES.append(n)
                        idx += 1
                    for x in SONARR_TYPES:
                        print(f"{x.id} - {x.name}")
                    SONARR_TYPE = good_value("Default series type?  Enter the number", SONARR_TYPES)
                    yaml_obj['sonarr']['series_type'] = SONARR_TYPE.name

                    yaml_obj['sonarr']['season_folder'] = yes_or_no("Should Sonarr use season folders by default?")

                    yaml_obj['sonarr']['search'] = yes_or_no("Should Sonarr initiate a search when those items are added?")

                    yaml_obj['sonarr']['cutoff_search'] = yes_or_no("Should Sonarr initiate a cutoff-unmet search when those items are added?")
                else:
                    yaml_obj['sonarr']['monitor'] = None

# 'tag': None
# 'add_existing': False
# 'sonarr_path': None
# 'plex_path': None

            break
        except Exception as ex:
            print(f"I was unable to connect to {SONARR_URL}")
            if yes_or_no("Would you like to enter a different URL token?"):
                print("Cool.\n")
            else:
                print("I will continue with that URL and token.")
#                 print("I will ask for root folder and quality later.\n")
                print("You will need to configure the rest of this section manually.\n")
                break
    else:
        break

# trakt:
#   client_id: 075daaa5d675d407596911afbdc535fef93102af21131f9a159a0c32446688fa
#   client_secret: 4b88ffc362979ddd223216c120202e68999af02f28beb275a5c1b2f11f3c9770

trakt = False
TRAKT_CLIENT_ID = None
TRAKT_CLIENT_SECRET = None

redirect_uri = "urn:ietf:wg:oauth:2.0:oob"
redirect_uri_encoded = redirect_uri.replace(":", "%3A")
base_url = "https://api.trakt.tv"

while True:
    try:
        if yes_or_no("Would you like to connect PMM to Trakt?"):
            response = requests.get(f"{base_url}/oauth/token")
            if response.status_code == 503:
                print("Trakt Error: Trakt Not Available")
                break
            TRAKT_CLIENT_ID = click.prompt(f"Trakt Client ID", type=str, default=CONFIG_DATA['TRAKT_CLIENT_ID'])
            TRAKT_CLIENT_SECRET = click.prompt(f"Trakt Client Secret", type=str, default=CONFIG_DATA['TRAKT_CLIENT_SECRET'])

            url = f"https://trakt.tv/oauth/authorize?response_type=code&client_id={TRAKT_CLIENT_ID}&redirect_uri={redirect_uri_encoded}"

            print(f"Open this URL in a browser: {url}")
            print(f"If you get an OAuth error in the browser your Client ID or Client Secret is invalid.")
            print(f"Log into Trakt if required and the page will present a PIN.")
            print(f"Copy that PIN and come back here.")

            TRAKT_PIN = click.prompt(f"Enter the Trakt pin [hit enter if the page displayed an error]", type=str, default='99999').lower().strip()

            if TRAKT_PIN != "99999":
                req_json = {
                    "code": TRAKT_PIN,
                    "client_id": TRAKT_CLIENT_ID,
                    "client_secret": TRAKT_CLIENT_SECRET,
                    "redirect_uri": redirect_uri,
                    "grant_type": "authorization_code",
                }
                response = post(
                    f"{base_url}/oauth/token", json=req_json, headers={"Content-Type": "application/json"}
                )

                if response.status_code != 200:
                    print(
                        "Trakt Error: Invalid trakt pin. If you're sure you typed it in correctly your client_id or client_secret may be invalid"
                    )
                else:
                    print("Authentication successful; validating credentials...")

                    headers = {
                        "Content-Type": "application/json",
                        "Authorization": f"Bearer {response.json()['access_token']}",
                        "trakt-api-version": "2",
                        "trakt-api-key": TRAKT_CLIENT_ID,
                    }

                    validation_response = requests.get(f"{base_url}/users/settings", headers=headers)
                    if validation_response.status_code == 423:
                        print("Trakt Error: Account is locked; please contact Trakt Support")
                    else:

                        # 'client_id': None
                        # 'client_secret': None
                        # 'pin': None
                        # 'authorization': {'access_token': None, 'token_type': None, 'expires_in': None, 'refresh_token': None, 'scope': 'public', 'created_at': None}

                        trakt = True
                        yaml_obj['trakt']["client_id"] = TRAKT_CLIENT_ID
                        CONFIG_DATA['TRAKT_CLIENT_ID'] = TRAKT_CLIENT_ID
                        yaml_obj['trakt']["client_secret"] = TRAKT_CLIENT_SECRET
                        CONFIG_DATA['TRAKT_CLIENT_SECRET'] = TRAKT_CLIENT_SECRET
                        yaml_obj['trakt']["authorization"]["access_token"] = response.json()['access_token']
                        yaml_obj['trakt']["authorization"]["token_type"] = response.json()['token_type']
                        yaml_obj['trakt']["authorization"]["expires_in"] = response.json()['expires_in']
                        yaml_obj['trakt']["authorization"]["refresh_token"] = response.json()['refresh_token']
                        yaml_obj['trakt']["authorization"]["scope"] = response.json()['scope']
                        yaml_obj['trakt']["authorization"]["created_at"] = response.json()['created_at']
                        print("Success.\n==============================\n")
                        break

            else:
                if yes_or_no("Would you like to enter a different Client ID/Secret or try for another PIN?"):
                    print("Cool.\n")
                else:
                    print("Skipping Trakt.")
                    break
        else:
            break
    except Exception as ex:
        print(f"I was unable to authenticate against Trakt")
        if yes_or_no("Would you like to try again?"):
            print("Cool.\n")
        else:
            print("Proceeding without Trakt.\n")
            break

# mal:
myanimelist = False
MAL_CLIENT_ID = None
MAL_CLIENT_SECRET = None
MAL_TOKEN_URL = "https://myanimelist.net/v1/oauth2/token"
MAL_AUTHORIZE_URL = "https://myanimelist.net/v1/oauth2/authorize"
LOCAL_URL = ""

while True:
    try:
        if yes_or_no("Would you like to connect PMM to MyAnimeList?"):
            MAL_CLIENT_ID = click.prompt(f"MyAnimeList Client ID", type=str, default=CONFIG_DATA['MAL_CLIENT_ID'])
            MAL_CLIENT_SECRET = click.prompt(f"MyAnimeList Client Secret", type=str, default=CONFIG_DATA['MAL_CLIENT_SECRET'])

            code_verifier = secrets.token_urlsafe(100)[:128]
            url = f"{MAL_AUTHORIZE_URL}?response_type=code&client_id={MAL_CLIENT_ID}&code_challenge={code_verifier}"

            print(f"Open this URL:{os.linesep}{url}{os.linesep}{os.linesep}")
            print(f"Log in and click the Allow option.{os.linesep}")
            print(
                f"You will be redirected to a localhost url that won't load.{os.linesep}"
            )
            print(f"That's fine.  Copy that localhost URL and paste it below.{os.linesep}{os.linesep}")

            LOCAL_URL = click.prompt(f"URL", type=str, default='')

            match = re.search("code=([^&]+)", str(LOCAL_URL))
            if not match:
                print(f"Couldn't find the required code in that URL.{os.linesep}")
                raise Failed(f"URL Error")

            code = match.group(1)

            data = {
                "client_id": MAL_CLIENT_ID,
                "client_secret": MAL_CLIENT_SECRET,
                "code": code,
                "code_verifier": code_verifier,
                "grant_type": "authorization_code",
            }

            new_authorization = post(url=MAL_TOKEN_URL, data=data).json()

            if "error" in new_authorization:
                print(f"ERROR: invalid code.{os.linesep}")
                raise Failed(f"URL Error")

            myanimelist = True
            yaml_obj['mal']["client_id"] = MAL_CLIENT_ID
            CONFIG_DATA['MAL_CLIENT_ID'] = MAL_CLIENT_ID
            yaml_obj['mal']["client_secret"] = MAL_CLIENT_SECRET
            CONFIG_DATA['MAL_CLIENT_SECRET'] = MAL_CLIENT_SECRET
            yaml_obj['mal']["authorization"]["access_token"] = new_authorization["access_token"]
            yaml_obj['mal']["authorization"]["token_type"] = new_authorization["token_type"]
            yaml_obj['mal']["authorization"]["expires_in"] = new_authorization["expires_in"]
            yaml_obj['mal']["authorization"]["refresh_token"] = new_authorization["refresh_token"]
            print("Success.\n==============================\n")

            break
        else:
            break

    except Exception as ex:
        print(f"I was unable to find the correct code in {LOCAL_URL}")
        if yes_or_no("Would you like to try again?"):
            print("Cool.\n")
        else:
            print("Proceeding without MyAnimeList.\n")
            break
print("Service connections complete.\n==============================\n")

print("Writing config.json.\n==============================\n")
with open("config.json", "w") as outfile:
    json.dump(CONFIG_DATA, outfile, indent=4)

print("Gathering Library details.\n==============================\n")

while True:
    if plex is not None:
        process_sections(plex)
        break

print("Writing final config file.\n==============================\n")
with open('config.yml', 'w') as outfile:
    yaml_str = yaml.safe_dump(yaml_obj).replace(r"''", '').replace(": null", ":")
    outfile.write(yaml_str)

print("Config generation Complete.\n==============================\n")

exit()
