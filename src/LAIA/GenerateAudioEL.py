import requests
from elevenlabs import client
from elevenlabs.client import ElevenLabs
from elevenlabs import play
from dotenv import load_dotenv
import os

load_dotenv()

client = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_KEY")
)

voice_id = "Sarah"

def generate_audio_with_elevenlabs(text):
    
    try:
        # Call the ElevenLabs generate function directly
        audio_content = client.generate(text=text, voice="Sarah", model="eleven_multilingual_v2")
        print("Audio generated successfully")
        play(audio_content) 
        return audio_content
    except Exception as e:
        print(f"Failed to generate audio: {e}")
        return None

  




    
