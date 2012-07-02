import gmusicapi
from file_management import pathfinder
from m3u_generation import M3U_Gen
from getpass import getpass

api = gmusicapi.Api()

account = raw_input('Input your Google Music account: ')
password = getpass("Password: ")
try:
    api.login(account, password)
except api.NotLoggedIn:
    print("Your account details didn't check out. Please restart the script and try again.")
music_root = raw_input('Enter the location of your music library: ')

userlists = api.get_all_playlist_ids().get('user')
listnames = userlists.keys()

for name in listnames:
    print("Exporting playlist " + name + "...")
    playGen = M3U_Gen(name, music_root)
    songs = api.get_playlist_songs(userlists.get(name))
    for song in songs:
        path = pathfinder(music_root, song)
        if path is None:
            continue
        playGen.M3UEntry(path)

    playGen.M3UClose()

print("Your playlists have been exported to " + music_root + "GMusic Exported Playlists, happy listening!")
