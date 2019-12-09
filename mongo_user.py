from pymongo import MongoClient
try:
    import secret as req_info
except ImportError:
    import require_info as req_info


class MongoUser:
    def __init__(self):
        if(req_info.needToAddInfo(useMongoDB=True)):
            print("Need to update required_info.py with correct credentials before running, see README for more info")
        self.client = MongoClient()
        self.db = client[req_info.mongoDatabaseName]
        self.currentCollection=""
        super().__init__()


    def update(self, collection, idmap, datamap):
        self.db[collection].update(idmap, datamap, upsert=True)


