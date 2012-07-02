import eyeD3

__author__ = 'sabrsorensen'


class M3U_Gen:
    def __init__(self, name):
        self.tagger = eyeD3.Tag()
        self.m3u_out = open(name + '.m3u', 'w')
        self.m3u_out.write("#Playlist " + name + " generated by gmusic_playlist_export\n#EXTM3U\n")

    def M3UEntry(self, path):
        self.tagger.link(path)
        self.m3u_out.write("#EXTINF:," + self.tagger.getArtist() + " - " + self.tagger.getTitle + "\n")
        self.m3u_out.write(path + "\n")

    def M3UClose(self):
        self.m3u_out.close()
