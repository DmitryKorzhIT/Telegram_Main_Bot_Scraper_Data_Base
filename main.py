import requests
from pprint import pprint
import json
import pandas as pd

from config import KEY
from additional_functions import json_to_csv


# Config data.
URL_MOVIES = 'https://kinopoiskapiunofficial.tech/api/v2.2/films'


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


# Get data from the API in .json format.
r = requests.get(URL_MOVIES, headers=headers_value, params=params_value)
json_result = r.json()


# Columns for pandas.DataFrame.
atributes = ['nameRu',
             'nameOriginal',
             'nameEn',

             'ratingKinopoisk',
             'ratingImdb',

             'kinopoiskId',
             'imdbId',

             'type',
             'year',

             'posterUrl',
             'posterUrlPreview',

             'countries',
             'genres']

movies_df = pd.DataFrame(columns=atributes)
json_result = r.json()


# Convert .json format to pandas.DataFrame with editing countries and genres attributes.
movies_df = json_to_csv()


# Save pd.DataFrame to .csv file.
movies_df.to_csv('./.data/data.csv', mode='w', index=False)



















