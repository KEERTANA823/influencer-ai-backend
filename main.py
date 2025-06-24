
  
from fastapi import FastAPI, HTTPException
from auth import verify_token
from payments import create_payment
from voice_api import generate_voice
from avatar_api import generate_avatar_video

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Influencer AI Backend is running successfully"}

@app.post("/generate_video/")
def generate_video(token: str, prompt: str):
    user_data = verify_token(token)
    user_id = user_data['uid']
    
    # Generate voice audio
    audio_data = generate_voice(prompt)

    # Save the audio temporarily
    audio_file = "output_audio.mp3"
    with open(audio_file, "wb") as f:
        f.write(audio_data)

    # Mock audio URL
    audio_url = "https://your-storage-service.com/path/to/audio/output_audio.mp3"

    # Generate avatar video
    video_url = generate_avatar_video(prompt, audio_url)

    return {"video_url": video_url}

@app.post("/payment/")
def payment(token: str, plan: str):
    user_data = verify_token(token)
    user_id = user_data['uid']
    client_secret = create_payment(user_id, plan)
    return {"client_secret": client_secret}
