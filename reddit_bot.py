import praw
try:
    import secret as req_info
except ImportError:
    import require_info as req_info

class RedditBot:
    def __init__(self):
        self.client=None
        self.authorized = False
        if(req_info.needToAddInfo(useRedditAPI=True)):
            print("Need to update required_info.py with correct credentials before running, see README for more info")
        super().__init__()
    def authenticate(self):
        self.client = praw.Reddit(username= req_info.reddit_username,
                password=  req_info.reddit_password,
                client_id = req_info.reddit_client_id,
                client_secret =  req_info.reddit_client_secret,
                user_agent =  req_info.reddit_user_agent)
        self.authorized=True

    def get_posts_from_subreddit(self, subreddit, count=50, toJson=False, rankType="top", minScore=0, imagesOnly=False):
        submissions = []
        if rankType=="top":
            submissions=self.client.subreddit(subreddit).top(limit=count)
        elif rankType=="hot":
            submissions=self.client.subreddit(subreddit).hot(limit=count)
        else:
            submissions=self.client.subreddit(subreddit).submissions(limit=count)
        if not toJson:
            return submissions
        jsonSubmissions=[]
        for submission in submissions:
            if submission.score>minScore and ((not imagesOnly) or ".jpg" in submission.url ):
                jsonSubmissions.append({
                    'text': submission.title,
                    'author': submission.author.name,
                    'submission_id': submission.id,
                    'subreddit': submission.subreddit.display_name,
                    'score': submission.score,
                    'created_at' : submission.created_utc,
                    'url': submission.url,
                })
        return jsonSubmissions
    
    

#     pass
# countries = "Canada Afghanistan Albania Algeria Andorra Angola Anguilla Antarctica Antigua Barbuda Argentina Armenia Aruba Australia Austria Azerbaijan Bahamas Bahrain Bangladesh Barbados Belarus Belgium Belize Benin Bermuda Bhutan Bolivia Bosnia Botswana Bouvet Island Brazil Brunei Bulgaria Burkina Faso Burundi Cambodia Cameroon Cayman  Chad Chile China Cocos Colombia Comoros Congo Costa Croatia Cuba Cyprus Czech Denmark Djibouti Dominica Dominican Timor Ecudaor Egypt El Salvador Eritrea Estonia Ethiopia Falkland Faroe Islands Fiji Finland France Gabon Gambia Georgia Germany Ghana Gibraltar Greece Greenland Grenada Guadeloupe Guam Guatemala Guinea Guyana Haiti Honduras Hong Kong Hungary Iceland India Indonesia Iran Iraq Ireland Israel Italy Ivory Jamaica Japan Jordan Kazakhstan Kenya Kiribati Korea Kuwait Kyrgyzstan Latvia Lebanon Lesotho Liberia Libya Liechtenstein Lithuania Luxembourg Macau Macedonia Madagascar Malawi Malaysia Maldives Mali Malta Marshall Martinique Mauritania Mauritius Mayotte Mexico Micronesia Moldova Monaco Mongolia Montserrat Morocco Mozambique Myanmar Namibia Nauru Nepal Netherlands Zealand Nicaragua Niger Nigeria Niue Norfork Norway Oman Pakistan Palau Panama Paraguay Peru Philippines Pitcairn Poland Portugal Puerto Qatar Romania Russia Rwanda Kitts Nevis Lucia Grenadines Samoa Marino Sao Tome Principe Saudi Arabia Senegal Seychelles Sierra Leone Singapore Slovakia Slovenia Solomon Somalia Spain Sri Lanka Helena Pierre Miquelon Sudan Suriname Svalbarn Swaziland Sweden Switzerland Syria Taiwan Tajikistan Tanzania Thailand Togo Tokelau Tonga Trinidad Tunisia Turkey Turkmenistan Tuvalu Uganda Ukraine Emirates UK Uruguay Uzbekistan Vanuatu Vatican Venezuela Vietnam Yemen Yugoslavia Zaire Zambia Zimbabwe"
# def bot_login():
#     r = praw.Reddit(username= req_info.reddit_username,
#             password=  req_info.reddit_password,
#             client_id = req_info.reddit_client_id,
#             client_secret =  req_info.reddit_client_secret,
#             user_agent =  req_info.reddit_user_agent)
#     return r

# def run_bot(r):
#     for submission in r.subreddit("travel").submissions(limit=50):
#         text = submission.body
#         words = text.split(" ")
#         for word in words:
#             if word in countries and len(word) > 4:
#                 print(word)

# if(req_info.needToAddInfo(useRedditAPI=True)):
#     print("Need to update required_info.py with correct credentials before running, see README for more info")
# else:
#     r = bot_login()
#     run_bot(r)

           # for submission in self.client.subreddit(subreddit).submissions(limit=50):
        #     text = submission.body
        #     words = text.split(" ")
        #     for word in words:
        #         if word in countries and len(word) > 4:
        #             print(word)