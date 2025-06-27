import whisper
from transformers import pipeline
import os
import shutil
import subprocess
from pydub import AudioSegment

def convert_to_wav(input_path, output_path="input.wav"):
    print("[INFO] Converting input to WAV...")
    audio = AudioSegment.from_file(input_path)
    audio = audio.set_frame_rate(16000).set_channels(1)
    audio.export(output_path, format="wav")
    return output_path

def transcribe_telugu(audio_path):
    print("[INFO] Transcribing Telugu audio using Whisper...")
    model = whisper.load_model("large")  # You can use "medium" if "large" is too big
    result = model.transcribe(audio_path, language="te")
    print("[INFO] Telugu Text:", result["text"])
    return result["text"]

def translate_to_english(text):
    print("[INFO] Translating to English using HuggingFace model...")
    translator = pipeline("translation", model="facebook/nllb-200-distilled-600M")
    result = translator(text, src_lang="te", tgt_lang="eng_Latn")
    english = result[0]["translation_text"]
    print("[INFO] English Translation:", english)
    return english

def run_tortoise_tts(text, voice_sample_dir="voice_sample", output_dir="outputs"):
    print("[INFO] Preparing Tortoise voice cloning...")

    with open("prompt.txt", "w", encoding="utf-8") as f:
        f.write(text)

    voice_id = "custom_voice"
    voice_dir = f"tortoise-tts/voices/{voice_id}"
    os.makedirs(voice_dir, exist_ok=True)

    for f_name in os.listdir(voice_sample_dir):
        if f_name.endswith(".wav"):
            shutil.copy(os.path.join(voice_sample_dir, f_name), os.path.join(voice_dir, f_name))

    escaped_text = text.replace('"', '\\"').replace("\n", " ")
    os.makedirs(output_dir, exist_ok=True)

    command = (
        f"cd tortoise-tts && "
        f"python tortoise/do_tts.py "
        f"--text \"{escaped_text}\" "
        f"--voice {voice_id} "
        f"--preset fast "
        f"--output_path ../{output_dir}"
    )

    print("[COMMAND]", command)
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print("[STDOUT]:", result.stdout)
    print("[STDERR]:", result.stderr)

    for file in os.listdir(output_dir):
        if file.startswith(voice_id) and file.endswith(".wav"):
            output_path = os.path.join(output_dir, file)
            print("[INFO] English audio output saved at:", output_path)
            return output_path

    raise FileNotFoundError("Tortoise-TTS did not produce an output WAV file.")

# ===================== MAIN PIPELINE =====================

def main():
    print(" Enter path to your Telugu audio file (.wav/.mp3/.mp4):")
    input_path = input(">>> ").strip()

    if not os.path.exists(input_path):
        print(" File not found!")
        return

    # Convert to WAV
    wav_path = convert_to_wav(input_path)

    # Transcribe
    telugu_text = transcribe_telugu(wav_path)

    # Translate
    english_text = translate_to_english(telugu_text)


    # Generate Audio
    try:
        output_audio = run_tortoise_tts(english_text)
        print(" Done! Your English audio with your voice is saved as:", output_audio)
    except FileNotFoundError as e:
        print(" TTS Error:", e)

if __name__ == "__main__":
    main()
