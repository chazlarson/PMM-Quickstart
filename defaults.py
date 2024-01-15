
class DefaultFile:
    def __init__(self, kind, group, name, path, notes, movie, shows, seasons=False, episodes=False, trakt=False, tautulli=False, myanimelist=False, mdblist=False, basic=False ):
        self.kind = kind
        self.group = group
        self.name = name
        self.path = path
        self.notes = notes
        self.movie = movie
        self.shows = shows
        self.seasons = seasons
        self.episodes = episodes
        self.trakt = trakt
        self.tautulli = tautulli
        self.myanimelist = myanimelist
        self.mdblist = mdblist
        self.basic = basic

DEFAULT_COLLECTION_TYPES = [
{"name": "Award",    "note": "Awards collections like the Emmys, Oscars, and Baftas"},
{"name": "Chart",    "note": "'top list' collections like the IMDB Top 250"},
{"name": "General",  "note": "People, Franchises, Years, Ratings, etc."},
]

DEFAULT_COLLECTIONS = [
DefaultFile('collection', "General",  "Actor",                                        "actor",               "Chris Hemsworth, Margot Robbie",                                           True,   True,   False,  False,  False,  False,  False,  False,  False),
DefaultFile('collection', "Chart",    "AniList",                                      "anilist",             "AniList Popular, AniList Season",                                          True,   True,   False,  False,  False,  False,  False,  False,  False),
DefaultFile('collection', "General",  "Audio Language",                               "audio_language",      "French Audio, Korean Audio",                                               True,   True,   False,  False,  False,  False,  False,  False,  False),
DefaultFile('collection', "Award",    "British Academy of Film and Television Arts",  "bafta",               "BAFTA Best Films, BAFTA 2021",                                             True,   False,  False,  False,  False,  False,  False,  False,  False),
DefaultFile('collection', "Chart",    "Basic",                                        "basic",               "Newly Released, New Episodes",                                             True,   True,   False,  False,  False,  False,  False,  False,  True),
DefaultFile('collection', "Award",    "Cannes",                                       "cannes",              "Cannes - Palme d’or, Cannes 2018",                                         True,   False,  False,  False,  False,  False,  False,  False,  False),
DefaultFile('collection', "Award",    "Critics Choice",                               "choice",              "Critics Choice Awards 2020",                                               True,   True,   False,  False,  False,  False,  False,  False,  False),
DefaultFile('collection', "General",  "Collectionless",                               "collectionless",      "Collectionless",                                                           True,   True,   False,  False,  False,  False,  False,  False,  False),
DefaultFile('collection', "General",  "Common Sense Content Rating",                  "content_rating_cs",   "1, 2, 3, 4, 5, 6, 15, 16, 17, 18",                                         True,   True,   False,  False,  False,  False,  False,  False,  False),
DefaultFile('collection', "General",  "MyAnimeList Content Rating",                   "content_rating_mal",  "G, PG, PG-13, R, R+, Rx",                                                  True,   True,   False,  False,  False,  False,  True,   False,  False),
DefaultFile('collection', "General",  "Content Rating (UK)",                          "content_rating_uk",   "U, PG, 12A",                                                               True,   True,   False,  False,  False,  False,  False,  False,  False),
DefaultFile('collection', "General",  "Content Rating (US) Movie/Show",               "content_rating_us",   "G, PG, NC-17",                                                             True,   True,   False,  False,  False,  False,  False,  False,  False),
DefaultFile('collection', "General",  "Country Movie/Show",                           "country",             "Belgium, India",                                                           True,   True,   False,  False,  False,  False,  False,  False,  False),
DefaultFile('collection', "General",  "Decade Movie/Show",                            "decade",              "Best of 2012, Best of 2022",                                               True,   True,   False,  False,  False,  False,  False,  False,  False),
DefaultFile('collection', "General",  "Director",                                     "director",            "Steven Spielberg (Director), Olivia Wilde (Director)",                     True,   False,  False,  False,  False,  False,  False,  False,  False),
DefaultFile('collection', "Award",    "Emmys",                                        "emmy",                "Emmys 2021",                                                               True,   True,   False,  False,  False,  False,  False,  False,  False),
DefaultFile('collection', "Chart",    "FlixPatrol",                                   "flixpatrol",          "Top Disney, Top Hbo, Top Hulu, Top Netflix",                               True,   True,   False,  False,  False,  False,  False,  False,  False),
DefaultFile('collection', "General",  "Franchise Movie/Show",                         "franchise",           "Star Wars: Skywalker Saga, Godzilla (Anime)",                              True,   True,   False,  False,  False,  False,  False,  False,  False),
DefaultFile('collection', "General",  "Genre",                                        "genre",               "Action, Drama, Science Fiction",                                           True,   True,   False,  False,  False,  False,  False,  False,  False),
DefaultFile('collection', "Award",    "Golden Globes",                                "golden",              "Best Motion Pictures",                                                     True,   True,   False,  False,  False,  False,  False,  False,  False),
DefaultFile('collection', "Chart",    "IMDb",                                         "imdb",                "IMDb Popular, IMDb Top 250",                                               True,   True,   False,  False,  False,  False,  False,  False,  True),
DefaultFile('collection', "Chart",    "MyAnimeList",                                  "myanimelist",         "MyAnimeList Popular, MyAnimeList Top Rated",                               True,   True,   False,  False,  False,  False,  True,   False,  False),
DefaultFile('collection', "General",  "Network",                                      "network",             "Disney Channel, Lifetime",                                                 False,  True,   False,  False,  False,  False,  False,  False,  False),
DefaultFile('collection', "Award",    "Academy Awards (Oscars)",                      "oscars",              "Best Picture Winners",                                                     True,   True,   False,  False,  False,  False,  False,  False,  False),
DefaultFile('collection', "Award",    "Other",                                        "other_award",         "Berlinale Golden Bears, Venice Golden Lions",                              True,   False,  False,  False,  False,  False,  False,  False,  False),
DefaultFile('collection', "Chart",    "Other",                                        "other_chart",         "AniDB Popular, Common Sense Selection",                                    True,   True,   False,  False,  False,  False,  False,  False,  False),
DefaultFile('collection', "General",  "Producer",                                     "producer",            "James Cameron (Producer), Reese Witherspoon (Producer)",                   True,   False,  False,  False,  False,  False,  False,  False,  False),
DefaultFile('collection', "General",  "Resolution",                                   "resolution",          "4K Movies, 1080p Movies, 720p Movies",                                     True,   True,   False,  False,  False,  False,  False,  False,  False),
DefaultFile('collection', "General",  "Seasonal",                                     "seasonal",            "Easter, Christmas",                                                        True,   False,  False,  False,  False,  False,  False,  False,  False),
DefaultFile('collection', "Award",    "Award Separator",                              "separator_award",     "Award Collections",                                                        True,   True,   False,  False,  False,  False,  False,  False,  False),
DefaultFile('collection', "Chart",    "Chart Separator",                              "separator_chart",     "Chart Collections",                                                        True,   True,   False,  False,  False,  False,  False,  False,  False),
DefaultFile('collection', "Award",    "Independent Spirit",                           "spirit",              "Independent Spirit Awards 2021",                                           True,   False,  False,  False,  False,  False,  False,  False,  False),
DefaultFile('collection', "General",  "Streaming",                                    "streaming",           "Disney+ Movies, HBO Max Shows",                                            True,   True,   False,  False,  False,  False,  False,  False,  True),
DefaultFile('collection', "General",  "Studio",                                       "studio",              "DreamWorks Studios, Walt Disney Pictures",                                 True,   True,   False,  False,  False,  False,  False,  False,  False),
DefaultFile('collection', "General",  "Anime Studio",                                 "studio_anime",        "Bones, Studio Ghibli, Toei Animation",                                     True,   True,   False,  False,  False,  False,  False,  False,  False),
DefaultFile('collection', "General",  "Subtitle Language",                            "subtitle_language",   "German Subtitles, Swedish Subtitles",                                      True,   True,   False,  False,  False,  False,  False,  False,  False),
DefaultFile('collection', "Award",    "Sundance",                                     "sundance",            "Sundance Grand Jury Winners",                                              True,   True,   False,  False,  False,  False,  False,  False,  False),
DefaultFile('collection', "Chart",    "Tautulli",                                     "tautulli",            "Plex Popular, Plex Watched",                                               True,   True,   False,  False,  False,  True,   False,  False,  False),
DefaultFile('collection', "Chart",    "TMDb",                                         "tmdb",                "TMDb Popular, TMDb Airing Today",                                          True,   True,   False,  False,  False,  False,  False,  False,  True),
DefaultFile('collection', "Chart",    "Trakt",                                        "trakt",               "Trakt Popular, Trakt Trending",                                            True,   True,   False,  False,  True,   False,  False,  False,  False),
DefaultFile('collection', "General",  "Universe",                                     "universe",            "Marvel Cinematic Universal, Wizarding World",                              True,   False,  False,  False,  True,   False,  False,  False,  True),
DefaultFile('collection', "General",  "Writer",                                       "writer",              "James Cameron (Writer), Lilly Wachowski (Writer)",                         True,   False,  False,  False,  False,  False,  False,  False,  False),
DefaultFile('collection', "General",  "Year",                                         "year",                "Best of 2010, Best of 2019",                                               True,   True,   False,  False,  False,  False,  False,  False,  False),
]

