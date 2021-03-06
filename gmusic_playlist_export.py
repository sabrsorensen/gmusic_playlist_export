import gmusicapi
import os
from file_management import Finder
from m3u_generation import M3U_Gen
from getpass import getpass

api = gmusicapi.Api()

account = raw_input('Input your Google Music account: ')
password = getpass("Password: ")
while not api.login(account, password):
    print "Your account details didn't check out. Please check your login details and try again."
    account = raw_input('Input your Google Music account: ')
    password = getpass("Password: ")

music_root = raw_input('Enter the location of your music library: ')
while not os.path.isdir(music_root):
    print "Music library not found, make sure you have the correct path and try again."
    music_root = raw_input('Enter the location of your music library: ')

userlists = api.get_all_playlist_ids().get('user')
listnames = userlists.keys()

finder = Finder()

for name in listnames:
    print "Exporting playlist %s..." % name
    playGen = M3U_Gen(name, music_root)
    songs = api.get_playlist_songs(userlists.get(name))
    for song in songs:
        path = finder.pathfinder(music_root, song, name)
        if path is None:
            continue
        playGen.M3UEntry(path)
    playGen.M3UClose()

finder.print_missing()
print "Your playlists have been exported to %s\\GMusic Exported Playlists\\, happy listening!" % music_root
api.logout()