from dotenv import load_dotenv
from openai import OpenAI
from langchain_community.document_loaders.merge import MergedDataLoader
import TranscribeAudio
import SupaBase
import local_data_loader
import CreateVector
import ModifyingPrompt
import os
from io import BytesIO
import time, json
from fastapi.responses import FileResponse
from typing import Union, Annotated
import DetectLanguage
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse, JSONResponse
import GenerateAudioOA
import GenerateAudioEL

app = FastAPI()

@app.get("/hello")
def read_root():
    return {"Hello": "World"}

# Load environment variables
load_dotenv()

# Create a client instance
openai_client = OpenAI()

# Setup Supabase client
supabase_client = SupaBase.setup_supabase_client()

# Define the path to your audio file
audio_path = "docs/audiorecord/TestRecord.wav"


@app.get("/api/update_vectorstore")
def fetch_data_rebuild_vectorstore():
    SupaBase.fetch_data_from_database_and_save(supabase_client)

    # Load documents from local folder
    local_docs = local_data_loader.load_local_documents("docs/opendata")

    # Fetch data from Supabase
    database_docs = local_data_loader.load_local_documents("docs/inputdata")

    # Combine documents from local and database
    combined_docs = [*local_docs, *database_docs]

    # Create and load vector store
    vector_store = CreateVector.create_vector_store(combined_docs)

    return 200, "Vectorstore created"


@app.post("/api/rag_processing")
async def rag_processing(audio_file: UploadFile):

    file_uploaded_status = 'in_process' 
    transcription_status = 'in_process'
    language_status = 'in_process'
    llm_answer_status = 'in_process'

    print(audio_file, type(audio_file))
    # Save the uploaded audio file locally
    file_location = f"docs/audiorecord/{audio_file.filename}"
    with open(file_location, 'wb') as f:
        f.write(await audio_file.read())

    file_uploaded_status = 'completed' 

    # Get the transcription
    transcription_text = TranscribeAudio.transcribe_audio(openai_client, file_location)
    
    # Print the transcription
    print("Transcription:\n", transcription_text)

    transcription_status = transcription_text

    # Detect Language
    language = DetectLanguage.detect_language(transcription_text)
    print("Detected Language:", language)
    language_status = language

    

    if os.path.exists(file_location):
        os.remove(file_location)

    ##### run RAG 
    vector_store = CreateVector.load_vector_store('docs/static')
    chain = ModifyingPrompt.create_chain(vector_store)

    # Invoke the chain
    response = chain.invoke({
        "input": transcription_text,
        "context": vector_store
    })

    llm_answer_status = response['answer']

    data = {
        "file_uploaded_status": file_uploaded_status,
        "transcription_status": transcription_status,
        "language_status": language_status,
        "llm_answer_status": llm_answer_status,
    }

    # Convert the dictionary to a JSON string
    json_response = json.dumps(data)

    return json_response




@app.post("/api/detect_language_and_generate_audio")
async def detect_language_and_generate_audio(text):
    try:
        # Detect Language
        language = DetectLanguage.detect_language(text)
        print("Detected Language:", language)
        # Step 3: Generate audio based on the detected language
        if language == "ca":  # Catalan
            audio_response_path = GenerateAudioOA.generate_audio_with_OpenAI(text, openai_client)
        else:  # Other languages
            audio_response_path = GenerateAudioEL.generate_audio_with_elevenlabs(text)

        data = {
            "audio_file_url": f"/audio/{os.path.basename(audio_response_path)}"
        }

        # Convert the dictionary to a JSON string
        return JSONResponse(content=data)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))







