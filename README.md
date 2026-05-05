# Video-to-Notes AI Assistant

An AI-powered system that converts video content into structured study notes using speech recognition and local LLMs.

---

## Overview

This project processes a video file, extracts audio, converts speech to text, and generates structured notes automatically. It helps in summarizing long lectures or tutorials into concise documentation.

---

## Features

- Extracts audio from video (MoviePy)  
- Converts speech to text (Google STT)  
- Generates structured notes (Agno + Ollama)  
- Handles long videos via chunking  
- Saves output as text file  

---

## Tech Stack

- Python  
- MoviePy  
- Pydub  
- Google Speech-to-Text  
- Agno  
- Ollama (Llama 3.2)  

---

---

## Workflow

Video → Audio → Chunking → Speech-to-Text → Transcript → LLM → Notes

---

## Setup & Run

1. Clone repository  
```bash
git clone https://github.com/bhavyaaaa08/video-to-notes.git
cd video-to-notes
```
2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Set Google credentials
```bash
set GOOGLE_APPLICATION_CREDENTIALS="path\to\key.json"
```
5. Start Ollama
```bash
ollama run llama3.2
```
6. Run project
```bash
python main.py
```
## Output

The system generates structured notes including:

- Title
- Topics Covered
- Detailed Notes
- Key Takeaways

Saved inside the output/ folder.

## Notes

- Audio is converted to mono for compatibility
- Chunking is used due to API size limits
- Large transcripts may be truncated for local models
- You need to create a videos/ directory and upload a sample video to check it.