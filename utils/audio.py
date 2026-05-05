from moviepy import VideoFileClip
from pydub import AudioSegment
import os


def extract_audio(video_path, output_path):
    """
    Extract audio from video and convert to:
    - mono channel
    - 16kHz sample rate
    - PCM WAV format (required by Google STT)
    """
    video = VideoFileClip(video_path)

    video.audio.write_audiofile(
        output_path,
        fps=16000,                 # required sample rate
        nbytes=2,                  # 16-bit audio
        codec='pcm_s16le',         # WAV format
        ffmpeg_params=["-ac", "1"] # force mono channel
    )

    return output_path


def split_audio(audio_path, chunk_length_ms=20000):
    """
    Split audio into smaller chunks (20 sec default)
    to avoid Google STT size limits.
    """
    audio = AudioSegment.from_wav(audio_path)

    # Ensure mono (extra safety)
    audio = audio.set_channels(1)

    chunks = []

    # Create chunks folder if not exists
    os.makedirs("chunks", exist_ok=True)

    for i in range(0, len(audio), chunk_length_ms):
        chunk = audio[i:i + chunk_length_ms]
        chunk_name = f"chunks/chunk_{i // chunk_length_ms}.wav"

        chunk.export(chunk_name, format="wav")
        chunks.append(chunk_name)

    return chunks