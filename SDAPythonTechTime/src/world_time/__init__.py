import requests

URL = 'http://worldtimeapi.org/api/ip/'


def get_time_by_ip(ip):
    resp = requests.get(URL + ip)

    result = resp.json()

    if result == {'msg': '503 Unavailable'}:
        return None

    return result.json()
