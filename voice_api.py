import os
import requests

SPEECH_KEY = "YOUR_AZURE_SPEECH_KEY"
SERVICE_REGION = "YOUR_AZURE_REGION"

def generate_voice(text: str):
    endpoint = f"https://{SERVICE_REGION}.tts.speech.microsoft.com/cognitiveservices/v1"
    headers = {
        "Ocp-Apim-Subscription-Key": SPEECH_KEY,
        "Content-Type": "application/ssml+xml",
        "X-Microsoft-OutputFormat": "audio-16khz-32kbitrate-mono-mp3"
    }
    body = f"""
    <speak version='1.0' xml:lang='en-US'>
        <voice xml:lang='en-US' xml:gender='Female' name='en-US-JennyNeural'>{text}</voice>
    </speak>
    """

    response = requests.post(endpoint, headers=headers, data=body.encode("utf-8"))
    if response.status_code != 200:
        raise Exception(f"Voice generation failed: {response.text}")

    return response.content
