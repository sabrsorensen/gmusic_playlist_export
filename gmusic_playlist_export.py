import gmusicapi
from getpass import getpass
import os

api = gmusicapi.Api()
#username = raw_input('Google Music Username: ')
#password = getpass()
api.login('omurcada', '99;6(;23*2X4>7^.(9^@6$@4@8$/L/9i<6Jdm764*3g34j$f)p')
playlists = api.get_all_playlist_ids()

userlists = playlists.get('user')
listnames = userlists.keys()
listids = userlists.values()

music_path = '/Users/Murph/Music/iTunes/iTunes Music/'

# for id in listids:
#     songs = api.get_playlist_songs(id)
#     for song in songs:
#         trackName = song.get('name')
#         trackArtist = song.get('artist')
#         trackAlbumArtist = song.get('albumArtist')
#         trackAlbum = song.get('album')
#         trackNumber = song.get('track')

for root, dirs, files in os.walk(music_path):
    print files
