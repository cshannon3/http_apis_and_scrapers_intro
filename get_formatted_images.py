import sys
import pymongo
from pymongo import MongoClient


def main():
    client = MongoClient()
    db = client.redditdb3
    submissions = db.submissions
    #comments = db.comments
    locs = []
    location = sys.argv[1].split(" ")

    print(location)
    for s in submissions.find({}):
        isin = 0
        loc = []
        for key, value in s.items():
            if key == 'text':
                for f in range(0, len(location)):
                    if location[f] in value and isin == 0:
                        loc.append(value)
                        isin = 1
                        f = len(location)
                        print(value)
            if key == 'url' and isin == 1:
                isin = 0
                print(value)
                loc.append(value)
                locs.append(loc)
    print(locs)
if __name__ == '__main__':
  main()



  
# import sys
# import pymongo
# from pymongo import MongoClient


# def main():
#     client = MongoClient()
#     db = client.redditdb3
#     submissions = db.submissions
#     #comments = db.comments

#     location = sys.argv[1]
#     print(location)
#     for s in submissions.find({}):
#         isin = 0
#         for key, value in s.items():
#             if key == 'text' and location in value:
#                 isin = 1
#                 print(value)
#             if key == 'url' and isin == 1:
#                 isin = 0
#                 print(value)

# if __name__ == '__main__':
#   main()