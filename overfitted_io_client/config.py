import os

MAX_RETRIES = 5
NUM_WORKERS = 5

API_KEY_ENV_VAR_NAME = 'OVERFITTED_IO_API_KEY'
API_KEY_PARAM_NAME = 'api_key'
FILE_POST_TYPES = ['image']

def get_api_key():
    assert API_KEY_ENV_VAR_NAME in os.environ, f"[OVERFITTED-IO] Missing API key in environment variable `{API_KEY_ENV_VAR_NAME}`"
    return os.environ[API_KEY_ENV_VAR_NAME]

class Endpoints:
    PROTOCOL_SCHEMA = "https://"
    DB_API_SERVICES = 'https://db-api.api.overfitted.io/view-service-specs'
    DB_API_ACCOUNTS = 'https://db-api.api.overfitted.io/view-account-info'


