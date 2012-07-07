import os
import fnmatch
#import eyeD3
from mutagen import flac, mp3, asf, ogg, mp4
import mutagen

class Finder:
    def __init__(self):
        self.history = {}
        self.global_missing = {}

    def print_missing(self):
        print "\nMissing tracks in the following playlists:"
        for playlist in self.global_missing.keys():
            print "\nPlaylist %s:\n" % playlist
            for track in self.global_missing[playlist]:
                print "     %s" % track
        print "Downloading is unsupported at this time, use the official Google Music Manager or otherwise obtain a local copy.\n"

    def pathfinder(self, root, song, name):
        '''Return a local path for the given song'''
        foundMultiple = False
        foundUnsupported = False
        results = []
        if name not in self.global_missing:
            playlist_missing = []
        else:
            playlist_missing = self.global_missing[name]
        songInfo = "%s - %s - %s" % (song.get('artist'), song.get('album'), song.get('title'))
        if songInfo in self.history:
            return self.history[songInfo]
        for path, directories, files in os.walk(os.path.abspath(root)):
            for filename in fnmatch.filter(files, '*' + song.get('title') + '*'):
                if filename.endswith('.mp3') or filename.endswith('.flac') or filename.endswith('.ogg') or filename.endswith('.wma') or filename.endswith('.m4a'):
                    audio = mutagen.File(os.path.join(path, filename), easy=True)
                    if audio['title'][0] == song.get('title') and audio['artist'][0] == song.get('artist') and audio['album'][0] == song.get('album'):
                        if foundMultiple:
                            print "Multiple possibilities have been found. Perfect match located: %s - %s - %s" % (audio['artist'][0], audio['album'][0], audio['title'][0])
                            print os.path.join(path, filename) + '\n'
                            #raw_input("Press Enter to continue...\n")
                        self.history[songInfo] = os.path.join(path, filename)
                        return os.path.join(path, filename)
                    else:
                        foundMultiple = True
                        results.append(os.path.join(path,filename))
        if foundMultiple and len(results) > 1:
            print "\nFuzzy or multiple possible matches found for %s, please select from the following:\n" % songInfo
            resultCount = 1
            for match in results:
                print "[%d]: %s\n" % (resultCount, results[resultCount-1])
                resultCount += 1
            choice = raw_input("Enter your selection:")
            while (int(choice) > resultCount or int(choice) < 1):
                print "Invalid selection, try again.\n"    
                choice = raw_input("Enter your selection:")
            self.history[songInfo] = results[int(choice)-1]
            return results[int(choice)-1]
        if foundMultiple and len(results) == 1:
            self.history[songInfo] = results[0]
            return results[0]

        playlist_missing.append(songInfo)
        self.global_missing[name] = playlist_missing