# Design a REST API program that takes data from three different websites and combines and/or compares data

#other sources - require key:
#https://tastedive.com/read/api
#https://tastedive-api-documentation.readthedocs.io/en/latest/endpoints.html

import requests
import json
import dmuse_func
import omdb_func

root_word = input('\nPlease type in a word:\n\n' )

#print(root_word)

start_word = dmuse_func.fetch_requests_datamuse(root_word)

#print(start_word)

return_word = dmuse_func.get_score_datamuse(start_word)

#print('\n')

#print(return_word)

get_year = omdb_func.fetch_requests_title_omdb(return_word)

#print(get_year)

#Put year and return title of movie back into OMDB for other movies from that year

omdb_func.fetch_requests_year_omdb(return_word, get_year)
