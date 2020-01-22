#create the datamuse retrieval function
#https://www.datamuse.com/api/
#datamuse_baseurl = http://api.datamuse.com/words

import requests
import json
import random

def fetch_requests_datamuse(word):
    #rel_rhy = rhyming words
    #trg = trigger words like cow -> milking
    #ml = means like, sl = sounds like, sp = spelled like,
    #rel_(possible:cns[consonant match], rhy[rhymes], ant[antonyms], syn[synonyms]
    #jja[popular nouns it modifies], spc[kind of], bga[freq followers], bgb[freq predecessors]
    #nry[approx rhymes], hom[homophones],cns[consonant match])
    #there are also metadata tags (see website) currently blocked in parameters mdd
    #topics returns topics and can take up to five words
    parameters = { 'topics' : word, """'rel_rhy' : word,""" """'ml' : word,""" """'mdd' : word,""" 'max' : '100' }
    request = requests.get('http://api.datamuse.com/words', params = parameters)
    format_request = json.loads(request.text) #returns list of dictionaries
    #print(format_request)
    return format_request

def get_score_datamuse(format_request):
    length = len(format_request)
    print('\nYour word returned {} possible answer(s).\n'.format(length))
    #return a random word generated from the answers returned
    if length > 1:
        while True:
            try:
                single_info = format_request[random.randint(1,len(format_request)-1)]['word']
                single_info2 = format_request[random.randint(1,len(format_request)-1)]['score']
                break
            except:
                print("Your word returned no results.\n")
                quit()
    if length == 1:
        single_info = format_request[0]['word']
        single_info2 = format_request[0]['score']
    if length == 0:
        print("Your word returned no results.\n")
        quit()
    print('The related word is: {}.\n\nThe related score is: {}.'.format(single_info, single_info2))
    return single_info
