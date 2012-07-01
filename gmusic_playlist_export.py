import gmusicapi
import getpass

api = gmusicapi.Api()

api.login('','')
playlists = api.get_all_playlist_ids()

userlists = playlists.get('user')
listnames = userlists.keys()
listids = userlists.values()

input()

for id in listids:
    songs = api.get_playlist_songs(id)
    for song in songs:
        trackName = song.get('name')
        trackArtist = song.get('artist')
        trackAlbumArtist = song.get('albumArtist')
        trackAlbum = song.get('album')
        trackNumber = song.get('track')
        print "Music Library\\" + trackAlbumArtist + '\\' + trackAlbum + '\\' + ("%02d" % trackNumber) + ' - ' + trackArtist + ' - ' + trackName
