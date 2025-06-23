auth.py

import firebase_admin from firebase_admin import credentials, auth

cred = credentials.Certificate("firebase_key.json") firebase_admin.initialize_app(cred)

def verify_token(token: str): try: decoded_token = auth.verify_id_token(token) return decoded_token except Exception as e: raise Exception("Authentication failed")