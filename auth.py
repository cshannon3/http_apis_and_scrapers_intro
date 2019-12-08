from imgurpython import ImgurClient
from helpers import get_input, get_config
import secret as secret

def authenticate():
    client_id = secret.client_id_imgur
    client_secret = secret.client_secret_imgur
    client = ImgurClient(client_id, client_secret)
    authorization_url = client.get_auth_url('pin')
    print("Go to the following URL: {0}".format(authorization_url))
    # Read in the pin, handle Python 2 or 3 here.
    pin = get_input("Enter pin code: ")

	# ... redirect user to `authorization_url`, obtain pin (or code or token) ...
    credentials = client.authorize(pin, 'pin')
    client.set_user_auth(credentials['access_token'], credentials['refresh_token'])
    print("Authentication successful! Here are the details:")
    print("   Access token:  {0}".format(credentials['access_token']))
    print("   Refresh token: {0}".format(credentials['refresh_token']))
    
    return client

# If you want to run this as a standalone script, so be it!
if __name__ == "__main__":
	authenticate()