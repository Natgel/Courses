from pytube import YouTube

def download_Video(yt):
  # filter mp4 streams from object
  my_streams = yt.streams.filter(file_extension='mp4', only_video=False)
  for streams in my_streams:
    # print itag, resolution and codec format of Mp4 streams
    print(
        f"Video itag : {streams.itag} Resolution : {streams.resolution} VCodec : {streams.codecs[0]}")

  # enter the itag value of resolution on which you want to download the video
  input_itag = input("Enter itag Value : ")
  # get video using itag vale
  video = yt.streams.get_by_itag(input_itag)

  # finally download the YouTube Video...
  video.download()
  print("Video is Downloading as", yt.title+".mp4")


LINK4 = "https://www.youtube.com/watch?v=Wqmtf9SA_kk"
LINK = "https://www.youtube.com/watch?v=PXMJ6FS7llk&t=525s"
LINK2 = "https://www.youtube.com/watch?v=K-Kr6eTK4MY"
LINK3 = "https://www.youtube.com/watch?v=NfggT5enF4o"
path = "/Users/NaGe/python weather app/"
filename = "automatewithpython"
prefix = "mp4"
str_file = ""

# Create YouTube Object.
yt = YouTube(LINK4)
# call The function..
download_Video(yt)
