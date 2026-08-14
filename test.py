from utils.audio_processor import process_input
from core.transcriber import transcribe_all

source = "https://www.youtube.com/watch?v=iQSZIOoe8P4"

language = "english"

chunks = process_input(source)

full_transcript = transcribe_all(chunks,language=language)

print("\n" + "=" * 80)

print("Full Transcript of Video \n ")

print("=" * 70)

print(full_transcript[:500] + "..." if len(full_transcript)>500 else full_transcript)