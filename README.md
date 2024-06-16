# LAIA-Raspi
This code is responsible for the server to which we send api calls from the raspberry pi and include our databases and process them with the ai. 
the main code consists of two blocks. building vector store and processing audio message. the audio processing part is responsible for transcribing the api calls from the raspberry pi, passing the transcript to the modifying prompt to respond with gpt as a neighborhood prompted including our data. 
The Vector store build part is responsible for updating from our local database files and collected new coming data from our form
<img width="4065" alt="Planning" src="https://github.com/marius-schairer/MicroChallange3-LAIA/assets/147055411/c57d8682-4dd6-48fc-bd51-887bae34ea0c">
