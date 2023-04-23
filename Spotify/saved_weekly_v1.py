import spotipy
from spotipy.oauth2 import SpotifyPKCE

client_id = """INPUT CLIENT ID"""
redirect_uri="""INPUT REDIRECT URI"""
scope = "user-library-read playlist-modify-public playlist-modify-private"


# Authorisation code flow with PKCE   
auth_manager = SpotifyPKCE(
    client_id = client_id, 
    redirect_uri = redirect_uri, 
    scope = scope
    )

sp = spotipy.Spotify(auth_manager = auth_manager) # Spotify Object
dw_id = None # Discovery Weekly playlist ID
user_id = sp.me()["id"] # Current user's ID
saved_playlists = sp.current_user_playlists()["items"] # Get current user's saved playlists
track_uris = []
dws_id = None # Discovery Weekly Saved playlist ID

def add_to_weekly_saved():
    for item in sp.playlist_items(dw_id)["items"]:
        # Get track URIs
        track_uris.append(item["track"]["uri"])
        # Add Discovery Weekly tracks to Discovery Weekly Saved playlist
        sp.playlist_add_items(playlist_id= dws_id, items=track_uris, position= None)
        print("SUCCESS")

for item in saved_playlists:
    if item["name"] == "Discovery Weekly":
        dw_id = item["id"] 
    if item["name"] == "Discovery Weekly Saved":
        dws_id = item["id"]
    
if not dws_id:
    # Create new 'Discovery Weekly Saved' playlist
    new_pl = sp.user_playlist_create(
        user= user_id,
        name= "Discovery Weekly Saved", 
        description= "Discovery Weekly saved using python👨🏾‍💻"
        )
        dws_id = new_pl["id"]
if not dw_id:
    print("DISCOVERY WEEKLY PLAYLIST NOT AVAILABLE")
else:
    add_to_weekly_saved()