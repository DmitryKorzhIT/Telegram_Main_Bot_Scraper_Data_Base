import requests
from pprint import pprint
import json
import pandas as pd


# Config data.
URL_MOVIES = 'https://kinopoiskapiunofficial.tech/api/v2.2/films'
KEY = '3bb02829-73f8-4599-b841-657276210588'


# Variables.
rating_from_value = 4
rating_to_value = 5
year_from_value = 2000
year_to_value = 2001
page_value = 1
order_value = 'num_vote'


# Headers and params values for an API.
headers_value = {
    'X-API-KEY': '3bb02829-73f8-4599-b841-657276210588',
    'Content-Type': 'application/json'
}

params_value = {
    'ratingFrom': rating_from_value,
    'ratingTo': rating_to_value,
    'yearFrom': year_from_value,
    'yearTo': year_to_value,
    'page': page_value,
    'order': order_value
}


# Get data from the API.
r = requests.get(URL_MOVIES, headers=headers_value, params=params_value)
json_result = r.json()
json_result = json_result['items'][0]


# Convert data in to .csv format.
df = pd.DataFrame.from_dict(json_result, orient='index')
# df.to_csv ('./.data/result.csv', index = None)
df.to_csv('./.data/result.csv', mode='a', header=False)

pprint(json_result)






















