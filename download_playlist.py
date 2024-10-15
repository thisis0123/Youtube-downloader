from pytubefix import Playlist 
import os


class Playlist1(Playlist):
    def __init__(self,url,path):
        super().__init__(url)
        self.path=path
        self.download_playlist()
    
    def download_playlist(self):
        for video in self.videos:
            os.system("cls")
            stream=video.streams.get_highest_resolution()
            print(video.title+" is being downloaded...")
            stream.download(self.path)




