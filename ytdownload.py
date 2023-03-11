from pytube import YouTube
import os

choose = input("1-MP4\n2-MP3\n")

if choose == "1":
    link = input("YT LINK: ")
    yt = YouTube(link)

    print("Title: ", yt.title)

    yd = yt.streams.get_highest_resolution()
    mp3 = yt.streams.get_audio_only()

    yd.download("C:\\Users\\User\\Desktop\\ytdownloads\\videos")
    print("**********Done**********")

elif choose == "2":
    yt = YouTube(input("YT LINK: "))

    print("Title: ", yt.title)

    video = yt.streams.filter(only_audio=True).first()

    out_file = video.download("C:\\Users\\User\\Desktop\\ytdownloads\\audios")

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    print("**********Done**********")
