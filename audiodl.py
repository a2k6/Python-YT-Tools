from pytubefix import YouTube

# where to save 
SAVE_PATH = "audio" #to_do 

# Links of the videos to be downloaded
urls = input("Enter each of the links with a space between each: ").split()

for url in urls:
    # Get video from YouTube
    yt = YouTube(url)

    try: 
        # Downloading the video 
        yt.streams.get_audio_only().download(output_path=SAVE_PATH)
        print('Audio downloaded successfully!')
    except: 
        print("Error!")

print('Task Completed!')