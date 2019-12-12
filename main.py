import sys
import imgur_bot, reddit_bot, mongo_user
import json, csv
from datetime import datetime
import pandas as pd

class Manager:
    def __init__(self):
        self.imgurClient=None
        self.redditClient=None
        self.mongoClient=None
        self.firebaseClient=None
        self.source=None
        self.sink=None
        self.data=None

        super().__init__()

    def mongoDB_to_imgur(self):
        pass

    def reddit_to_mongoDB(self):
        pass

    def reddit_to_Json(self, filename, subreddit, count=10,rankType="top"):
        test = self.redditClient.get_posts_from_subreddit( subreddit, count=count, toJson=True, rankType=rankType)
        reddit_data = {
            'subreddit': subreddit,
            'count': count,
            'rankType':rankType,
            'timeOfRequest':str(datetime.now()),
            "posts":test
        }
        with open('data/{}.json'.format(filename), 'w') as json_file:
            json.dump(reddit_data, json_file)
        pass

    def reddit_to_csv(self, filename, subreddit, depth=1,count=10,rankType="top"):
        test = self.redditClient.get_posts_from_subreddit( subreddit, count=count, toCSV=True, rankType=rankType)
        df = pd.DataFrame(test)
        df.to_csv('data/{}.csv'.format(filename))

    
    def reddit_to_Firebase(self):
        pass

    
    def activate(self, imgur=False, reddit=False, mongoDB=False, firebaseDB=False):
        if imgur:
            if self.imgurClient==None:
                self.imgurClient= imgur_bot.ImgurBot()
            if not self.imgurClient.authorized:
                self.imgurClient.authenticate()
        if reddit:
            if self.redditClient==None:
                self.redditClient= reddit_bot.RedditBot()
            if not self.redditClient.authorized:
                self.redditClient.authenticate()
        if mongoDB:
            if self.mongoClient==None:
                self.mongoClient= mongo_user.MongoClient()
        if firebaseDB:
            if self.firebaseClient==None:
                self.firebaseClient= firebaseClient.FirebaseClient()

    pass

if __name__ == "__main__":
    manager = Manager()
    manager.activate(reddit=True)# activate apis and databases
    #test = manager.redditClient.get_posts_from_subreddit( "travel", count=10, toJson=True, rankType="top")
   # manager.reddit_to_Json("test", "travel",count=10)
    manager.reddit_to_csv("test", "dataisbeautiful",count=15)




    

