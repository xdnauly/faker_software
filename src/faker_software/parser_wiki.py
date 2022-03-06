import requests


r = requests.get('https://en.wikipedia.org/wiki/List_of_operating_systems', timeout=10)


print(r)

