from pathlib import Path
from openai import OpenAI
# Load environment variables
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

def generate_audio_with_OpenAI(text):
    
    try:
        speech_file_path = Path(__file__).parent / "speech.mp3"
        response = client.audio.speech.create(
        model="tts-1",
        voice="onyx",
        input="A la ciutat, tots vivim en bombolles individuals on sovint ens trobem desconnectats del nostre entorn; veïnat, naturalesa, relacions personals...Sovint recorrem a Google per buscar informació, oblidant-nos del coneixement que tenen les persones del nostre voltant, i perdent, cada cop més, el coneixement local."
        )
        print("Audio generated successfully")
        return response.stream_to_file(speech_file_path)
        
    except Exception as e:
        print(f"Failed to generate audio: {e}")
        return None             



