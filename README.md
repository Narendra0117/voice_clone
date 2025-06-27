# Telugu-to-English Voice Translator with Voice Cloning

This project enables Telugu speech audio to be:
1. Transcribed into Telugu text
2. Translated into English
3. Spoken aloud in your own cloned voice

Built for real-time communication, accessibility, and cross-language interaction, this pipeline leverages cutting-edge open-source AI models to preserve your voice across languages.

---

## Key Features

- Telugu Audio Input: Accepts `.wav`, `.mp3`, or `.mp4` files
- Speech Recognition: Uses OpenAI’s Whisper to transcribe Telugu speech
- Translation: Translates transcribed Telugu into fluent English using HuggingFace’s `facebook/nllb-200` model
- Voice Cloning: Synthesizes translated English text in your own voice using Tortoise TTS
- Audio Conversion: Automatically converts input formats to Whisper-compatible `.wav`
- Output: Generates English audio as `.wav` while preserving your speaker identity

---

## Project Structure

telugu_voice_translation_project/
├── main_pipeline.py # Main orchestrating script
├── voice_sample/ # Your English voice samples (.wav files)
├── tortoise-tts/ # Tortoise TTS cloned repo
├── outputs/ # Final audio outputs
├── prompt.txt # Temporary file for holding generated English text
├── input_audio.wav # Converted input


---

## Workflow Overview

1. **Input**: User uploads Telugu audio (`.wav`, `.mp3`, or `.mp4`)
2. **Transcription**: Audio is transcribed to Telugu text using Whisper
3. **Translation**: Telugu text is translated to English using a multilingual model
4. **Voice Cloning**: The English text is synthesized using your pre-recorded English voice samples via Tortoise TTS
5. **Output**: English audio in your own voice is generated and saved

---

## Requirements

- Python 3.8+
- torch, torchaudio
- whisper
- transformers
- pydub
- ffmpeg
- Git clone of Tortoise TTS

You can install dependencies using:

```bash
pip install -r requirements.txt
