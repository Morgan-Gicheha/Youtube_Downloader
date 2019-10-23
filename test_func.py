
from pytube import YouTube

# yt=YouTube(url)
# print("retieving and combining audio with video...")
# title = (yt.title)
# print("downloading =>" (title))
# yt.download.first(https://www.youtube.com/watch?v=E_yAzZZeuAQ)
# print("video downloaded")

# from pytube import YouTube
# print('initializing state')
# yt = YouTube("https://www.youtube.com/watch?v=E_yAzZZeuAQ")
# print("getting title")

# print("getting streams")
# stream = yt.streams.first()
# print("preparing download")
# stream.download()
# print("donloaded succesfullys")
# import pytube
# print("initializing state")
# video_url = 'https://www.youtube.com/watch?v=E_yAzZZeuAQ' # copy and paste url
# print('getting video')
# youtube = pytube.YouTube(video_url)
# print('getting sreams')
# video = youtube.streams.first()
# print("downloading")

# video.download('Downloadss') # path, where to video download.
# print('downloaded')
# # it may take some tome to download.

def download_yt(url):
    print('getting video...')
    yt = YouTube(url)
    print('getting streams')

    stream=yt.streams.first()
    print('getting video title...')
    print(yt.title)
    print('downloadint video...')
    yt.stream.download()
    print('#####Download complete#####')

    'https://www.youtube.com/watch?v=m_MW_iLLHaA'
