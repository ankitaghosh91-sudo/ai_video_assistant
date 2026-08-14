import yt_dlp

url = "https://www.youtube.com/watch?v=OFmxKgaLN80"

ydl_opts = {
    "format": "bestaudio/best",
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])