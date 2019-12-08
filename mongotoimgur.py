
import sys
from auth import authenticate
from datetime import datetime
import praw
import os
import pymongo
from pymongo import MongoClient
# mongoclient = MongoClient()

# db = clientmongo.redditdb3
# locations = db.locations

def add_country_to_imgur(client): # country):
    mongoclient = MongoClient()
    db = mongoclient.redditdb3
    locations = db.locations
    


    for l in locations.find({"country": "Chile"}):
        name = ""
        title = ""
        description = ""
        image_url = ""
        good = False
        for key, value in l.items():
            if key == "text":
                name = value
                title = value
            elif key == "url":
                image_url = value
                good = True
        config = {
		    'album': "bEBdwKJ",#album,
		    'name':  name,
		    'title': title,
		    'description': '{0}'.format(datetime.now())
	    }
        
        if good:
            print("Uploading image... ")
            client.upload_from_url(image_url, config=config, anon=False)
            print("Done")
            print()



if __name__ == "__main__":
    client = authenticate()
    add_country_to_imgur(client)

