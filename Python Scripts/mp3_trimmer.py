'''
Created this little script to solve windows 11 lack of free audio trimming tools
The python verison I used to make this script was 3.12.8
Need to run "pip install pydub" in the terminal
Also need to download "FFmpeg" look up instructions for your specific operating system
For windows 11 I found installing and setting up "Windows builds from gyan.dev" to be easiest

Helpful resources:
https://pypi.org/project/pydub/
https://github.com/jiaaro/pydub
https://www.ffmpeg.org/download.html
https://phoenixnap.com/kb/ffmpeg-windows
'''

from pydub import *
from pathlib import Path

''' Easy to work with variables for setting time you would like to trim mp3 files to '''
seconds = 1000
minutes = seconds * 60

''' Gets path to mp3 file then converts it to an "AudioSegment" so that operations can be done to it '''
mp3_path = Path("C:/my_file.mp3")
mp3_file = AudioSegment.from_mp3(mp3_path)

''' Line for trimming files

    Examples: 
    trimmed_mp3 = mp3_file[:] -> copies entire .mp3 file
    trimmed_mp3 = mp3_file[:10 * minutes] -> beginning of file to 00:09:59.999
    trimmed_mp3 = mp3_file[10 * seconds:] -> ten second mark to end of .mp3 file
    trimmed_mp3 = mp3_file[56:7 * minutes] -> 56 millisecond mark to 00:06:59.999
 '''
trimmed_mp3 = mp3_file[:]

''' Exports trimmed file as .mp3 '''
file_handle = trimmed_mp3.export("C:/export.mp3", format="mp3")

''' Prints done after file is done being exported '''
print("done")
