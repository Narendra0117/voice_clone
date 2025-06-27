<<<<<<< HEAD

=======
import streamlit as st
import os
import base64
from main_pipeline import transcribe_telugu, translate_to_english, run_tortoise_tts

st.set_page_config(page_title="Telugu to English Voice Translator", layout="centered")
st.title(" Telugu ➜ English Voice Translator")
st.markdown("Convert Telugu speech into English while preserving your **own voice** (no AI voice used).")

uploaded_file = st.file_uploader("Upload your Telugu audio (.wav)", type=["wav"])

if uploaded_file:
    with open("telugu_audio.wav", "wb") as f:
        f.write(uploaded_file.read())
    st.audio("telugu_audio.wav", format="audio/wav")

    if st.button("🔁 Translate and Clone My Voice"):
        with st.spinner("Processing... Please wait..."):
            telugu_text = transcribe_telugu("telugu_audio.wav")
            english_text = translate_to_english(telugu_text)
            output_path = run_tortoise_tts(english_text)

        st.success("Translation and Voice Cloning Complete!")

        st.subheader(" Telugu Transcription")
        st.code(telugu_text)

        st.subheader(" English Translation")
        st.code(english_text)

        st.subheader(" Your Voice Speaking English")
        audio_bytes = open(output_path, "rb").read()
        st.audio(audio_bytes, format="audio/wav")

        b64 = base64.b64encode(audio_bytes).decode()
        download_link = f'<a href="data:audio/wav;base64,{b64}" download="final_output.wav">📥 Download Your English Voice</a>'
        st.markdown(download_link, unsafe_allow_html=True)
>>>>>>> e7f62f2 (commit)