DEFAULT_OVERLAYS = [
DefaultFile('overlay',    None,       "Audio Codec",                                 "audio_codec",          'Dolby Atmos logo, DTS logo',                                               True,   True,   True,   True,   False,  False,  False,  False,  True),
DefaultFile('overlay',    None,       "CommonSense Age Rating",                      "commonsense",          '“3+”, “16+”',                                                              True,   True,   False,  False,  False,  False,  False,  False,  False),
DefaultFile('overlay',    None,       "Direct Play",                                 "direct_play",          '“Direct Play Only”',                                                       True,   False,  False,  True,   False,  False,  False,  False,  False),
DefaultFile('overlay',    None,       "Episode Info",                                "episode_info",         '“S01E01”, “S02E09”',                                                       False,  False,  False,  True,   False,  False,  False,  False,  False),
DefaultFile('overlay',    None,       "FlixPatrol",                                  "flixpatrol",           '“Streaming service logo with words “TOP”',                                 True,   True,   False,  False,  False,  False,  False,  False,  False),
DefaultFile('overlay',    None,       "Language Count",                              "language_count",       'Dual-Audio, Multi-Audio, Dual-Subtitle, Multi-Subtitle',                   True,   True,   True,   True,   False,  False,  False,  False,  False),
DefaultFile('overlay',    None,       "Languages",                                   "languages",            'Flags Based on the Audio/Subtitles a file has',                            True,   True,   True,   True,   False,  False,  False,  False,  False),
DefaultFile('overlay',    None,       "Mediastinger",                                "mediastinger",         'Mediastinger Logo for After/During Credit Scenes',                         True,   True,   False,  False,  False,  False,  False,  False,  False),
DefaultFile('overlay',    None,       "Ratings",                                     "ratings",              'IMDb Audience Rating, Metacritic Critic Rating',                           True,   True,   False,  True,   False,  False,  False,  False,  False),
DefaultFile('overlay',    None,       "Resolution/Editions",                         "resolution",           '4K Dolby Vision logo, 720P logo, “Extended Cut”, “Criterion Collection”',  True,   True,   False,  True,   False,  False,  False,  False,  True),
DefaultFile('overlay',    None,       "Ribbon",                                      "ribbon",               'IMDb Top 250 Ribbon, RT Fresh Ribbon',                                     True,   True,   False,  False,  False,  False,  False,  False,  False),
DefaultFile('overlay',    None,       "Runtimes",                                    "runtimes",             'Runtime: 1h 30m',                                                          True,   True,   False,  False,  False,  False,  False,  False,  False),
DefaultFile('overlay',    None,       "Status",                                      "status",               'Airing, Returning, Canceled, Ended',                                       False,  True,   False,  False,  False,  False,  False,  False,  False),
DefaultFile('overlay',    None,       "Streaming",                                   "streaming",            'Netflix logo, Hulu logo',                                                  True,   True,   False,  False,  False,  False,  False,  False,  False),
DefaultFile('overlay',    None,       "Versions",                                    "versions",             'Multiple Versions logo',                                                   True,   True,   True,   True,   False,  False,  False,  False,  False),
DefaultFile('overlay',    None,       "Video Format",                                "video_format",         '“REMUX”, “HDTV”',                                                          True,   False,  False,  True,   False,  False,  False,  False,  True),
]

