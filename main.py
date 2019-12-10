import sys
import imgur_bot
import reddit_bot
import mongo_user

class Manager:
    def __init__(self):
        self.imgurClient=None
        self.redditClient=None
        self.mongoClient=None
        self.firebaseClient=None
        super().__init__()

    def mongoDB_to_imgur(self):
        pass

    def reddit_to_mongoDB(self):
        pass

    def reddit_to_Json(self):
        pass
    
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
    manager.activate()# activate apis and databases


    

