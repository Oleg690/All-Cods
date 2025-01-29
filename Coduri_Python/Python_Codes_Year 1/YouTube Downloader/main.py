from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Titlu: ", yt.title)

print("Vizionări: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('D:\YouTube Videos')

print('Download Succsesfuly')