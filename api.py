from requests import get
from requests.exceptions import JSONDecodeError

def query(url, data=None):
    resp = get(url=url, data=data)
    try:
        return resp.json()
    except JSONDecodeError:
        print(resp.content)
        return []