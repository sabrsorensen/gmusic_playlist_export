import gmusicapi
from local_constants import account, password, music_path
from file_management import pathfinder
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

for id in listids:
    songs = api.get_playlist_songs(id)
    for song in songs:
        path = pathfinder(music_path, song)
