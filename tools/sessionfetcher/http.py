import json
from urllib.request import urlopen


def fetch_response(uri):
    with urlopen(uri) as res:
        data = res.read()
        return json.loads(data)
