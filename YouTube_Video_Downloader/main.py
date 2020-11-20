from pytube import YouTube
video_url = input('Enter the link')
try:
    you_object = YouTube(video_url)
 
    filters = you_object.streams.filter(progressive=True, file_extension='mp4')   
    filters.get_highest_resolution().download()
    print('Video Downloaded')
except Exception as e:
    print(e)
