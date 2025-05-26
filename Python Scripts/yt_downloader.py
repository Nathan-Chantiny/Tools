'''
Little script for downloading YouTube videos
'''
import yt_dlp

url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
output_path = r"d:\PROJECTS\Tools\YT_Vids\rick_roll.%(ext)s"

ydl_opts = {
    'outtmpl': output_path,
    'format': 'bestvideo+bestaudio/best',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("done")