class PMMOp:
    def __init__(self, name, path, notes, movie, music, shows, seasons=False, episodes=False ):
        self.name = name
        self.path = path
        self.notes = notes
        self.movie = movie
        self.music = music
        self.shows = shows
        self.seasons = seasons
        self.episodes = episodes

class PMMOpOption:
    def __init__(self, name, group, notes, trakt=False, tautulli=False, myanimelist=False, mdblist=False, omdb=False, anidb=False):
        self.group = group
        self.name = name
        self.notes = notes
        self.trakt = trakt
        self.tautulli = tautulli
        self.myanimelist = myanimelist
        self.mdblist = mdblist
        self.omdb = omdb
        self.anidb = anidb

    #  name                          path                          notes                                                                                                         movie  music  shows  seasons episodes
BOOLEAN_OPERATIONS = [
PMMOp("Assets For All",             "assets_for_all",             "search in assets for images for every item in this library",                                                 True,  True,  True,  False,  False),
PMMOp("Update Blank Track Titles",  "update_blank_track_titles",  "search though every track in a music library and replace any blank track titles with the tracks sort title", False, True,  False, False,  False),
PMMOp("Remove Title Parentheses",   "remove_title_parentheses",   "search through every title and remove all ending parentheses in an item's title if the title is not locked",  True,  True,  True,  False,  False),
PMMOp("Split Duplicates",           "split_duplicates",           "split all duplicate movies/shows found in this library",                                                    True,  True,  True,  False,  False),
]

