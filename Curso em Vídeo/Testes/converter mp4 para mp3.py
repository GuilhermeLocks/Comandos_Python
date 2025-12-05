from moviepy.editor import *

# Substitua 'video_original.mp4' pelo nome do seu arquivo MP4
# e 'audio_convertido.mp3' pelo nome desejado para o MP3.
video = VideoFileClip("video_original.mp4")
video.audio.write_audiofile("audio_convertido.mp3")
video.close() # Boa prática para liberar recursos
