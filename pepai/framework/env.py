"""
Database can be either an sqlite file or a postgress server
"""
import os
from pathlib import Path

from platformdirs import user_data_dir

PEPAI_ENV_KEYS = {  # dict of name then function to  convert str to correct type
    "FPL_TEAM_ID": int,
    "FPL_LOGIN": str,
    "FPL_PASSWORD": str,
    "FPL_LEAGUE_ID": int,
    "PEPAI_DB_FILE": str,
    "PEPAI_DB_URI": str,
    "PEPAI_DB_USER": str,
    "PEPAI_DB_PASSWORD": str,
    "DISCORD_WEBHOOK": str,
}

# Cross-platform data directory
if "PEPAI_HOME" in os.environ.keys():
    PEPAI_HOME = os.environ["PEPAI_HOME"]
else:
    PEPAI_HOME = Path(user_data_dir("pepai"))
os.makedirs(PEPAI_HOME, exist_ok=True)


def check_valid_key(func):
    """decorator to pre-check whether we are using a valid PEPAI key in env
    get/save/del functions"""

    def wrapper(key, *args, **kwargs):
        if key not in PEPAI_ENV_KEYS:
            raise KeyError(f"{key} is not a known PEPAI environment variable")
        return func(key, *args, **kwargs)

    return wrapper


@check_valid_key
def get_env(key, default=None):
    if key in os.environ.keys():
        return PEPAI_ENV_KEYS[key](os.environ[key])
    if os.path.exists(PEPAI_HOME / key):
        with open(PEPAI_HOME / key) as f:
            return PEPAI_ENV_KEYS[key](f.read().strip())
    return default


@check_valid_key
def save_env(key, value):
    with open(PEPAI_HOME / key, "w") as f:
        f.write(value)


@check_valid_key
def delete_env(key):
    if os.path.exists(PEPAI_HOME / key):
        os.remove(PEPAI_HOME / key)
    if key in os.environ.keys():
        os.unsetenv(key)
        os.environ.pop(key)