RATING_TYPES = [
"audience",
"critic",
"user"
]

CONFIG_OPERATIONS = [
PMMOp("Mass Genre Update",                 "mass_genre_update",                      "Updates every item's genres in the library to the chosen site's genres.",True, True, False, False),
PMMOp("Mass Content Rating Update",        "mass_content_rating_update",             "Updates every item's content rating in the library to the chosen site's content rating.",True, True, False, False),
PMMOp("Mass Original Title Update",        "mass_original_title_update",             "Updates every item's original title in the library to the chosen site's original title.",True, True, False, False),
PMMOp("Mass Originally Available Update",  "mass_originally_available_update",       "Updates every item's originally available date in the library to the chosen site's date.",True, True, False, False),
PMMOp("Mass * Rating Update",              "mass_RATINGTYPE_rating_update",          "Updates every item's audience/critic/user rating in the library to the chosen site's rating.",True, True, False, False),
PMMOp("Mass Episode * Rating Update",      "mass_episode_RATINGTYPE_rating_update",  "Updates every item's episode's audience/critic/user rating in the library to the chosen site's rating.",True, True, False, False),
PMMOp("Mass Poster Update",                "mass_poster_update",                     "Updates every item's poster to the chosen sites poster. Will fallback to `plex` if the given option fails. Assets will be used over anything else.",True, True, False, False),
PMMOp("Mass Background Update",            "mass_background_update",                 "Updates every item's background to the chosen sites background. Will fallback to `plex` if the given option fails. Assets will be used over anything else.",True, True, False, False),
PMMOp("Mass IMDb Parental Labels",         "mass_imdb_parental_labels",              "Updates every item's labels in the library to match the IMDb Parental Guide",True, True, False, False),
PMMOp("Mass Collection Mode",              "mass_collection_mode",                   "Updates every Collection in your library to the specified Collection Mode.",True, True, False, False),
]

