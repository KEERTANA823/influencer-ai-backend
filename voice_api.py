voice_api.py

import azure.cognitiveservices.speech as speechsdk

SPEECH_KEY = "YOUR_AZURE_SPEECH_KEY" SERVICE_REGION = "YOUR_AZURE_REGION"

def generate_voice_audio(prompt: str): speech_config = speechsdk.SpeechConfig(subscription=SPEECH_KEY, region=SERVICE_REGION) audio_output_config = speechsdk.audio.AudioOutputConfig(filename="output.wav") speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_output_config) result = speech_synthesizer.speak_text(prompt)

if result.reason != speechsdk.ResultReason.SynthesizingAudioCompleted:
    raise Exception("Azure voice synthesis failed")

# You would typically upload output.wav to cloud storage and return the public URL
return "https://your-storage-service/output.wav"
