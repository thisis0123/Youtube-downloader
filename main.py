from download_playlist import Playlist1
from download_videos import YouTube1
from download_video import YouTube2
import os


def modify_path(path):
    new_path=""
    for i in path:
        if i=="\\":
            new_path+="/"
        else:
            new_path+=i

    return new_path

while True:
    os.system("cls")
    
    choice=input("""
    1: Enter 1 to download a playlist
    2: Enter 2 to download multiple videos at the same time
    3: Enter 3 to download a video with the ability to choose the stream
    choice:""")


    if choice=="1":
        url=input("Enter the URL of the playlist: ")
        path=input(r"Enter the path where this playlist will be saved: ")
        new_path=modify_path(path)

        pl=Playlist1(url,new_path)
        os.system("cls")
        print("Your playlist has been downloaded!")

    elif choice=="2":
        urls=input("Enter the URLs of the videos separated by a comma: ").split(", ")
        path=input(r"Enter the path where these videos will be saved: ")
        new_path=modify_path(path)

        yt=YouTube1(urls,new_path)
        os.system("cls")
        print("Your videos have been downloaded!")

    elif choice=="3":
        url=input("Enter the URL of the video you want to download: ")
        path=input(r"Enter the path where the video will be saved: ")
        new_path=modify_path(path)

        yt=YouTube2(url,new_path)
        os.system("cls")
        print("Your video has been downloaded!")
    
    input("Press enter to get back!")

