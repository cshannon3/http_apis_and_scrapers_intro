


from datetime import datetime
from imgurpython import ImgurClient
try:
    import secret as req_info
except ImportError:
    import require_info as req_info

def get_input(string):
	''' Get input from console regardless of python 2 or 3 '''
	return input(string)

def get_config():
	''' Create a config parser for reading INI files '''
	try:
		import ConfigParser
		return ConfigParser.ConfigParser()
	except:
		import configparser
		return configparser.ConfigParser()

class ImgurBot:
    def __init__(self):
        self.client=None

        self.authorized = False
        if(req_info.needToAddInfo(useImgur=True)):
            print("Need to update required_info.py with correct credentials before running, see README for more info")
        super().__init__()
        
    def authenticate(self):
        self.client = ImgurClient(req_info.client_id_imgur, req_info.client_secret_imgur)
        authorization_url = self.client.get_auth_url('pin')
        print("Go to the following URL: {0}".format(authorization_url))
        # Read in the pin, handle Python 2 or 3 here.
        pin = get_input("Enter pin code: ")
        # ... redirect user to `authorization_url`, obtain pin (or code or token) ...
        credentials = self.client.authorize(pin, 'pin')
        self.client.set_user_auth(credentials['access_token'], credentials['refresh_token'])
        print("Authentication successful! Here are the details:")
        print("   Access token:  {0}".format(credentials['access_token']))
        print("   Refresh token: {0}".format(credentials['refresh_token']))
        self.authorized=True
        
       
    
    def getalbums(self):
        albums = self.client.get_account_albums(req_info.imgur_account, page=0)
        print("Done")
        print(albums)
    

    def upload_to_album(self, albumId, title, description, image_url):
        config = {
		    'album':albumId,
		    'name': title,
		    'title': title,
		    'description': description
	    }
        self.client.upload_from_url(image_url, config=config, anon=False)
        pass
    




    
# from auth import authenticate
# from datetime import datetime
# try:
#     import secret as req_info
# except ImportError:
#     import require_info as req_info

# def getalbums(client):
#     albums = client.get_account_albums(req_info.imgur_account, page=0)
#     print("Done")
#     print(albums)
    
 
# if __name__ == "__main__":
#     if(req_info.needToAddInfo(useImgur=True)):
#         print("Need to update required_info.py with correct credentials before running, see README for more info")
#     else:
#         client = authenticate()
#         getalbums(client)
    