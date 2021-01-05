# yt-spotify-playlist-share
This app converts your favourite youtube playlist into a spotify playlist. No need to search for songs on spotify or add songs to a playlist manually! 
A seamless transfer of your favourite tracks from one platform to another:)

Used YoutubeData API and spotify for developers in python.
On YoutubeData API need to create OAuth client ID as the app needs permission to fetch information from your personal youtube account.

1. Final.py - > main file where playlist from youtube is fetched and then a new playlist is created on your spotify account, the songs are searched and added in the playlist on Spotify. 
Spotify functions use token and id from secret file & youtube function use client_Secret.json file from Credentials.

2. Spotify_gettoken.py -->This is an additional file where spotify authorization tokens are generated through two methods.
For more details refer to: https://developer.spotify.com/documentation/general/guides/authorization-guide/

3. Search_youtube.py ---> This is an additional file where search feature of youtube data api is being used.

Youtube Data API : https://developers.google.com/youtube/v3
Spotify for developers: https://developer.spotify.com/documentation/web-api/
