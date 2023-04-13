import spotipy
from spotipy.oauth2 import SpotifyPKCE

client_id = """INPUT CLIENT ID"""
redirect_uri="""INPUT REDIRECT URI"""
scope = "user-library-read playlist-modify-public playlist-modify-private"


#  Authorisation code flow with PKCE   
auth_manager = SpotifyPKCE(client_id = client_id, 
                            redirect_uri = redirect_uri, 
                            scope = scope)

sp = spotipy.Spotify(auth_manager = auth_manager) # Spotify Object
dw_id = "" # Discovery Weekly playlist ID
user_id = sp.me()["id"] # Current user ID
saved_playlists= []
track_uri = []
dws_id = "" # Discovery Weekly Saved playlist ID

# Get all the current user's saved playlist names 
for item in sp.current_user_playlists()["items"]:
    saved_playlists.append(item["name"])

def add_to_weekly_saved():
    global dws_id
    if "Discovery Weekly Saved" not in saved_playlists:
        new_pl = sp.user_playlist_create(user= user_id,name= "Discovery Weekly Saved", 
                                         description= "Discovery Weekly saved using python👨🏾‍💻")
        dws_id = new_pl["id"]
    else:
        for item in sp.current_user_playlists()["items"]:
            if item["name"] == "Discovery Weekly Saved":
                dws_id = item["id"]
                break
                
if "Discovery Weekly" in saved_playlists:
    for item in sp.current_user_playlists()["items"]:
        if item["name"] == "Discovery Weekly":
            dw_id = item["id"]
            add_to_weekly_saved()
            # Discovery Weekly track URIs
            for item in sp.playlist_items(dw_id)["items"]:
                track_uri.append(item["track"]["uri"])
            # Add Discovery Weekly tracks to Discovery Weekly Saved playlist
            sp.playlist_add_items(playlist_id= dws_id, items=track_uri, position= 0)
            print("SUCCESS")
            break   
else:
    print("DISCOVERY WEEKLY PLAYLIST NOT AVAILABLE")
    