#            group                                name                     notes                                                                                              trakt   tautulli   myanimelist   mdblist   omdb    anidb
PMM_OP_OPTIONS = [
PMMOpOption("mass_background_update",            "lock",                  "Lock Background",                                                                                  False,  False,     False,        False,    False,  False),
PMMOpOption("mass_background_update",            "plex",                  "Use Plex Background",                                                                              False,  False,     False,        False,    False,  False),
PMMOpOption("mass_background_update",            "tmdb",                  "Use TMDb Background",                                                                              False,  False,     False,        False,    False,  False),
PMMOpOption("mass_background_update",            "unlock",                "Unlock Background",                                                                                False,  False,     False,        False,    False,  False),
PMMOpOption("mass_collection_mode",              "default",               "Library default",                                                                                  False,  False,     False,        False,    False,  False),
PMMOpOption("mass_collection_mode",              "hide",                  "Hide Collection",                                                                                  False,  False,     False,        False,    False,  False),
PMMOpOption("mass_collection_mode",              "hide_items",            "Hide Items in this Collection",                                                                    False,  False,     False,        False,    False,  False),
PMMOpOption("mass_collection_mode",              "show_items",            "Show this Collection and its Items",                                                               False,  False,     False,        False,    False,  False),
PMMOpOption("mass_content_rating_update",        "lock",                  "Lock Content Rating Field",                                                                        False,  False,     False,        False,    False,  False),
PMMOpOption("mass_content_rating_update",        "mal",                   "Use MyAnimeList for Content Ratings",                                                              False,  False,     True,         False,    False,  False),
PMMOpOption("mass_content_rating_update",        "mdb",                   "Use MdbList for Content Ratings",                                                                  False,  False,     False,        True,     False,  False),
PMMOpOption("mass_content_rating_update",        "mdb_commonsense",       "Use Commonsense Rating through MDbList for Content Ratings",                                       False,  False,     False,        True,     False,  False),
PMMOpOption("mass_content_rating_update",        "mdb_commonsense0",      "Use Commonsense Rating with Zero Padding through MDbList for Content Ratings",                     False,  False,     False,        True,     False,  False),
PMMOpOption("mass_content_rating_update",        "omdb",                  "Use IMDb through OMDb for Content Ratings",                                                        False,  False,     False,        False,    True,   False),
PMMOpOption("mass_content_rating_update",        "remove",                "Remove Content Rating and Lock Field",                                                             False,  False,     False,        False,    False,  False),
PMMOpOption("mass_content_rating_update",        "reset",                 "Remove Content Rating and Unlock Field",                                                           False,  False,     False,        False,    False,  False),
PMMOpOption("mass_content_rating_update",        "unlock",                "Unlock Content Rating Field",                                                                      False,  False,     False,        False,    False,  False),
PMMOpOption("mass_episode_rating_update",        "imdb",                  "Use IMDb Rating",                                                                                  False,  False,     False,        False,    False,  False),
PMMOpOption("mass_episode_rating_update",        "lock",                  "Lock Rating Field",                                                                                False,  False,     False,        False,    False,  False),
PMMOpOption("mass_episode_rating_update",        "remove",                "Remove Rating and Lock Field",                                                                     False,  False,     False,        False,    False,  False),
PMMOpOption("mass_episode_rating_update",        "reset",                 "Remove Rating and Unlock Field",                                                                   False,  False,     False,        False,    False,  False),
PMMOpOption("mass_episode_rating_update",        "tmdb",                  "Use TMDb Rating",                                                                                  False,  False,     False,        False,    False,  False),
PMMOpOption("mass_episode_rating_update",        "unlock",                "Unlock Rating Field",                                                                              False,  False,     False,        False,    False,  False),
PMMOpOption("mass_genre_update",                 "anidb",                 "Use AniDB Tags for Genres",                                                                        False,  False,     False,        False,    False,  True),
PMMOpOption("mass_genre_update",                 "imdb",                  "Use IMDb for Genres",                                                                              False,  False,     False,        False,    False,  False),
PMMOpOption("mass_genre_update",                 "lock",                  "Lock Genre Field",                                                                                 False,  False,     False,        False,    False,  False),
PMMOpOption("mass_genre_update",                 "mal",                   "Use MyAnimeList for Genres",                                                                       False,  False,     True,         False,    False,  False),
PMMOpOption("mass_genre_update",                 "omdb",                  "Use IMDb through OMDb for Genres",                                                                 False,  False,     False,        False,    True,   False),
PMMOpOption("mass_genre_update",                 "reset",                 "Remove all Genres and Unlock Field",                                                               False,  False,     False,        False,    False,  False),
PMMOpOption("mass_genre_update",                 "remove",                "Remove all Genres and Lock Field",                                                                 False,  False,     False,        False,    False,  False),
PMMOpOption("mass_genre_update",                 "tmdb",                  "Use TMDb for Genres",                                                                              False,  False,     False,        False,    False,  False),
PMMOpOption("mass_genre_update",                 "tvdb",                  "Use TVDb for Genres",                                                                              False,  False,     False,        False,    False,  False),
PMMOpOption("mass_genre_update",                 "unlock",                "Unlock Genre Field",                                                                               False,  False,     False,        False,    False,  False),
PMMOpOption("mass_original_title_update",        "anidb",                 "Use AniDB Main Title for Original Titles",                                                         False,  False,     False,        False,    False,  True),
PMMOpOption("mass_original_title_update",        "anidb_official",        "Use AniDB Official Title based on the language attribute in the config file for Original Titles",  False,  False,     False,        False,    False,  True),
PMMOpOption("mass_original_title_update",        "lock",                  "Lock Original Title Field",                                                                        False,  False,     False,        False,    False,  False),
PMMOpOption("mass_original_title_update",        "mal",                   "Use MyAnimeList Main Title for Original Titles",                                                   False,  False,     True,         False,    False,  False),
PMMOpOption("mass_original_title_update",        "mal_english",           "Use MyAnimeList English Title for Original Titles",                                                False,  False,     True,         False,    False,  False),
PMMOpOption("mass_original_title_update",        "mal_japanese",          "Use MyAnimeList Japanese Title for Original Titles",                                               False,  False,     True,         False,    False,  False),
PMMOpOption("mass_original_title_update",        "remove",                "Remove Original Title and Lock Field",                                                             False,  False,     False,        False,    False,  False),
PMMOpOption("mass_original_title_update",        "reset",                 "Remove Original Title and Unlock Field",                                                           False,  False,     False,        False,    False,  False),
PMMOpOption("mass_original_title_update",        "unlock",                "Unlock Original Title Field",                                                                      False,  False,     False,        False,    False,  False),
PMMOpOption("mass_originally_available_update",  "anidb",                 "Use AniDB Release Date",                                                                           False,  False,     False,        False,    False,  True),
PMMOpOption("mass_originally_available_update",  "lock",                  "Lock Originally Available Field",                                                                  False,  False,     False,        False,    False,  False),
PMMOpOption("mass_originally_available_update",  "mal",                   "Use MyAnimeList Release Date",                                                                     False,  False,     True,         False,    False,  False),
PMMOpOption("mass_originally_available_update",  "mdb",                   "Use MdbList Release Date",                                                                         False,  False,     False,        True,     False,  False),
PMMOpOption("mass_originally_available_update",  "omdb",                  "Use IMDb Release Date through OMDb",                                                               False,  False,     False,        False,    True,   False),
PMMOpOption("mass_originally_available_update",  "remove",                "Remove Originally Available and Lock Field",                                                       False,  False,     False,        False,    False,  False),
PMMOpOption("mass_originally_available_update",  "reset",                 "Remove Originally Available and Unlock Field",                                                     False,  False,     False,        False,    False,  False),
PMMOpOption("mass_originally_available_update",  "tmdb",                  "Use TMDb Release Date",                                                                            False,  False,     False,        False,    False,  False),
PMMOpOption("mass_originally_available_update",  "tvdb",                  "Use TVDb Release Date",                                                                            False,  False,     False,        False,    False,  False),
PMMOpOption("mass_originally_available_update",  "unlock",                "Unlock Originally Available Field",                                                                False,  False,     False,        False,    False,  False),
PMMOpOption("mass_poster_update",                "lock",                  "Lock Poster",                                                                                      False,  False,     False,        False,    False,  False),
PMMOpOption("mass_poster_update",                "plex",                  "Use Plex Poster",                                                                                  False,  False,     False,        False,    False,  False),
PMMOpOption("mass_poster_update",                "tmdb",                  "Use TMDb Poster",                                                                                  False,  False,     False,        False,    False,  False),
PMMOpOption("mass_poster_update",                "unlock",                "Unlock Poster",                                                                                    False,  False,     False,        False,    False,  False),
PMMOpOption("mass_rating_update",                "anidb_average",         "Use AniDB Average",                                                                                False,  False,     False,        False,    False,  True),
PMMOpOption("mass_rating_update",                "anidb_rating",          "Use AniDB Rating",                                                                                 False,  False,     False,        False,    False,  True),
PMMOpOption("mass_rating_update",                "anidb_score",           "Use AniDB Review Score",                                                                           False,  False,     False,        False,    False,  True),
PMMOpOption("mass_rating_update",                "imdb",                  "Use IMDb Rating",                                                                                  False,  False,     False,        False,    False,  False),
PMMOpOption("mass_rating_update",                "lock",                  "Lock Rating Field",                                                                                False,  False,     False,        False,    False,  False),
PMMOpOption("mass_rating_update",                "mal",                   "Use MyAnimeList Score",                                                                            False,  False,     True,         False,    False,  False),
PMMOpOption("mass_rating_update",                "mdb",                   "Use MdbList Score",                                                                                False,  False,     False,        True,     False,  False),
PMMOpOption("mass_rating_update",                "mdb_average",           "Use MdbList Average Score",                                                                        False,  False,     False,        True,     False,  False),
PMMOpOption("mass_rating_update",                "mdb_imdb",              "Use IMDb Rating through MDbList",                                                                  False,  False,     False,        True,     False,  False),
PMMOpOption("mass_rating_update",                "mdb_letterboxd",        "Use Letterboxd Rating through MDbList",                                                            False,  False,     False,        True,     False,  False),
PMMOpOption("mass_rating_update",                "mdb_metacritic",        "Use Metacritic Rating through MDbList",                                                            False,  False,     False,        True,     False,  False),
PMMOpOption("mass_rating_update",                "mdb_metacriticuser",    "Use Metacritic User Rating through MDbList",                                                       False,  False,     False,        True,     False,  False),
PMMOpOption("mass_rating_update",                "mdb_myanimelist",       "Use MyAnimeList Rating through MDbList",                                                           False,  False,     False,        True,     False,  False),
PMMOpOption("mass_rating_update",                "mdb_tmdb",              "Use TMDb Rating through MDbList",                                                                  False,  False,     False,        True,     False,  False),
PMMOpOption("mass_rating_update",                "mdb_tomatoes",          "Use Rotten Tomatoes Rating through MDbList",                                                       False,  False,     False,        True,     False,  False),
PMMOpOption("mass_rating_update",                "mdb_tomatoesaudience",  "Use Rotten Tomatoes Audience Rating through MDbList",                                              False,  False,     False,        True,     False,  False),
PMMOpOption("mass_rating_update",                "mdb_trakt",             "Use Trakt Rating through MDbList",                                                                 False,  False,     False,        True,     False,  False),
PMMOpOption("mass_rating_update",                "omdb",                  "Use IMDbRating through OMDb",                                                                      False,  False,     False,        False,    True,   False),
PMMOpOption("mass_rating_update",                "remove",                "Remove Rating and Lock Field",                                                                     False,  False,     False,        False,    False,  False),
PMMOpOption("mass_rating_update",                "reset",                 "Remove Rating and Unlock Field",                                                                   False,  False,     False,        False,    False,  False),
PMMOpOption("mass_rating_update",                "tmdb",                  "Use TMDb Rating",                                                                                  False,  False,     False,        False,    False,  False),
PMMOpOption("mass_rating_update",                "trakt_user",            "Use Trakt User's Personal Rating",                                                                 True,   False,     False,        False,    False,  False),
PMMOpOption("mass_rating_update",                "unlock",                "Unlock Rating Field",                                                                              False,  False,     False,        False,    False,  False),
]

def extract(kind, lib_type, group, basics=False, mal=False, trakt=False, tautulli=False):
    ret_val = []
    SOURCE_LIST = []
    if kind == 'collections':
        SOURCE_LIST = DEFAULT_COLLECTIONS
    elif kind == 'overlays':
        SOURCE_LIST = DEFAULT_OVERLAYS
    else:
        SOURCE_LIST = DEFAULT_OPERATIONS

    for thing in SOURCE_LIST:
        if lib_type == "both" or (lib_type == "movie" and thing.movie) or (lib_type == "show" and thing.shows):
            if not group or thing.group == group:
                if not basics or (basics and thing.basic):
                    if not thing.myanimelist or (thing.myanimelist and mal):
                        if not thing.trakt or (thing.trakt and trakt):
                            if not thing.tautulli or (thing.tautulli and tautulli):
                                ret_val.append(thing)
    return ret_val

def get_options(kind, lib_type , group=None, basics=False, mal=True, trakt=True, tautulli=True):
    return extract(kind, lib_type, group=group, basics=basics, mal=mal, trakt=trakt, tautulli=tautulli)

def get_collection_types():
    return DEFAULT_COLLECTION_TYPES

def get_boolean_operations():
    return BOOLEAN_OPERATIONS