import praw
import os
import re
import glob
import sys
import requests
import pprint
import secret as secret
import urllib.request as web
from bs4 import BeautifulSoup
import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.redditdb3
submissions = db.submissions
comments = db.comments

MIN_SCORE = 100
reddit = praw.Reddit(client_id=secret.client_id,
                     client_secret=secret.client_secret,
                     user_agent=secret.user_agent)


#dir_path = os.path.join(current_dir,subreddit_name)
 #   if not os.path.exists(dir_path):
  #      os.mkdir(dir_path)
    


def save_post(submission):
 
  try:
    sub = {
        'text': submission.title,
        'author': submission.author.name,
        'submission_id': submission.id,
        'subreddit': submission.subreddit.display_name,
        'score': submission.score,
        'created_at' : submission.created_utc,
        'url': submission.url,
      }
    submissions.update({'submission_id': submission.id}, sub, upsert=True)
  except:
    pass

reddit_list = ['travel', 'naturepics', 'EarthPorn', 'backpacking', 'Outdoors', 
'solotravel', 'hiking', 'remoteplaces', 'ruralporn', 'IWishIWasThere', 'CityPorn'
]

for sr in reddit_list:
    #posts = reddit.subreddit(sr).hot(limit=10000)
  posts = reddit.subreddit(sr).top(limit=10000)
  for post in posts:
    
    if '.jpg' in post.url:
      save_post(post)
      print(post.title)
    