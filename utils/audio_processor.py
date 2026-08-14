import os
import sys
from pathlib import Path
import audioop
import yt_dlp




sys.modules["audioop"] = audioop


from pydub import AudioSegment


DOWNLOAD_DIR = "mydownloads"
os.makedirs(DOWNLOAD_DIR,exist_ok=True)

def download_youtube_audio(url:str)-> str:
    output_path = os.path.join(DOWNLOAD_DIR,"%(title)s.%(ext)s")

    ydl_opts = {
        "format":"bestaudio/best",
        "outtmpl":output_path,

         # Required for current YouTube extraction
        "js_runtimes": {
            "deno": {}
        },
        
        "postprocessors": [
            {
                "key":"FFmpegExtractAudio",
                "preferredcodec":"wav",
                "preferredquality":"192",
            }
        ],
        "quiet":False

    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info).replace(".webm",".wav").replace(".m4a",".wav")
    return filename


try:
    file = download_youtube_audio(
        "https://www.youtube.com/watch?v=Lg-meK5IU8Q"
    )
    #print("Downloaded file:", file)

except Exception as e:
    print("ERROR TYPE:", type(e).__name__)
    print("ERROR:", e)


def convert_to_wav(input_path:str)-> str:
    """Converts any audio video file to wav format using pydub"""
    output_path = os.path.splitext(input_path)[0]+"_converted.wav"
    audio = AudioSegment.from_file(input_path)
    audio = audio.set_channels(1).set_frame_rate(16000) #16khz
    audio.export(output_path,format="wav")
    return output_path

path = convert_to_wav(file)
print("Path of converted file : ",path)


# Chunk the audio file
def chunk_audio(wav_path:str,chunk_minutes:int=10)-> list:
    audio = AudioSegment.from_wav(wav_path)
    chunk_ms = chunk_minutes*60*1000 #chunking works in millisec so chunk_mins*60*1000

    chunks = []

    for i,start in enumerate(range(0,len(audio),chunk_ms)):
        chunk = audio[start : start+chunk_ms]
        chunk_path = f"{wav_path}_chunk_{i}.wav"
        chunk.export(chunk_path,format="wav")

        chunks.append(chunk_path)
    return chunks

print(chunk_audio(path))

def process_input(source:str)-> list:
    if source.startswith("http://") or source.startswith("https://"):
        print("Detected Youtube URL. Downloading audio...")
        wav_path = download_youtube_audio(source)
    else:
        print("Detected local file. Converting to wav...")
        wav_path = convert_to_wav(source)

    print("Chunking audio...")
    chunks = chunk_audio(wav_path=wav_path)
    print(f"Audio Ready - {len(chunks)} chunk(s) created.")
    return chunks