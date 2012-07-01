import gmusicapi
from local_constants import account, password, music_path
import os
import eyeD3

api = gmusicapi.Api()

#from getpass import getpass
#account = raw_input('Input your Google Music account:')
#password = getpass("Password: ")
#musicRoot = raw_input('Enter the location of your music library:')
api.login(account, password)

playlists = api.get_all_playlist_ids()

userlists = playlists.get('user')
listnames = userlists.keys()
listids = userlists.values()

music_path = music_path

for root, dirs, files in os.walk(music_path):
    print files

for id in listids:
    songs = api.get_playlist_songs(id)
    for song in songs:
        trackInfo = [song.get('albumArtist'), song.get('album'), song.get('artist'), song.get('name'), "%02d" % song.get('track')]
        print trackInfo
