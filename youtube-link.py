import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as messagebox
import moviepy.editor as mp
import os
from pytube import YouTube


def download_video():
    video_url = entry.get()
    if "youtube.com" not in video_url:
        status_label["text"] = "Invalid YouTube URL"
        return

    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        default_filename = stream.default_filename
        download_path = os.path.join("Downloads", default_filename)
        stream.download(output_path="Downloads")
        status_label["text"] = "Video downloaded successfully"
    except Exception as e:
        status_label["text"] = f"Error: {str(e)}"


def extract_audio():
    video_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4")])
    if video_path:
        video = mp.VideoFileClip(video_path)
        audio = video.audio
        audio_path = filedialog.asksaveasfilename(defaultextension=".mp3",
                                                  filetypes=[("Audio Files", "*.mp3")])
        if audio_path:
            audio.write_audiofile(audio_path)
            status_label["text"] = "Audio extracted and saved successfully"
        else:
            status_label["text"] = "Audio save canceled"
    else:
        status_label["text"] = "No video file selected"


window = tk.Tk()
window.title("Video Downloader")
window.geometry("400x200")

entry = tk.Entry(window)
entry.pack()

download_button = tk.Button(window, text="Download Video", command=download_video)
download_button.pack()

extract_button = tk.Button(window, text="Extract Audio", command=extract_audio)
extract_button.pack()

status_label = tk.Label(window, text="")
status_label.pack()

window.mainloop()
