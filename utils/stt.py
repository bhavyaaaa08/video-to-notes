from google.cloud import speech
from tqdm import tqdm

def transcribe_chunk(audio_file):
    client = speech.SpeechClient()

    with open(audio_file, "rb") as f:
        content = f.read()

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        language_code="en-US",
        enable_automatic_punctuation=True,
    )

    response = client.recognize(config=config, audio=audio)

    text = ""
    for result in response.results:
        text += result.alternatives[0].transcript + " "

    return text


def transcribe_chunks(chunk_paths):
    full_transcript = ""

    for chunk in chunk_paths:
        print(f"Processing {chunk}...")
        full_transcript += transcribe_chunk(chunk)

    return full_transcript