import openai
import requests
import os
import sys
from dotenv import load_dotenv
import json
from deepgram import (
    DeepgramClient,
    PrerecordedOptions,
    FileSource,
    SpeakOptions,
)
from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip

load_dotenv()
AUDIO_FILE = sys.argv[1]
API_KEY = os.getenv("DG_API_KEY")

def main():

    azure_openai_key = os.getenv("azure_openai_key") # Replace with your actual key
    azure_openai_endpoint = os.getenv("azure_openai_endpoint")  # Correct the endpoint URL
    
    # Check if both the key and endpoint are provided
    if azure_openai_key and azure_openai_endpoint and API_KEY and AUDIO_FILE:
        try:
            deepgram = DeepgramClient(API_KEY)

            with open(AUDIO_FILE, "rb") as file:
                buffer_data = file.read()

            payload: FileSource = {
                "buffer": buffer_data,
            }

            #STEP 2: Configure Deepgram options for audio analysis
            options = PrerecordedOptions(
                model="nova-2",
                smart_format=True,
            )

            # STEP 3: Call the transcribe_file method with the text payload and options
            response = deepgram.listen.prerecorded.v("1").transcribe_file(payload, options)
            t_data=response['results']['channels'][0]['alternatives'][0]['paragraphs']['paragraphs']
            sentences_array=[]
            start_time=[]
            end_time=[]
            for i in t_data:
                for j in i['sentences']:
                    sentences_array.append(j['text'])
                    start_time.append(j['start'])
                    end_time.append(j['end'])
            
            # Setting up headers for the API request
            headers = {
                "Content-Type": "application/json",  # Specifies that we are sending JSON data
                "api-key": azure_openai_key  # The API key for authentication
            }
            
            # # Data to be sent to Azure OpenAI
            data = {
                        "messages": [
                            {
                                "role": "user",
                                "content": '''You are a language correction assistant. Your task is to correct grammatical mistakes and remove filler words (such as "um", "hmm", "like", etc.) from the given list of sentences while ensuring that the length of each sentence and the number of words remain unchanged.''',
                            },
                           
                            {
                                "role": "user",
                                "content": '''Please return the corrected sentences in the same concated formate with "#" like if there are two sencences sentence1 and sentence2 then after upgradetion return like sentences1#sentence2 Note: Number of sentences shouldn't be change.'''
                            },
                            {
                                "role": "user",
                                "content": f"Here is the input: {sentences_array}. Please correct the sentences according to the instructions."
                            }
                        ],  # The message we want the model to respond to
                        "max_tokens": 1500  # Adjusted response length limit to allow for more detailed corrections
                    }

            ## Making the POST request to the Azure OpenAI endpoint
            response_AI = requests.post(azure_openai_endpoint, headers=headers, json=data)
            if response_AI.status_code == 200:
                result = response_AI.json()  # Parse the JSON response
                updated_sentences_array=result["choices"][0]["message"]["content"].strip().split('#')  # Display the response content from the AI
                chunk= [{"text": item} for item in updated_sentences_array]
                
                #  Convert TEXT TO AUDIO HERE
                optionst_v = SpeakOptions(
                        model="aura-asteria-en",
                        encoding="linear16",
                        container="wav"
                    )
                video = VideoFileClip(AUDIO_FILE)
                video = video.set_audio(None)
                arr_audio=[]
                for i in range(len(chunk)):
                    SPEAK_OPTIONS = chunk[i]
                    filename = f"audio/output{i}.wav"
                    s_tiem= start_time[i]
                    response = deepgram.speak.v("1").save(filename, SPEAK_OPTIONS, optionst_v)
                    arr_audio.append(AudioFileClip(filename).set_start(s_tiem))
                final_audio = CompositeAudioClip(arr_audio)
                final_video = video.set_audio(final_audio)
                final_video.write_videofile("output_video.mp4", codec="libx264", audio_codec="aac")
               
            else:
                # Handle errors if the request was not successful
                print(f"Failed to connect or retrieve response: {response.status_code} - {response.text}")
        except Exception as e:
            # Handle any exceptions that occur during the request
            print(f"ERRORR: Failed to connect or retrieve response: {str(e)}")
    else:
        # Warn the user if key or endpoint is missing
        print("Please enter all the required details.")
    

if __name__ == "__main__":
    main()
