# rest_api_dmuse_omdb

Objectives:
1) become familiar with REST API requests - Datamuse and OMDB in this case
2) become familiar with manipulating/using resulting data
3) use some resulting data to search again and get more results
4) prepare basic documentation for the program
5) make sure there are error messages or quits so that the user does not get error messages

Currently this program:

1) takes imput from the user (up to 5 words - but haven't limited this with code yet - 'topic' key in OMDB is the limiter)
2) sends input to datamuse for 'related topic word(s)
3) it returns the related topic word(s) and runs it through OMDB to find a title with the topic word in it
4) it returns title, actor, and years to user
5) then it sends that year and the topic word into OMDB again to find another movie from the same year

Contributors:
Tim Baron
