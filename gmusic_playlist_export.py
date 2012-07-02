import gmusicapi
#from local_constants import account, password, music_path
from file_management import pathfinder
from m3u_generation import M3U_Gen
from getpass import getpass

api = gmusicapi.Api()

account = raw_input('Input your Google Music account:')
password = getpass("Password: ")
musicRoot = raw_input('Enter the location of your music library:')
api.login(account, password)

userlists = api.get_all_playlist_ids().get('user')
listnames = userlists.keys()

for name in listnames:
    playGen = M3U_Gen(name,musicRoot)
    songs = api.get_playlist_songs(userlists.get(name))
    for song in songs:
        path = pathfinder(musicRoot, song)
        if path is None:
            continue
        playGen.M3UEntry(path)

    playGen.M3UClose()
