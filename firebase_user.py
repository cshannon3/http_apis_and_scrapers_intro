import pyrebase
try:
    import secret as req_info
except ImportError:
    import require_info as req_info


#https://github.com/thisbejim/Pyrebase
#https://hackbrightacademy.com/blog/heating-firebase-tutorial-integrate-firebase-app/
#db.generate_key()
class FirebaseClient:
    def __init__(self):
        self.client=None
        self.authorized = False
        if(req_info.needToAddInfo(useFirebase=True)):
            print("Need to update required_info.py with correct credentials before running, see README for more info")
       
        super().__init__()
        
    def authenticate(self):
        config = {
            "apiKey": req_info.firebase_api_key,
            "authDomain": req_info.firebase_auth_domain,
            "databaseURL": req_info.firebase_database_url,
            "storageBucket": req_info.firebase_storage_bucket
            }
        self.client=pyrebase.initialize_app(config)
        self.authorized=True
    def getData(self, collectionName=""):
      

        pass
    
    def pushData(self, collectionName=""):
         #  data = {"name": "Mortimer 'Morty' Smith"}
        #db.child("users").child("Morty").set(data)
        pass

    def setData(self, collectionName=""):
         #   data = {"name": "Mortimer 'Morty' Smith"}
          #  db.child("users").child("Morty").set(data)
        pass
    
    def updateData(self, collectionName=""):
         # db.child("users").child("Morty").update({"name": "Mortiest Morty"}) #  db.child("users").child("Morty").set(data)
        pass
    
    def removeData(self, collectionName=""):
            #db.child("users").child("Morty").remove()
        pass

    def storageChild(self):
        pass

    def storagePut(self):
        pass

    def storageDownload(self):
        pass

    def storageGetUrl(self):
        pass

# Queries return a PyreResponse object. Calling val() on these objects returns the query data.

# users = db.child("users").get()
# print(users.val()) # {"Morty": {"name": "Mortimer 'Morty' Smith"}, "Rick": {"name": "Rick Sanchez"}}
# key
# Calling key() returns the key for the query data.

# user = db.child("users").get()
# print(user.key()) # users
# each
# Returns a list of objects on each of which you can call val() and key().

# all_users = db.child("users").get()
# for user in all_users.each():
#     print(user.key()) # Morty
#     print(user.val()) # {name": "Mortimer 'Morty' Smith"}
# get
# To return data from a path simply call the get() method.

# all_users = db.child("users").get()
# shallow
# To return just the keys at a particular path use the shallow() method.

# all_user_ids = db.child("users").shallow().get()


# streaming
# You can listen to live changes to your data with the stream() method.

# def stream_handler(message):
#     print(message["event"]) # put
#     print(message["path"]) # /-K7yGTTEp7O549EzTYtI
#     print(message["data"]) # {'title': 'Pyrebase', "body": "etc..."}

# my_stream = db.child("posts").stream(stream_handler)
# You should at least handle put and patch events. Refer to "Streaming from the REST API" for details.

# You can also add a stream_id to help you identify a stream if you have multiple running:

# my_stream = db.child("posts").stream(stream_handler, stream_id="new_posts")
# close the stream
# my_stream.close()
# Complex Queries
# Queries can be built by chaining multiple query parameters together.

# users_by_name = db.child("users").order_by_child("name").limit_to_first(3).get()
# This query will return the first three users ordered by name.

# order_by_child
# We begin any complex query with order_by_child().

# users_by_name = db.child("users").order_by_child("name").get()
# This query will return users ordered by name.

# equal_to
# Return data with a specific value.

# users_by_score = db.child("users").order_by_child("score").equal_to(10).get()
# This query will return users with a score of 10.

# start_at and end_at
# Specify a range in your data.

# users_by_score = db.child("users").order_by_child("score").start_at(3).end_at(10).get()
# This query returns users ordered by score and with a score between 3 and 10.

# limit_to_first and limit_to_last
# Limits data returned.

# users_by_score = db.child("users").order_by_child("score").limit_to_first(5).get()
# This query returns the first five users ordered by score.

# order_by_key
# When using order_by_key() to sort your data, data is returned in ascending order by key.

# users_by_key = db.child("users").order_by_key().get()
# order_by_value
# When using order_by_value(), children are ordered by their value.

# users_by_value = db.child("users").order_by_value().get()