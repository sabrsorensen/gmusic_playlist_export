gmusic_playlist_export is a Python script utilizing simon-weber's Unofficial Google Music API 
located at https://github.com/simon-weber/Unofficial-Google-Music-API to interface with the 
Google Music servers.

Google Music playlists are retrieved through the API, then scanned for individual song metadata.
The metadata is used to scan a user-specified local directory in an attempt to locate the 
corresponding songs. Once the songs are located, the locations are written to a local .m3u 
in the same order as found in the playlist retrieved from Google Music. 

File searching requires the song title to be in the local filename, and the local file's tags 
must match the tags stored in Google Music.