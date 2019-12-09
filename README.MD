# Reddit Photo Scraper

I thought it would be a cool organize and display the best travel photos on reddit by the country or state they were taken in.


To do so I did the following
1. Using [Python Reddit API Wrapper(PRAW) library](https://praw.readthedocs.io/en/latest/), I scraped the highly-upvoted photos from the top travel photo subreddits. 

2. I searched the title for a country or state name to specify the locations

3. I saved the photos to a local instance of a mondoDB database

4. I used the  imgur api with the [imgurpython library](https://github.com/Imgur/imgurpython) to post the photos from a specific location into an album on imgur to make the photos easier to view and retreive

# SET UP
 
If you don't have git or python installed go to ... first to set them up(todo)


Clone Repo
```
git clone https://github.com/cshannon3/reddit_travel_pics_scraper
cd reddit_travel_pics_scraper
```

**REDDIT API**
1. Create a reddit account at [reddit.com](https://www.reddit.com/)
2. Log in then go to your[reddit apps page](https://www.reddit.com/prefs/apps/)
3. Scroll to the bottom and click and click the buttom that says
    "Are you a developer? Create an app"
    *if you've created one already the button says "create another app"
4. Fill in the name with anything you want, chose "script" for the type(options should be web app, installed app and script), write a quick description about what you plan to use this for, put "http://localhost:8080" for the redirect uri, leave the about url section blank.
<img align="center" src="https://github.com/cshannon3/reddit_travel_pics_scraper/blob/master/screenshots/createapplicationreddit.png" height="400">

5. Click create app and copy the client id, client secret, script name, username and password as labeled below. 
<img align="center" src="https://github.com/cshannon3/reddit_travel_pics_scraper/blob/master/screenshots/applicationcomponentsreddit.png" height="400">

6. Go to /required_info.py and replace the placeholders with your info
```
reddit_username= "REPLACE WITH USERNAME"
reddit_password=  "REPLACE_WITH_PASSWORD"
reddit_client_id = "REPLACE_WITH_CLIENTID"
reddit_client_secret =  "REPLACE_WITH_CLIENTSECRET"
reddit_user_agent =  "REPLACE_WITH_USERAGENT"
```
6. Install [Python Reddit API Wrapper(PRAW)](https://praw.readthedocs.io/en/latest/)
```
    pip install praw
```
You should be good to go for reddit, on to Imgur API


**Imgur API**



**Mongo DB**