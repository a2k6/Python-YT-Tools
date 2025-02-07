from pytubefix import YouTube

# Where to save
SAVE_PATH = "vid"  # to_do

# Links of the videos to be downloaded
urls = input("Enter each of the links with a space between each: ").split()

for url in urls:
    # Get video from YouTube
    yt = YouTube(url)

    try: 
        # Downloading the video 
        yt.streams.get_highest_resolution().download(output_path=SAVE_PATH)
        print('Video downloaded successfully!')
    except: 
        print("Error!")

print('Task Completed!')