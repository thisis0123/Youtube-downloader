from pytubefix import YouTube
import os


class YouTube2(YouTube):
    def __init__(self,url,path):
        super().__init__(url)
        self.path=path
        self.download_video()

    def download_video(self):
        os.system("cls")
        for stream in self.streams:
            print(stream)
        
        print()
        print("These are all the available streams.")
        itag=int(input("Choose by the itag: "))
        stream=self.streams.get_by_itag(itag)
        print(self.title+" is being downloaded...")
        stream.download(self.path)

