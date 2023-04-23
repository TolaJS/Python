# Saved Weekly Version 1
Python code for saving the Spotify 'Discovery Weekly' playlist in a new playlist called 'Discovery Weekly Saved'

## Installation
```bash
pip install spotipy
```
## Prerequisites
* Have a Spotify account
* Your Spotify Discovery Weekly playlist must be added to your profile. This can be done on any of the Spotify apps
* Create an app in the dashboard of the spotify for developers [website](https://developer.spotify.com/)
* Give the app a redirect uri e.g. "https://www.google.com" or "https://www.example.com"

## Code Additions
* Add the client-ID and redirect URI on your developer's dashboard to the code as a string
```python
client_id = """INPUT CLIENT ID"""
redirect_uri="""INPUT REDIRECT URI"""
scope = "user-library-read playlist-modify-public playlist-modify-private"
```
