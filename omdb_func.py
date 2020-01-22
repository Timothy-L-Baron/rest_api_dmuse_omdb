#omdb function
#https://www.omdbapi.com/
#omdbkey = 31b127b6
#omdb_baseurl = http://www.omdbapi.com/

import requests
import json
import string

#function for title search
def fetch_requests_title_omdb(word):
    parameters = {'t' : word, 'r' : 'json', 'apikey' : '31b127b6'}
    request = requests.get('http://www.omdbapi.com/', params = parameters)
    #print(request)
    format_request = json.loads(request.text) #returns dictionary
    #print(format_request) #this print out the dictionary
    #choices: Title, Rated, Year, Released, Runtime, Genre, Director, Writer, Actors, Plot,
    #Language, Country, Awards, Ratings
    while True:
        try:
            title_info = format_request['Title']#[random.randint(1,len(format_request)-1)]
            actor_info = format_request['Actors']
            year_info = format_request['Year']
            plot_info = format_request['Plot']
            break
        except:
            print("\nYour word returned no movie results.\n")
            quit()
    print('\nThe related movie title is: "{}" \n\nStarring: {} \n\nFrom the Year: {}.\n'.format(title_info, actor_info, year_info))
    print('Plot: {}'.format(plot_info))
    #year_info is a string
    return year_info



#function for year search
def fetch_requests_year_omdb(word, year):
    parameters = {'t' : word, 'y' : year, 'r' : 'json', 'apikey' : '31b127b6'}
    request = requests.get('http://www.omdbapi.com/', params = parameters)
    format_request = json.loads(request.text) #returns dictionary
    #print(format_request) #this print out the dictionary
    if len(format_request) == 0:
        print("Your movie year returned no extra movie results.\n")
        quit()
    #choices: Title, Rated, Year, Released, Runtime, Genre, Director, Writer, Actors, Plot,
    #Language, Country, Awards, Ratings
    while True:
        try:
            title_info = format_request['Title']
            actor_info = format_request['Actors']
            year_info = format_request['Year']
            plot_info = format_request['Plot']
            #print(year_info)
            break
        except:
            print("Your movie year returned no extra movie results.\n")
            quit()
    print('\nAnother movie from ' + year_info + ' is: "{}" \n\nStarring: {}.\n'.format(title_info, actor_info))
    print('Plot: {}\n'.format(plot_info))
    #return single_info
    #print(year_info)
    #return year_info
