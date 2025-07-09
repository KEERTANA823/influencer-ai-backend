import pyttsx3
import uuid

def generate_voice_audio(text):
    engine = pyttsx3.init()
    output_path = f"output_{uuid.uuid4()}.mp3"
    engine.save_to_file(text, output_path)
    engine.runAndWait()
    return output_path
