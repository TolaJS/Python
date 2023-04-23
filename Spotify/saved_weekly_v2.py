"""
Credit: Katia Gilligan
        @katiagilligan888 (github)
"""

import spotipy
import time
from flask import Flask, request, url_for, redirect, session
from spotipy.oauth2 import SpotifyPKCE

# Client Authorisation code flow with PKCE
auth_manager = SpotifyPKCE(
    client_id = """INPUT CLIENT ID""", 
    redirect_uri = """INPUT REDIRECT URI""", 
    scope = 'user-library-read playlist-modify-public playlist-modify-private')

# Initialise Flask app
app = Flask(__name__)
# Set session cookie name
app.config['SESSION COOKIE NAME'] = 'Spotify Cookie'
# Set a random session cookie secret key
app.secret_key = """INPUT SECRET KEY"""
# Set the key for the token info in the session dictionary
TOKEN_INFO = 'token_info'

# Route for user authorisation 
@app.route('/')
def login():
    # Get authorisation URL from SpotifyPKCE auth manager
    auth_url = auth_manager.get_authorize_url()
    # Redirect to authorisation URL 
    return redirect(auth_url)

# Route to handle the redirect after authorisation
@app.route('/redirect')
def redirect_page():
    # Clear the session
    session.clear()
    # Get authorization code from redirect URL
    code = auth_manager.get_authorization_code(request.full_path)
    # Gets access token and saves to cache
    auth_manager.get_access_token(code)
    # Set session token info to cached token
    session[TOKEN_INFO] = auth_manager.get_cached_token()
    # Redirect to /SaveWeekly route
    return redirect(url_for('save_discovery_weekly', _external = True))

@app.route('/SaveWeekly')
def save_discovery_weekly():
    try:
        # Check if session token is valid
        check_token()
    except:
        # If token is not valid, redirect to authorisation page
        print('User not logged in')
        return redirect('/')
    
    # Spotify object authenticated with PKCE auth_manager
    sp= spotipy.Spotify(auth_manager= auth_manager)
    # Current user's playlists
    current_playlists = sp.current_user_playlists()['items']
    dw_id = None # Discovery Weekly playlist ID
    sw_id = None # Saved Weekly playlist ID
    
    # Find the Discover Weekly and Saved Weekly playlists
    for playlist in current_playlists:
        if(playlist['name'] == 'Discover Weekly'):
            dw_id = playlist['id']
        if(playlist['name'] == 'Saved Weekly3'):
            sw_id = playlist['id']
            
    # If the Discover Weekly playlist is not found, return error message
    if not dw_id:
        return 'Discover Weekly not found.'
    # If saved Saved Weekly playlist is not found, create it
    if not sw_id:
        new_pl = sp.user_playlist_create(
            user= sp.me()['id'],
            name= 'Saved Weekly',
            description= 'Discover Weekly saved using python👨🏾‍💻')
        sw_id = new_pl['id']
     
    # Get the tracks from the Discover Weekly playlist    
    discover_weekly_playlist = sp.playlist_items(dw_id)
    song_uris = []
    for song in discover_weekly_playlist['items']:
        # Get track URIs
        song_uris.append(song['track']['uri'])
        
    # Add tracks to Saved Weekly
    sp.playlist_add_items(
        playlist_id = sw_id, 
        items = song_uris, 
        position = None
        )
    return ('Discover Weekly songs added successfully')
      
def check_token():
    token_info = session.get(TOKEN_INFO, None)
    if not token_info:
        # If token is not found, redirect to authorisation page
        redirect(url_for('login', _external=False))
        
    # Check if the token is expired and refresh it if necessary
    now = int(time.time())
    is_expired = token_info['expires_at'] - now < 60
    
    if is_expired:
        token_info = auth_manager.refresh_access_token(token_info['refresh_token'])
    return token_info


app.run(debug=True)