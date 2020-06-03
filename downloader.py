from pytube import YouTube
import sys

video = YouTube(sys.argv[1])

video.streams.filter(file_extension = 'mp4')[0].download()



