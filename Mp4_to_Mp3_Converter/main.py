import moviepy.editor
video = moviepy.editor.VideoFileClip('yourvideo.mp4')
audio=video.audio
audio.write_audiofile('saveas.mp3')
