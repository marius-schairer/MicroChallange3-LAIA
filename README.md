# LAIA-Raspi
This code is responsible for the server to which we send api calls from the raspberry pi and include our databases and process them with the ai. 
the main code consists of two blocks. building vector store and processing audio message. the audio processing part is responsible for transcribing the api calls from the raspberry pi, passing the transcript to the modifying prompt to respond with gpt as a neighborhood prompted including our data. 
The Vector store build part is responsible for updating from our local database files and collected new coming data from our form
<img width="4065" alt="Planning" src="https://github.com/marius-schairer/MicroChallange3-LAIA/assets/147055411/c57d8682-4dd6-48fc-bd51-887bae34ea0c">

## Requirement: OpenAI KEY

## Vector Store
<img width="789" alt="Screenshot 2024-06-16 at 22 18 13" src="https://github.com/marius-schairer/MicroChallange3-LAIA/assets/147055411/b3c5b2d9-bd98-4394-9fda-1ca7cc8b715e">

## Input Processing

<img width="822" alt="Screenshot 2024-06-16 at 22 19 21" src="https://github.com/marius-schairer/MicroChallange3-LAIA/assets/147055411/450110bd-7679-4fff-84a7-03695ffe8ad6">



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
