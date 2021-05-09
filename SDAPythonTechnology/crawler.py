import requests

r = requests.get('http://worldtimeapi.org/api/timezone/Europe')

list_time_zones = r.json()

print("List of time zones> ", list_time_zones)

index = list_time_zones.index('Europe/Tallinn')

if 'Europe/Tallinn' in list_time_zones:
    print("Yes, it is there! Index is ", index)

