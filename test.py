from utils.audio_processor import process_input
from core.transcriber import transcribe_all
from core.summarizer import summarize, generate_title
from core.extractor import extract_action_items, extract_key_decisions, extract_questions
import time

source = "https://www.youtube.com/watch?v=VlSdTbrvNRw"

language = "english"

total_start = time.perf_counter()


# ============================================================
# 1. AUDIO PROCESSING
# ============================================================

start = time.perf_counter()

chunks = process_input(source)

print(f"\n⏱ Audio processing: {time.perf_counter() - start:.2f} sec")


# ============================================================
# 2. TRANSCRIPTION
# ============================================================

start = time.perf_counter()

full_transcript = transcribe_all(chunks,language=language)

print(f"⏱ Transcription: {time.perf_counter() - start:.2f} sec")

print("\n" + "=" * 80)

print("Full Transcript of Video \n ")

print("=" * 70)

print(full_transcript[:500] + "..." if len(full_transcript)>500 else full_transcript)

# ============================================================
# 3. TITLE
# ============================================================

start = time.perf_counter()

title = generate_title(full_transcript)

print(f"⏱ Title generation: {time.perf_counter() - start:.2f} sec")

# ============================================================
# 4. SUMMARY
# ============================================================

start = time.perf_counter()

summary = summarize(full_transcript)

print(f"⏱ Summary generation: {time.perf_counter() - start:.2f} sec")

print("\n" + "=" * 60)
print(f"📌 TITLE: {title}")
print("=" * 60)
print("\n📋 SUMMARY")
print("-" * 60)
print(summary)


# ============================================================
# 5. ACTION ITEMS
# ============================================================

start = time.perf_counter()

action_items = extract_action_items(full_transcript)

print(f"⏱ Action items: {time.perf_counter() - start:.2f} sec")

# ============================================================
# 6. KEY DECISIONS
# ============================================================

start = time.perf_counter()

decisions = extract_key_decisions(full_transcript)

print(f"⏱ Key decisions: {time.perf_counter() - start:.2f} sec")

# ============================================================
# 7. OPEN QUESTIONS
# ============================================================

start = time.perf_counter()

questions = extract_questions(full_transcript)

print(f"⏱ Open questions: {time.perf_counter() - start:.2f} sec")

print("\n" + "=" * 60)
print("✅ ACTION ITEMS")
print("=" * 60)
print(action_items)

print("\n" + "=" * 60)
print("🔑 KEY DECISIONS")
print("=" * 60)
print(decisions)

print("\n" + "=" * 60)
print("❓ OPEN QUESTIONS")
print("=" * 60)
print(questions)