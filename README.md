# LAIA-Raspi
This code is responsible for the server to which we send api calls from the raspberry pi and include our databases and process them with the ai. 
the main code consists of two blocks. building vector store and processing audio message. the audio processing part is responsible for transcribing the api calls from the raspberry pi, passing the transcript to the modifying prompt to respond with gpt as a neighborhood prompted including our data. 
The Vector store build part is responsible for updating from our local database files and collected new coming data from our form
<img width="4065" alt="Planning" src="https://github.com/marius-schairer/MicroChallange3-LAIA/assets/147055411/c57d8682-4dd6-48fc-bd51-887bae34ea0c">

## Requirement: OpenAI KEY

## Vector Store
<img width="895" alt="Screenshot 2024-06-16 at 22 21 32" src="https://github.com/marius-schairer/MicroChallange3-LAIA/assets/147055411/eaf1d2ca-1ced-4ab0-be22-0933c9bd493f">

## Input Processing
<img width="840" alt="Screenshot 2024-06-16 at 22 22 24" src="https://github.com/marius-schairer/MicroChallange3-LAIA/assets/147055411/4e7088a2-7ddf-4a6f-ab10-447666425a8c">




## Challenges we had:

### Formatting a file
We managed to send an audio file from the raspberry pi to the server but not yet send an audio file back. 

### Merging database and CSV
Langchain offers a function that made it possible to merge multiple data sources into one vectorstore.

### Handle data volume
If the vectorstore becomes too full, the prompt becomes too long to be processed.

## Next steps:
1. Add similarity search to be able to trade more data volume
2. Generate audio response in the server
3. Integrate input analysis to be able to switch between input and uotput and handle seperately

## Inspiring Sources:

[Langchain Tutorial Series ->](https://www.youtube.com/watch?v=ekpnVh-l3YA&list=PL4HikwTaYE0GEs7lvlYJQcvKhq0QZGRVn)

[Langchain Docs ->](https://python.langchain.com/v0.2/docs/introduction/)
[Supabase Docs ->](https://supabase.com/docs/reference/python/initializing)
