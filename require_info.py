
reddit_username= "REPLACE WITH USERNAME"
reddit_password=  "REPLACE_WITH_PASSWORD"
reddit_client_id = "REPLACE_WITH_CLIENTID"
reddit_client_secret =  "REPLACE_WITH_CLIENTSECRET"
reddit_user_agent =  "REPLACE_WITH_USERAGENT"


mongoDatabaseName = "REPLACE_WITH_DB_NAME" 

imgur_account =  "REPLACE_WITH_IMGUR_ACCNT" 
client_id_imgur="REPLACE_WITH_CLIENT_ID" 
client_secret_imgur="REPLACE_WITH_CLIENT_SECRET" 

def needToAddInfo(useImgur=False,useMongoDB=False, useRedditAPI=False ):
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
   