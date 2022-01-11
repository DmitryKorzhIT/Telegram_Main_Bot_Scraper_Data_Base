# Convert .json format to pandas.DataFrame with editing countries and genres attributes.
def json_to_csv():

    from main import json_result, atributes, movies_df

    for movie in range(len(json_result['items'])):

        for atribute in atributes:
            movies_df.at[movie, atribute] = json_result['items'][movie][atribute]

        # Convert countries from dictionaries format to string format.
        countries_list = []
        for county_index in range(len(json_result['items'][movie]['countries'])):
            countries_list.append(json_result['items'][movie]['countries'][county_index]['country'])
        movies_df.at[movie, 'countries'] = countries_list

        # Convert genres from dictionaries format to string format.
        genres_list = []
        for genre_index in range(len(json_result['items'][movie]['genres'])):
            genres_list.append(json_result['items'][movie]['genres'][genre_index]['genre'])
        movies_df.at[movie, 'genres'] = genres_list

    return movies_df