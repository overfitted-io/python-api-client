from typing import NamedTuple

class APIService(NamedTuple):
    service: str
    endpoint: str
    method: str
    parameters: dict


