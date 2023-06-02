import tkinter as tk
from tkinter import filedialog
from pytube import YouTube


class YoutubeDownloader:
    def __init__(self, master):
        self.master = master
        master.title("Youtube Downloader")

        self.label = tk.Label(master, text="Insira o link do vídeo:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Download", command=self.download)
        self.button.pack()

    def download(self):
        url = self.entry.get()
        yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)

        save_path = filedialog.askdirectory()
        video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        video.download(save_path)

        self.label.config(text="Download completo!")

root = tk.Tk()
my_gui = YoutubeDownloader(root)
root.mainloop()
