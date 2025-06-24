import firebase_admin
from firebase_admin import credentials, auth as firebase_auth

cred = credentials.Certificate("/etc/secrets/firebase_credentials.json")
firebase_admin.initialize_app(cred)

def verify_token(token: str):
    try:
        decoded_token = firebase_auth.verify_id_token(token)
        return decoded_token
    except Exception as e:
        raise Exception("Invalid token") from e
