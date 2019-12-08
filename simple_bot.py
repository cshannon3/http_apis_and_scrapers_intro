import praw
import secret as secret

username = secret.username
pswd = secret.pswd
client_id = secret.client_id
client_secret = secret.client_secret
countries = "Canada Afghanistan Albania Algeria Andorra Angola Anguilla Antarctica Antigua Barbuda Argentina Armenia Aruba Australia Austria Azerbaijan Bahamas Bahrain Bangladesh Barbados Belarus Belgium Belize Benin Bermuda Bhutan Bolivia Bosnia Botswana Bouvet Island Brazil Brunei Bulgaria Burkina Faso Burundi Cambodia Cameroon Cayman  Chad Chile China Cocos Colombia Comoros Congo Costa Croatia Cuba Cyprus Czech Denmark Djibouti Dominica Dominican Timor Ecudaor Egypt El Salvador Eritrea Estonia Ethiopia Falkland Faroe Islands Fiji Finland France Gabon Gambia Georgia Germany Ghana Gibraltar Greece Greenland Grenada Guadeloupe Guam Guatemala Guinea Guyana Haiti Honduras Hong Kong Hungary Iceland India Indonesia Iran Iraq Ireland Israel Italy Ivory Jamaica Japan Jordan Kazakhstan Kenya Kiribati Korea Kuwait Kyrgyzstan Latvia Lebanon Lesotho Liberia Libya Liechtenstein Lithuania Luxembourg Macau Macedonia Madagascar Malawi Malaysia Maldives Mali Malta Marshall Martinique Mauritania Mauritius Mayotte Mexico Micronesia Moldova Monaco Mongolia Montserrat Morocco Mozambique Myanmar Namibia Nauru Nepal Netherlands Zealand Nicaragua Niger Nigeria Niue Norfork Norway Oman Pakistan Palau Panama Paraguay Peru Philippines Pitcairn Poland Portugal Puerto Qatar Romania Russia Rwanda Kitts Nevis Lucia Grenadines Samoa Marino Sao Tome Principe Saudi Arabia Senegal Seychelles Sierra Leone Singapore Slovakia Slovenia Solomon Somalia Spain Sri Lanka Helena Pierre Miquelon Sudan Suriname Svalbarn Swaziland Sweden Switzerland Syria Taiwan Tajikistan Tanzania Thailand Togo Tokelau Tonga Trinidad Tunisia Turkey Turkmenistan Tuvalu Uganda Ukraine Emirates UK Uruguay Uzbekistan Vanuatu Vatican Venezuela Vietnam Yemen Yugoslavia Zaire Zambia Zimbabwe"
def bot_login():
    r = praw.Reddit(username= username,
            password= pswd,
            client_id = client_id,
            client_secret = client_secret,
            user_agent = "travel pic linker v0.1")
    return r

def run_bot(r):
    for submission in r.subreddit("travel").submissions(limit=50):
        text = submission.body
        words = text.split(" ")
        for word in words:
            if word in countries and len(word) > 4:
                print(word)

r = bot_login()
run_bot(r)