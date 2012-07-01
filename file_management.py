import os
import fnmatch
import eyeD3


def pathfinder(root, song):
    '''Return a local path for the given song'''
    for path, directories, files in os.walk(os.path.abspath(root)):
        for filename in fnmatch.filter(files, song.get('title')):
            tag = eyeD3.Tag()
            tag.link(os.path.join(path, filename))
            if tag.getArtist() == song.get('artist') and tag.getAlbum() == song.get('album') and tag.getTitle() == song.get('title'):
                print os.path.join(path, filename)
                yield os.path.join(path, filename)
