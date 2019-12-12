
# Data-Collector-Tool

## Introduction
**What's the point?**
By collecting data from different sources, you can use it to create value in millions of ways. It allows you to recreate the data into a way that you like better or to analyze it and find interesting trends or insight in it. 

**Organizing/Presenting Data Better**
World map where you can click on country or state and see top travel pics from there


**Testing a Hypothesis**

**Gaining Insight**

## How To 'Talk' to the Web <br/>

Imagine that you live in a community with a few friends. You can talk freely amongst your friends but if you want to talk to anyone outside of your town you need to send a letter. Say you want to ask your friend from another town to send you the photos she took why you two were on vacation together. You first have to write a letter asking her for the photos you want her to send you. Its important to be clear enough that she knows what you are talking about. You then put the letter into an envelope, add her address and postage stamp then put it into the mail. Once she gets the letter she sends back another letter with the pictures that you requested. If you did this over the internet you would be using a GET function. On the internet, the letter is in the form of an "http request", the address in the form of an Internet Protocol(IP) address, and servers following the Transmission Communication Protocol(TCP)/IP rules are the postal service.  

There are a handful of 'letter types' you can send on the internet. The letter types differ in what is expected from the recieve of the letter. If the recipient is supposed to send you something like the photo example it is a GET letter.
The next type is called POST. This is like when you register your marriage, company, or car with the state. You tell them you want to get married and they can create a marriage certificate to put on record.
You can also send PUT and DELETE requests to change the records once they are made on their end.

Every time that you go to a site, you computer makes a request to that site to get all of the information to show you the site. In order for you to see ... sends all info.

**What are APIs**
If you want to interact with the site without having to go into the site, they can make application-programmer interfaces(APIs) which basically allows you to ask to see or do more specific tasks on the site. Say you run a financial firm and want the most up-to-date stock prices. The newspaper company shares that info in their daily newspaper but you don't want to buy the whole newspaper when all you need is a list of stock prices so to suit your needs they create a service that will allow for you to get just the list of stock prices. Many sites have these sorts of APIs, in this example I use reddit, imgur and firebase. To use reddit as an example, without specific api requests, anytime I send a letter to Reddit's address, they automatically send me all of the info required to recreate reddit's website on my browser. If I wanted to just get the post data, as I do in my examples below, all of the information on how to format the data in the browser is irrelavent. I'd have to make code to find and format the relavent data, which is not very fun(more below on that). Reddit's API provides services like the stock price list such as getting a list of posts from a specific subreddit. 

These APIs are great but just like how you had to be explicit with your friend about what pictures you wanted her to send you, you have to be explicit with the APIs in how you ask for specific services in order for them to provide the services you wanted. The reddit library is like a friend who knows exactly what to say to the reddit api to get the data you want. In this case you can tell him what data you want and he will transcribe the letter in a way that the reddit api understands and send it for you then give you the response once he gets it. 

**What if there is an API but you have no friend to transcribe your letters?**
Now you'll have to make your own letters(http requests) to send to these sites. 

**What if there isn't an API?**
You can still get data from sites but now you can't asking for specific information, you'll get all of the info to recreate the site and have to find a way to just get the parts you care about from it. This would be just like if you got the entire paper but just pulled out the stock prices and threw away the rest. The first time you do this you will have to search through the newspaper to find the business section but after that, as long as they don't change it, you can jump immediately to they right section. Beautify Soup is a tool that makes it easier to jump between page and sections as well as finding the specific sections that you care about. This method isn't ideal but since most sites don't have APIs its the only method to get data from much of the web.




<img align="center" src="https://github.com/cshannon3/reddit_travel_pics_scraper/blob/master/screenshots/explanations/rough-draft.png" height="300">






Data Source Options<br/>
 - reddit 
<br/>

Data Storage Options<br/>
 - Firebase
 - MongoDB
 - Imgur
 - Json
 - csv 


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

    [Python Reddit API Wrapper(praw)](https://praw.readthedocs.io/en/latest/)
    [Python Imgur API Library(imgurpython)](https://github.com/Imgur/imgurpython)
    [Mongo Python Driver(pymongo)](https://github.com/mongodb/mongo-python-driver)

To install required packages you can run either:
```
pip install -r requirements.txt
```
or 
```
pip install praw imgurpython pymongo pyrebase
```
**REDDIT API**<br/>
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

6. Go to /required_info.py and replace the placeholders with your info<br/>

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
1. Create an account at [Imgur.com](https://imgur.com/)
2. Once logged in go to [here](https://api.imgur.com/oauth2/addclient)(should look like below) to create an app in order to get the necessary credentials. Fill in info, chose OAuth2 authorization without a callback url. Your form should end up looking similar to below
<img align="center" src="https://github.com/cshannon3/reddit_travel_pics_scraper/blob/master/screenshots/imgur_setup/imgur2.png" height="300">
3. Click submit, copy down the client ID and client Secret from the screen the pops up after you submit(shown below)
<img align="center" src="https://github.com/cshannon3/reddit_travel_pics_scraper/blob/master/screenshots/imgur_setup/imgur3.png" height="300">
4. Go to /required_info.py and replace the placeholders with your info<br/>

```
imgur_account =  "REPLACE_WITH_IMGUR_ACCNT" 
client_id_imgur="REPLACE_WITH_CLIENT_ID" 
client_secret_imgur="REPLACE_WITH_CLIENT_SECRET" 

```
it should look similar to this:
```
imgur_account =  "webscraperaccnt" 
client_id_imgur="8y3940672846c44" 
client_secret_imgur="98c0945k23dgd192834729572d8se5434200c20"
```

**Mongo DB**<br/>
Using [Mongo Python Driver(pymongo)](https://github.com/mongodb/mongo-python-driver)
1. Follow [this installation guide](https://docs.mongodb.com/manual/installation/#mongodb-community-edition-installation-tutorials) on MongoDB's site to install the MongDB Community Edition Software
2. Follow [this startup guide](https://docs.mongodb.com/guides/server/install/)


**FIREBASE**

Using [Pyrebase](https://github.com/thisbejim/Pyrebase)


# Example Uses


**Reddit Travel Photos**
```


```

**Reddit Travel Advice**
```


```


I think this will end up being a multipurpose web-scrapper tool that aggregates a bunch of my previous projects and acts as a guide to getting started in this area. You'd basically just have to specify the source, relavent source info and storage method and this program will do the rest.
