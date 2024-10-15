from pytubefix import YouTube
import os


class YouTube1(YouTube):
    def __init__(self,urls,path):
        super().__init__(urls[0])
        self.urls=urls
        self.path=path
        self.download_videos()

    def download_videos(self):

        for url in self.urls:  
            os.system("cls")
            yt=YouTube(url)
            stream=yt.streams.get_highest_resolution()
            print(yt.title+" is being downloaded...")
            stream.download(self.path)
            

