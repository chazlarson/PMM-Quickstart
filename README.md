# PMM-quickstart
quickstart script for building a basic config for PMM

## if you use [`direnv`](https://github.com/direnv/direnv):
1. clone the repo
1. cd into the repo dir
1. run `direnv allow` as the prompt will tell you to
1. direnv will build the vitrual env and keep requirements up to date

## if you don't use [`direnv`](https://github.com/direnv/direnv):
1. install direnv
2. go to the previous section
   
ok no

1. clone the repo
1. cd into the repo dir
1. create a python3 venv
1. `python -m pip install -r requirements.txt`

## after that, in either case
1. run with `python config-gen.py`
1. Follow the prompts.


If you're doing a lot of this, copy `config.json.default` to `config.json` and fill in the values.  The script will read those and then you can just hit return to accept the defaults.
