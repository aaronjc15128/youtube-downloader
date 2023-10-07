from pytube import YouTube
from os import system
import time
import math

SAVE_PATH = "downloads"

links = []
links_file = open("links.txt", "r")
for link in links_file:
    links.append(link)
links_file.close()

start_time = time.time()

def message(title, number):
    current_time = time.time()
    time_elapsed = current_time - start_time
    time_elapsed_minutes = math.floor(time_elapsed/60)
    time_elapsed_seconds = math.floor(time_elapsed-(time_elapsed_minutes*60))
    
    system("clear")
    print(f"{number} / {len(links)}   {round(number/len(links)*100)}%    {time_elapsed_minutes}m {time_elapsed_seconds}s    {title}")

i = 0
for link in links:
    try:
        video = YouTube(link).streams.get_highest_resolution()
    except:
        with open("errors.txt", "w") as errors:
            errors.write(f"C:    {video.title}")

    message(video.title, i)

    try:
        video.download(SAVE_PATH)
    except:
        with open("errors.txt", "w") as errors:
            errors.write(f"D:    {video.title}")

    i += 1

message("Done!", i)