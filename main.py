main.py

from fastapi import FastAPI, HTTPException, Depends from auth import verify_token from avatar_api import generate_avatar_video from voice_api import generate_voice_audio from payments import handle_payment

app = FastAPI()

@app.get("/") def root(): return {"message": "Influencer AI Backend is running!"}

@app.post("/generate") def generate_content(prompt: str, user_token: str = Depends(verify_token)): try: # Generate voice audio_url = generate_voice_audio(prompt)

# Generate avatar video
    video_url = generate_avatar_video(prompt, audio_url)

    return {"video_url": video_url}
except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

@app.post("/payment") def process_payment(user_id: str, plan: str): try: payment_status = handle_payment(user_id, plan) return {"status": payment_status} except Exception as e: raise HTTPException(status_code=500, detail=str(e))