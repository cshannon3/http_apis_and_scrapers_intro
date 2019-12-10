
reddit_username= "REPLACE WITH USERNAME"
reddit_password=  "REPLACE_WITH_PASSWORD"
reddit_client_id = "REPLACE_WITH_CLIENTID"
reddit_client_secret =  "REPLACE_WITH_CLIENTSECRET"
reddit_user_agent =  "REPLACE_WITH_USERAGENT"


mongoDatabaseName = "REPLACE_WITH_DB_NAME" 

imgur_account =  "REPLACE_WITH_IMGUR_ACCNT" 
client_id_imgur="REPLACE_WITH_CLIENT_ID" 
client_secret_imgur="REPLACE_WITH_CLIENT_SECRET" 


firebase_storage_url = "REPLACE_WITH_STORAGE_URL" #https://your_storage.firebaseio.com
firebase_client_secret="REPLACE_WITH_CLIENT_SECRET"
firebase_user_email = "REPLACE_WITH_EMAIL"

firebase_api_key="REPLACE_WITH_API_KEY" 
firebase_auth_domain="REPLACE_WITH_AUTH_DOMAIN" 
firebase_database_url="REPLACE_WITH_DATABASE_URL" 
firebase_storage_bucket="REPLACE_WITH_STORAGE_BUCKET" 
            

def needToAddInfo(useImgur=False,useMongoDB=False, useRedditAPI=False, useFirebase=False):
    if(useImgur and not(imgur_account==  "REPLACE_WITH_IMGUR_ACCNT" )):
        return True
    if(useMongoDB and not( mongoDatabaseName == "REPLACE_WITH_DB_NAME")):
        return True
    if useRedditAPI and not(reddit_username== "REPLACE WITH USERNAME" or
    reddit_password== "REPLACE_WITH_PASSWORD" or
    reddit_client_id == "REPLACE_WITH_CLIENTID" or
    reddit_client_secret ==  "REPLACE_WITH_CLIENTSECRET" or
    reddit_user_agent ==  "REPLACE_WITH_USERAGENT"):
        return True
    return False
   