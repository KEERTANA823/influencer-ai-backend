from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os, requests, time
import openai

# Load API Keys
openai.api_key = os.getenv("OPENAI_API_KEY")
HEYGEN_API_KEY = os.getenv("HEYGEN_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
ELEVENLABS_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID")

app = FastAPI()

# Allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Request Models
class ScriptRequest(BaseModel):
    product_description: str

class VoiceRequest(BaseModel):
    script: str

class AvatarRequest(BaseModel):
    script: str
    avatar_id: str

# 1️⃣ Generate AI Ad Script
@app.post("/generate-script")
async def generate_script(req: ScriptRequest):
    prompt = f"Create a short, catchy video ad script for: {req.product_description}"
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=500
    )
    return {"script": response['choices'][0]['message']['content']}

# 2️⃣ Generate AI Voice using ElevenLabs
@app.post("/generate-voice")
async def generate_voice(req: VoiceRequest):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{ELEVENLABS_VOICE_ID}/stream"
    headers = {"xi-api-key": ELEVENLABS_API_KEY}
    data = {"text": req.script}
    response = requests.post(url, json=data, headers=headers)
    audio_filename = "output_audio.mp3"
    with open(audio_filename, "wb") as f:
        f.write(response.content)
    return {"audio_path": audio_filename}

# 3️⃣ Generate Avatar Video using HeyGen
@app.post("/generate-avatar-video")
async def generate_avatar_video(req: AvatarRequest):
    url = "https://api.heygen.com/v1/video.create"
    payload = {
        "avatar_id": req.avatar_id,
        "script": req.script,
        "test": False
    }
    headers = {
        "Authorization": f"Bearer {HEYGEN_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    video_id = response.json()["data"]["video_id"]
    return {"video_id": video_id}

# 4️⃣ Check Video Status
@app.get("/check-video-status/{video_id}")
async def check_video_status(video_id: str):
    url = f"https://api.heygen.com/v1/video.get?video_id={video_id}"
    headers = {"Authorization": f"Bearer {HEYGEN_API_KEY}"}
    response = requests.get(url, headers=headers)
    data = response.json()
    return {
        "status": data["data"]["status"],
        "video_url": data["data"].get("video_url", None)
    }