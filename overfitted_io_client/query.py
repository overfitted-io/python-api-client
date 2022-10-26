import requests
import json
from . import config

from concurrent.futures import ThreadPoolExecutor

pool = ThreadPoolExecutor(max_workers=config.NUM_WORKERS)



def query_api(params = []):
    return list(pool.map(query_one, params))


def query_one(params):
    endpoint = params[0]
    files = params[1]
    data = params[2]

    status = -1

    for i in range(1, config.MAX_RETRIES): 
        response = requests.post(endpoint, data = data, files=files)
        status = response.status_code
        result = response.text

        # if 200, return the response
        if status == 200:
            return json.loads(result), status
        else:
            print(f'[OVERFITTED-IO API] Got response with status {status}, message: {result}; retrying {i} / {config.MAX_RETRIES}')

    assert False, "[OVERFITTED-IO API] Failed to retrieve a valid response from the API" 
    return {}, status