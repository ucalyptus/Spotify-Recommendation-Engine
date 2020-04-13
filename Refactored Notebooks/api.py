import utils.py

cid = "ffbef2bcb4b84e80b3a0039a2906cb01"
secret = "6c57daa1247f4abe96f38635d38869a0"
username = "francocasadei"
redirect_uri = "https://developer.spotify.com/dashboard/applications/ffbef2bcb4b84e80b3a0039a2906cb01"
scope = "user-library-read playlist-modify-public playlist-read-private"

client_credentials_manager = SpotifyClientCredentials(
    client_id=cid, client_secret=secret
)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
token = util.prompt_for_user_token(username, scope, cid, secret, redirect_uri)

# https://open.spotify.com/user/francocasadei/playlist/6aWL6tZgIycyz98WgigfsG
sourcePlaylistID = "6aWL6tZgIycyz98WgigfsG"
sourcePlaylist = sp.user_playlist(username, sourcePlaylistID)
