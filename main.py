
#get movie list from csv
#loop through each movie checking if they are on a streaming service
#add the films id to csv
#output films that match up
#initial call to check streaming services
#update call to check for changed titles
#if changed title exists in database then check that film for new availabilty

import urllib.request
import json
import csv

API_KEY = "RzBwqUTJkRIkR3hfzsW6i4J5NeTkOwg5KN0hUaaR"
MOVIE_FILE = "watchlist-mattjg154-2024-08-02-13-30-utc.csv"
OUTPUT_FILE = "moviesIDs.csv"

def getTitles():
    movies = []
    with open(MOVIE_FILE, newline='', encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            movies.append(row[1])
    return movies

def getTitleID(MOVIE_NAME):
    with urllib.request.urlopen("https://api.watchmode.com/v1/autocomplete-search/?apiKey="+API_KEY+"&search_value="+MOVIE_NAME+"&search_type=1") as url:
        data = json.loads(url.read().decode())
        TITLE_ID = str(data['results'][0]['id'])
    return TITLE_ID

def getSources(TITLE_ID):
    with urllib.request.urlopen("https://api.watchmode.com/v1/title/"+TITLE_ID+"/sources/?apiKey="+API_KEY) as url:
        data = json.loads(url.read().decode())
        SOURCES = data
        for source in SOURCES:
            if source['region'] == 'GB' and source['type'] == 'sub':
                print(source['name'])

def storeIDs(TITLES, IDs):
    with open(OUTPUT_FILE, 'w', newline='', encoding="utf8") as csvfile:
        fieldnames = ['TITLE', 'TITLE_ID']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(0, len(TITLES)):
            writer.writerow({'TITLE': TITLES[i], 'TITLE_ID': IDs[i]})
    

TITLES = ["A","b","c"]
IDs = ["1","2","3"]

for TITLE in TITLES:
    TITLE = TITLE.replace(' ', '%20')

storeIDs(TITLES,IDs)



