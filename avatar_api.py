import requests

HYGIENE_API_KEY = "YOUR_HYGIENE_API_KEY"
AVATAR_ID = "YOUR_AVATAR_ID"

def generate_avatar_video(prompt: str, audio_url: str):
    response = requests.post(
        "https://hygiene.api/avatar/generate",
        headers={"Authorization": f"Bearer {HYGIENE_API_KEY}"},
        json={
            "script": prompt,
            "voice_url": audio_url,
            "avatar_id": AVATAR_ID
        }
    )
    if response.status_code != 200:
        raise Exception("Failed to generate avatar video")
    data = response.json()
    return data["video_url"]
