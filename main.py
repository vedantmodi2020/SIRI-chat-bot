import speech_recognition as sr
import os
import gtts
from playsound import playsound
from datetime import datetime
import openai
import random
import numpy as np
from spotify import  play_song,pause_song,get_artist_top_tracks
from open import open_app
from notion import  NotionClient
from Constants import  apiKey
import keyboard
import time

chatStr = ""
# https://youtu.be/Z3ZAJoi4x6Q
def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apiKey
    chatStr += f"Vedant: {query}\n Friday: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

def ai(prompt):
    openai.api_key = apiKey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

def say(text):
    try:
        tts = gtts.gTTS(text)
        tempfile = "./temp.mp3"
        tts.save(tempfile)
        playsound(tempfile)
        os.remove(tempfile)
    except AssertionError:
        print("could not play sound")

token = ""
database_id = ""

client = NotionClient(token, database_id)

def takeCommand():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source,timeout=2)
            query = r.recognize_google(audio,language="en-in")
            print(f"User said: {query}")
            return query

    except Exception as e:
        return f"Some error occured. Sorry {e}"



if __name__ == '__main__':
   say('Hello How Can I help you Today')
   while True:
       print("listening...")
       command = takeCommand()
       print(command)
       if not command:  # If no speech is detected, continue to listen for the next command
           continue

       if "play" in command.lower():
           wait_time = play_song(command.replace("play", "").strip())
           print("Currently the song is playing to stop the song please press 'sapce key' ")
           start_time = time.time()
           while time.time() - start_time < wait_time / 1000:
               if keyboard.is_pressed('space'):
                   pause_song()
                   print("Song stopped.")
                   break

       elif "pause" in command:
           print("Pausing the song")
           pause_song()


       elif "show me" in command:
           result = get_artist_top_tracks(command.replace("show me songs for", "").strip())
           say("These are some of the most famous tracks for the given artist")
           print(result)

       elif "open" in command:
           open_app(command.replace("open", "").strip().replace(" ", "").lower())

       elif "write" in command:
           if command:
               now = datetime.now().astimezone().isoformat()
               res = client.create_page(command, now, status="Active")
               if res.status_code == 200:
                   say("Note Saved successfully")

       elif "Using artificial intelligence".lower() in command.lower():
           ai(prompt=command)

       elif "friday Quit".lower() in command.lower():
           exit()

       elif "reset chat".lower() in command.lower():
           chatStr = ""

       else:
           print("Chatting...")
           chat(command)

