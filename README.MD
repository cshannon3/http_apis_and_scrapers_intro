
# Reddit Photo Scraper

I think this will end up being a multipurpose web-scrapper tool that aggregates a bunch of my previous projects and acts as a guide to getting started in this area. You'd basically just have to specify


Data Source Options
reddit 

Data Storage Options
Firebase
MongoDB
Imgur
Json
csv 


To do so I did the following
1. Using [Python Reddit API Wrapper(PRAW) library](https://praw.readthedocs.io/en/latest/), I scraped the highly-upvoted photos from the top travel photo subreddits. 

2. I searched the title for a country or state name to specify the locations

3. I saved the photos to a local instance of a mondoDB database

4. I used the  imgur api with the [imgurpython library](https://github.com/Imgur/imgurpython) to post the photos from a specific location into an album on imgur to make the photos easier to view and retreive

# SET UP
 
For instructions on installing Python and pip see ["The Hitchhiker's Guide to Python" Installation Guides](http://docs.python-guide.org/en/latest/starting/installation/)


Clone Repo
```
git clone https://github.com/cshannon3/reddit_travel_pics_scraper
cd reddit_travel_pics_scraper
```
The libraries I use are:
    -[Python Reddit API Wrapper(praw)](https://praw.readthedocs.io/en/latest/)
    -[Python Imgur API Library(imgurpython)](https://github.com/Imgur/imgurpython)
    -[Mongo Python Driver(pymongo)](https://github.com/mongodb/mongo-python-driver)

To install required packages you can run either:
```
pip install -r requirements.txt
```
or 
```
pip install praw imgurpython pymongo Pyrebase
```
**REDDIT API**
[Python Reddit API Wrapper(praw)](https://praw.readthedocs.io/en/latest/)
1. Create a reddit account at [reddit.com](https://www.reddit.com/)
2. Log in then go to your [reddit apps page](https://www.reddit.com/prefs/apps/)
3. Scroll to the bottom and click and click the buttom that says
    "Are you a developer? Create an app"
    *if you've created one already the button says "create another app"
4. Fill in the name with anything you want, chose "script" for the type(options should be web app, installed app and script), write a quick description about what you plan to use this for, put "http://localhost:8080" for the redirect uri, leave the about url section blank.
<img align="center" src="https://github.com/cshannon3/reddit_travel_pics_scraper/blob/master/screenshots/createapplicationreddit.png" height="300">

5. Click create app and copy the client id, client secret, script name, username and password as labeled below. 
<img align="center" src="https://github.com/cshannon3/reddit_travel_pics_scraper/blob/master/screenshots/applicationcomponentsreddit.png" height="300">

6. Go to /required_info.py and replace the placeholders with your info
```
reddit_username= "REPLACE WITH USERNAME"
reddit_password=  "REPLACE_WITH_PASSWORD"
reddit_client_id = "REPLACE_WITH_CLIENTID"
reddit_client_secret =  "REPLACE_WITH_CLIENTSECRET"
reddit_user_agent =  "REPLACE_WITH_USERAGENT"
```
it should look like this example from [praw's docs](https://praw.readthedocs.io/en/latest/getting_started/authentication.html#oauth) shown below:
```
reddit_username="fakebot3"
reddit_password="1guiwevlfo00esyy"
reddit_client_id="SI8pN3DSbt0zor"
reddit_client_secret="xaxkj7HNh8kwg8e5t4m6KvSrbTI"
reddit_user_agent="testscript by /u/fakebot3"

```



**Imgur API**



**Mongo DB**
Using [Mongo Python Driver(pymongo)](https://github.com/mongodb/mongo-python-driver)
1. Follow [this installation guide](https://docs.mongodb.com/manual/installation/#mongodb-community-edition-installation-tutorials) on MongoDB's site to install the MongDB Community Edition Software
2. Follow [this startup guide](https://docs.mongodb.com/guides/server/install/)


**FIREBASE**
Using [Pyrebase](https://github.com/thisbejim/Pyrebase)
