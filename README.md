# Youtube-Video-Downloader
This Python script provides a graphical user interface (GUI) for downloading YouTube videos and extracting their audio. 
The script utilizes the Tkinter library for creating the GUI, as well as the pytube and moviepy.editor libraries for handling YouTube video downloads and audio extraction.

Prerequisites
Before running the script, make sure you have the following dependencies installed:
Python 3.x
Tkinter
pytube
moviepy

You can install the dependencies using pip by running the following command:
pip install tkinter pytube moviepy

Launch the script by executing the Python file youtube-link.py.
The GUI window will appear with an entry field and two buttons: "Download Video" and "Extract Audio".
To download a YouTube video, enter the URL of the video in the entry field and click the "Download Video" button. The video will be downloaded at the highest available resolution and saved in a "Downloads" folder within the script's directory.

To extract audio from a video file, click the "Extract Audio" button. A file dialog will open where you can select a video file (MP4 format). Once a video file is selected, another file dialog will open for choosing a save location and filename for the extracted audio (MP3 format). After selecting the save location, the audio will be extracted and saved.

The status label in the GUI window will display messages indicating the progress and outcome of the operations, such as successful downloads or any encountered errors.

Notes
The script assumes that the ffmpeg executable is installed on your system. If it's not already installed, you can download it from the FFmpeg website and add it to your system's PATH environment variable.
Ensure that you have a stable internet connection when downloading videos from YouTube.
The script supports downloading videos from YouTube only.




