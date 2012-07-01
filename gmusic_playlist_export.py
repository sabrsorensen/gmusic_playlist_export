import gmusicapi
import getpass
import os
from mutagen.mp3 import MP3

api = gmusicapi.Api()

account = raw_input('Input your Google Music account:')
password = getpass.getpass("Password: ")
api.login(account,password)

musicRoot = raw_input('Enter the location of your music library:')

playlists = api.get_all_playlist_ids()

userlists = playlists.get('user')
listnames = userlists.keys()
listids = userlists.values()

for id in listids:
    songs = api.get_playlist_songs(id)
    for song in songs:
        trackInfo = [song.get('albumArtist'),song.get('album'),song.get('artist'),song.get('name'),"%02d" % song.get('track')]
        print trackInfo
      #  print "Music Library\\" + trackAlbumArtist + '\\' + trackAlbum + '\\' + ("%02d" % trackNumber) + ' - ' + trackArtist + ' - ' + trackName
