

from TTS.api import TTS
import uuid
import os

def generate_voice_audio(text):
    tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False, gpu=False)
    filename = f"static/audio_{uuid.uuid4()}.wav"

    os.makedirs("static", exist_ok=True)  # Ensure 'static' folder exists
    tts.tts_to_file(text=text, file_path=filename)

    return filename  # Return the local path to the audio file
