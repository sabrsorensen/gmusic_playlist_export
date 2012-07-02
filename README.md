Overview
=========

gmusic_playlist_export is a Python script utilizing simon-weber's [Unofficial Google Music API](https://github.com/simon-weber/Unofficial-Google-Music-API) to interface with the Google Music servers.

Google Music playlists are retrieved through the API, then scanned for individual song metadata.
The metadata is used to scan a user-specified local directory in an attempt to locate the 
corresponding songs. Once the songs are located, the locations are written to a local .m3u 
in the same order as found in the playlist retrieved from Google Music. 

File searching requires the song title to be in the local filename, and the local file's tags 
must match the tags stored in Google Music.

Dependencies
==============

   * [gmusicapi](http://pypi.python.org/pypi/gmusicapi/2012.05.04)
   * [eyeD3](http://pypi.python.org/pypi/eyeD3-pip/0.6.19)

Use
====

Install the required dependencies, then manuever to the directory you downloaded the script to. Run the script with `python gmusic_playlist_export.py` and answer the prompts in the CLI. **Make sure the tracks have the song title in the filename, and the metadata matches between the local and Google Music copies of the music**. All generated playlists will be placed in a GMusic Exported Playlists folder inside your specified music folder.
