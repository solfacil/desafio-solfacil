
# How to develop with this structure

## Essentials 
### virtualenv
[virtualenv](https://virtualenv.pypa.io/en/latest/) are used to create a separate environment for each project, so our dependencies won't clash with another project.
After cloning, you need to create a new environment (after installing virtualenv) with:
`virtualenv venv`
Then activate that environment with  `./venv/Scripts/activate`

Install the requirements on venv with `pip install -r requirements.txt`


### Tox

First, please [install tox](https://tox.wiki/en/latest/installation.html)

If you are curious about, I recommend reading about it and what it can or cannot do.

Personally, I use it outside the virtualenv as it can be used for all your projects.


Before any commits, please run `tox` (without any specific environment) at project root, it's set to run our linters, formatters and tests, so anything wrong should be fixed before committing to repo.


Tox can also be used for building docker container and uploading to a registry* with latest tag + current version tag:

`tox -e build_docker`

This will also run linting, format and tests. Anything wrong would stop the building process.
*Please change `tox.ini` accordingly


## Optional, scriv

[scriv](https://pypi.org/project/scriv/) is the changelog management tool that I prefer to use.

I also use it system-wide for various projects, you can read more about it in the [docs](https://scriv.readthedocs.io/en/latest/index.html)



To start using it, we need a `changelog.d` at our project root, you can then use `scriv create` to create a new fragment

This should be edited with what has been done, like an added endpoint, fixed a bug, removed a test.

After writing the changes, save the file and use `scriv collect`, scriv will aggregate all fragments into `CHANGELOG.md` file with the current `__version__` variable from `src/app/definitions.py`, so for a new version it should be updated with changelog.


Scriv can also be used to trigger releases on GitHub, but this wouldn't be used here.

## Environment variables
Some options on the app can be set using environment variables, those options some aspects of the application like the default listening port, host or if email is enabled.

While running outside docker those can be easily changed editing `.env` file, on Docker the environments can be changed on `docker-compose.yaml` file or using `-e` flag

| Variable | Default Value| Behaviour |
|--|--|--|
| DB_DRIVER_NAME | sqlite | What engine is used to connect to database |
| DB_USERNAME | | username to connect to db, if any |
| DB_PASSWORD | | password to connect to db if any |
| DB_HOST | | the host ip of the database |
| DB_DATABASE| ./db.sqlite3 | database name, for sqlite it sets the path to db file |
| APP_PORT | 5000 | listening port for the API, same behaviour as `--port`|
| APP_IP | 0.0.0.0 | api host, same behaviour as `--host` |
| APP_TRUSTED_HOSTS | * | hosts that can use this API, use `*` to accept any, ommiting this flag also se as `*` |
| LOG_LEVEL | DEBUG | Log level of the app |
| LOG_ROTATION | 00:00 | When the file log is rotated |
| LOG_RETENTION | 30 days | For how long the files are kept before deletion |
| LOG_COMPRESSION |zip | In what format the logs are compressed |
| EMAIL_ENABLED | 0 | 0=disabled, 1=enabled |
| EMAIL_USERNAME | | The email user |
| EMAIL_PASSWORD | | The email password |
| EMAIL_SMTP_HOST | | Email SMTP host |
| EMAIL_SMTP_PORT | | SMTP port |
| GET_ADDRESS_FROM_VIACEP|0| 0=false, 1=true, so we dont break viacep with too many requests |

## Deploy

Our docker can be built and started by running `docker-compose up --build` from our project root.

This will build the image if needed and run based on our `docker-compose.yaml`


## Development

### Preferred method
Simply run `python ./src/app/main.py` or execute `main.py` on your editor (VSCode, PyCharm)
_I've found this method to be easier to intercept FastAPI logs_

### Usual method
Change directory from root to `./src/app` then use `uvicorn main:app`


