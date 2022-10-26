from . import query
from . import config
import itertools
from .service import APIService
from functools import lru_cache

@lru_cache(maxsize=100)
def get_service_specs(service = None):
    assert service is not None, "Incorect function call; the <service> parameter shouldn't be empty"
    data = { "service" : service }
    return query.query_api(params = [(config.Endpoints.DB_API_SERVICES, {}, data)])

def get_account_info(inputs):
    assert len(inputs) == 1, "Incorrect number of inputs provided for getting account information"

    data = inputs[0]
    return query.query_api(params = [(config.Endpoints.DB_API_ACCOUNTS, {}, data)])

def query_service(service, inputs):
    specs_result = get_service_specs(service = service)
    
    assert len(specs_result) == 1, f"Found >1 service specs for service {service}; this could be an API issue"
    service_specs = specs_result[0][0][0]

    svc = APIService(**service_specs)

    files_list = []
    data_list = []

    for crt_input in inputs:
        crt_files = {}
        crt_data = {}

        for pk, pv in svc.parameters.items():
            assert (not pv['required']) or (pk in crt_input), f"Parameter <{pk}> should be provided for service {service}"

            if pk in crt_input:
                if pv['type'] in config.FILE_POST_TYPES:
                    crt_files[pk] = crt_input[pk]
                else:
                    crt_data[pk] = crt_input[pk]
        
        files_list.append(crt_files)
        data_list.append(crt_data)

    return query.query_api(params = zip(itertools.repeat(config.Endpoints.PROTOCOL_SCHEMA + svc.endpoint), files_list, data_list))