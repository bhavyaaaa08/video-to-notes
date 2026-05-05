from utils.audio import extract_audio, split_audio
from utils.stt import transcribe_chunks
from utils.notes import generate_notes
import os

VIDEO_PATH = r"C:\Users\nanaj\Documents\accure internship\video documentation\videos\test1.mp4"
AUDIO_PATH = "audio/audio.wav"

def process_video():
    print("Extracting audio...")
    extract_audio(VIDEO_PATH, AUDIO_PATH)

    print("Splitting audio...")
    chunks = split_audio(AUDIO_PATH)

    print("Transcribing chunks...")
    transcript = transcribe_chunks(chunks)

    print("Generating notes...")
    notes = generate_notes(transcript)

    os.makedirs("output", exist_ok=True)
    output_path = "output/notes.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(notes)
    print(f"\nNotes saved to {output_path}\n")

if __name__ == "__main__":
    process_video()