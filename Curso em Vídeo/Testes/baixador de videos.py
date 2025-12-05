import yt_dlp

url = input('Digite a URL: ')

ydl_opts = {
    'outtmpl': 'E:/%(title)s.%(ext)s',
    'format': 'bestvideo+bestaudio/best',
    'merge_output_format': 'mp4',
    'cookiesfrombrowser': ('firefox',),  # ← Firefox detectado automaticamente
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
