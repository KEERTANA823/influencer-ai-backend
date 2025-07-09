
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from auth import verify_token
from payments import create_payment
from voice_api import generate_voice_audio
from avatar_api import generate_avatar_video

app = FastAPI()

# Serve audio files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    return {"message": "Influencer AI Backend is running successfully"}

@app.post("/generate-voice")
def generate_voice_route(data: dict):
    text = data.get("text")
    if not text:
        raise HTTPException(status_code=400, detail="No text provided")

    audio_path = generate_voice_audio(text)
    return {"audio_url": f"/{audio_path}"}

@app.post("/generate_video")
def generate_video(token: str, prompt: str):
    user_data = verify_token(token)
    user_id = user_data["uid"]

    # Generate voice
    audio_path = generate_voice_audio(prompt)

    # Generate avatar video
    video_url = generate_avatar_video(prompt, audio_url=f"https://influencer-ai-backend-evbj.onrender.com/{audio_path}")

    return {
        "user_id": user_id,
        "prompt": prompt,
        "audio_url": f"/{audio_path}",
        "video_url": video_url
    }
