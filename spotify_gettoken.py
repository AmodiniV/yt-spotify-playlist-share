#in this file two methods to get spotify taken are implemented 
#Client Credentials Flow & Authorization Code Flow. Both provide different access controls.

import requests
import json
import base64
from urllib.parse import urlencode

client_id = ' ' #client ID from Spotify dashboard
client_secret = ' ' #client secret from Spotify dashboard
user_id = ' ' #spotify user ID

#get token for spotify using Client Credentials Flow method
client_creds = f"{client_id}:{client_secret}"
type (client_creds)

client_creds_b64 = base64.b64encode(client_creds.encode())
type(client_creds_b64)

token_url = "https://accounts.spotify.com/api/token"
method = "POST"
token_data = { "grant_type": "client_credentials" }
token_headers = { "Authorization":f"Basic {client_creds_b64.decode()}"
}

r = requests.post(token_url,data=token_data,headers = token_headers)
if r.status_code in range(200,299):
	request_data = r.json()
	token = request_data['access_token']
#print(r.json())
#get spotify token from Authorization Code Flow
endpoints = "https://accounts.spotify.com/authorize"
method = "GET"
token_data = urlencode({ "client_id": {client_id},"response_type":"code","redirect_uri":"http://mysite.com/callback/" })

lookup_url = f"{endpoints}?{token_data}"
r = requests.get(lookup_url)
