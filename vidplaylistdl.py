from pytubefix import Playlist

# where to save 
SAVE_PATH = "vidplaylist" #to_do 

# Links of the videos to be downloaded
urls = input("Enter each of the links with a space between each: ").split()

for url in urls:
    # Get video from YouTube
    pl = Playlist(url)
    
    for video in pl.videos():
        try: 
            # Downloading the video 
            pl.streams.get_audio_only().download(output_path=SAVE_PATH)
            print('Video downloaded successfully!')
        except: 
            print("Error!")

print('Task Completed!')