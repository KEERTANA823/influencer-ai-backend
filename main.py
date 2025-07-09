from fastapi import FastAPI, HTTPException
from auth import verify_token
from payments import create_payment
from voice_api import generate_voice_audio
from avatar_api import generate_avatar_video

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Influencer AI Backend is running successfully"}

@app.post("/generate_video/")
def generate_video(token: str, prompt: str):
    user_data = verify_token(token)
    user_id = user_data["uid"]

    # Generate voice audio
    audio_file = generate_voice_audio(prompt)

    # Use the audio file to generate avatar video
    # For now just mock the URL
    mock_audio_url = f"https://yourdomain.com/static/{audio_file}"
    video_url = generate_avatar_video(prompt, mock_audio_url)

    return {
        "user_id": user_id,
        "audio_file": audio_file,
        "video_url": video_url
    }

@app.post("/create_payment/")
def payment(token: str):
    user_data = verify_token(token)
    user_id = user_data["uid"]
    result = create_payment(user_id)
    return result
