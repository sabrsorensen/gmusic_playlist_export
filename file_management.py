import os
import fnmatch
#import eyeD3
from mutagen import flac, mp3, asf, ogg, mp4
import mutagen


def pathfinder(root, song):
    '''Return a local path for the given song'''
    foundMultiple = False
    foundUnsupported = False
    for path, directories, files in os.walk(os.path.abspath(root)):
        for filename in fnmatch.filter(files, '*' + song.get('title') + '*'):#+ ('.mp3' or '.flac' or '.wma' or '.m4a' or '.ogg')):
            if filename.endswith('.mp3') or filename.endswith('.flac') or filename.endswith('.ogg') or filename.endswith('.wma') or filename.endswith('.m4a'):
                audio = mutagen.File(os.path.join(path, filename), easy=True)                
                '''Old eyeD3 code, kept for archival purposes while testing mutagen code'''
                #tag = eyeD3.Tag()
                #tag.link(os.path.join(path, filename))
                #if tag.getTitle() == song.get('title') and tag.getArtist() == song.get('artist') and tag.getAlbum() == song.get('album'):
                if audio['title'][0] == song.get('title') and audio['artist'][0] == song.get('artist') and audio['album'][0] == song.get('album'):
                    if foundMultiple or foundUnsupported:
                        print "Multiple possibilities have been found. Accepting: %s - %s - %s" % (audio['artist'][0], audio['album'][0], audio['title'][0])
                        print os.path.join(path, filename) + '\n'
                        raw_input("Press Enter to continue...\n")
                    return os.path.join(path, filename)
                else:
                    foundMultiple = True
                    print "Song %s - %s - %s not found." % (song.get('artist'), song.get('album'), song.get('title'))
                    print "Found %s - %s - %s instead.\n" % (audio['artist'][0], audio['album'][0], audio['title'][0])
                    pass
            else:
                foundUnsupported = True
                print "Found %s." % filename
                print "Found no audio file matching %s - %s - %s. Other filetypes unsupported at this time.\n" % (song.get('artist'), song.get('album'), song.get('title'))

    print "Song %s - %s - %s not found locally." % (song.get('artist'), song.get('album'), song.get('title'))
    raw_input("Press Enter to continue...\n")