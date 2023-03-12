import tkinter as tk
from pytube import YouTube
import os

root = tk.Tk()

root.geometry("800x500")
root.title("YT_Downloader")

labelis1 = tk.Label(text="Enter youtube link:")
labelis1.place(rely=0.1, relx=0.03)
entry1 = tk.Entry()
entry1.place(rely=0.1, relx=0.20, height=23, width=500)
button1 = tk.Button(text="Upload", command=lambda: upload())
button1.place(rely=0.1, relx=0.85, height=24)
labelis2 = tk.Label(text="********Done********")
yttitle = tk.Label(text="Title:")
yttitle.place(relx=0.03, rely=0.2)
ytviews = tk.Label(text="Views:")
ytviews.place(relx=0.03, rely=0.25)
ytlenght = tk.Label(text="Lenght:")
ytlenght.place(relx=0.03, rely=0.3)
ytauthor = tk.Label(text="Author:")
ytauthor.place(relx=0.03, rely=0.35)


def upload():
    link = entry1.get()
    yt = YouTube(link)
    title = tk.Label(text=yt.title)
    title.place(rely=0.2, relx=0.1)
    views = tk.Label(text=yt.views)
    views.place(rely=0.25, relx=0.1)
    lenght = tk.Label(text=yt.length)
    lenght.place(rely=0.3, relx=0.1)
    author = tk.Label(text=yt.author)
    author.place(rely=0.35, relx=0.1)
    mp4 = tk.Button(text="Download MP4", command=lambda: download_mp4())
    mp4.place(rely=0.45, relx=0.1)
    mp3 = tk.Button(text="Download MP3", command=lambda: download_mp3())
    mp3.place(rely=0.45, relx=0.25)


def download_mp4():
    link = entry1.get()
    yt = YouTube(link)

    yd = yt.streams.get_highest_resolution()

    yd.download("C:\\Users\\User\\Desktop\\ytdownloads\\videos")
    labelis = tk.Label(text="Downloaded MP4 succesfully!!")
    labelis.place(relx=0.03, rely=0.55)


def download_mp3():
    link = entry1.get()
    yt = YouTube(link)

    video = yt.streams.filter(only_audio=True).first()

    out_file = video.download("C:\\Users\\User\\Desktop\\ytdownloads\\audios")

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    labelis = tk.Label(text="Downloaded MP3 succesfully!!")
    labelis.place(relx=0.03, rely=0.55)


root.mainloop()
