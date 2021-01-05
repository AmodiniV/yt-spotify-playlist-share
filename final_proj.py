import json
import requests
from secret import id,token
from urllib.parse import urlencode
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

def create_spotify_playlist():
    request_body = json.dumps({
        "name":"Youtube liked videos!",
        "public": True
    })

    query = "https://api.spotify.com/v1/users/{}/playlists".format(id)
    response = requests.post(
        query,
        data = request_body,
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer {}".format(token)
            }
    )
    if response.status_code in range(200,299):
        print ("Your spotify playlist is created \n")
        output = response.json()
        return(output["id"])
    else:
        print ("Playlist not created\n")
        return 0
    
#search track on spotify
def search_track(title_track):
    endpoints = "https://api.spotify.com/v1/search"
    method = "GET"
    token_data = urlencode({ "q":{title_track},"type":"track","limit":"1" })
    token_headers = {"Authorization":f"Bearer {token}" }

    lookup_url = f"{endpoints}?{token_data}"
    r = requests.get(lookup_url,headers = token_headers)
    response = r.json()
    res = response.get("tracks",[])
    items_list = res.get("items",[])
    if (items_list):
        track_id = items_list[0]['uri']
        add_track_to_playlist(playlist_id,track_id)
    else:
        print ('Track {} not found on spotify'.format(title_track))

#add track to spotify playlist
def add_track_to_playlist(playlist_id,track_id):
    query = "https://api.spotify.com/v1/playlists/{0}/tracks?uris={1}".format(playlist_id,track_id)
    response = requests.post(
            query,
            headers = {
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(token)
                }
    )
    print (response.json())

#fetch yt playlist
def fetch_yt_playlist():
    scopes = ["https://www.googleapis.com/auth/youtube.readonly"]
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "#client_Secret_json_file"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    #here youtube is the API client
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube.playlistItems().list(
        part="snippet,contentDetails",
        playlistId=" " #playlist_id from yt
    )
    response = request.execute()
    for item in response["items"]:
        track_title = item["snippet"]["title"].split("(")
        track_id = search_track(track_title[0]) 
       

playlist_id = create_spotify_playlist()
fetch_yt_playlist()