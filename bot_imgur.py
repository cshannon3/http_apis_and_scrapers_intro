#from imgurpython import ImgurClient
from auth import authenticate
from datetime import datetime

def getalbums(client):
    albums = client.get_account_albums("travelpicsbot", page=0)
    print("Done")
    print(albums)
    
 
if __name__ == "__main__":
    client = authenticate()

    getalbums(client)
    

    

#image = upload_pic(client)
#client = ImgurClient(client_id, client_secret)
#imgurl = "https://i.redd.it/m3dpn3dqmdy01.jpg"
# Example request
#items = client.gallery()
#for item in items:
#   print(item.link)
#client.
# def upload_pic(client):

#     album = "5CNIbCw" # You can also enter an album ID here
#     image_url = "https://i.redditmedia.com/qE68JS8sMone_oDqFxAJEGauRuK7XhsSK9i8Z1mxZFc.jpg?w=962&s=4e9d5dbc6c1737e936c74031a06f3337"

# 	# Here's the metadata for the upload. All of these are optional, including
# 	# this config dict itself.
#     config = {
# 		'album': album,
# 		'name':  'Morocco',
# 		'title': 'Morocco',
# 		'description': 'Idk {0}'.format(datetime.now())
# 	}
#     print("Uploading image... ")
#     image = client.upload_from_url(image_url, config=config, anon=False)
#     print("Done")
#     print()
#     return image
