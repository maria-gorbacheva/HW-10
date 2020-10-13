import requests
import json
from pprint import pprint

heroes_list = [
    'Hulk',
    'Thanos',
    'Captain America'
]


def find_smartest(heroes):
    rating = 0
    for hero in heroes:
        response = requests.get('https://superheroapi.com/api/2619421814940190/search/'+hero)
        data = response.json()
        pprint(data)
        intelligence = data['results'][0]['powerstats']['intelligence']
        if int(intelligence) > int(rating):
            rating = intelligence
            smartest = hero

    print(f'Самый умный герой с интеллектом {rating} - {smartest}')
    return hero


#find_smartest(heroes_list)
# a = requests.get('https://superheroapi.com/api/2619421814940190/search/Hulk')
# b = a.json()
pprint(requests.get('https://superheroapi.com/api/2619421814940190/search/Hulk').json())

