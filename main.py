import subprocess
import wolframalpha
import pyttsx3
import tkinter as tk
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen

app_id = 'XGRRX3-7VQ99UGK9Q'
client = wolframalpha.Client(app_id)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    today = datetime.datetime.today().strftime('%A')

    if hour >= 0 and hour < 12:
        speak(f'good morning, have a great {today}.')
    elif hour >= 12 and hour < 4:
        speak(f'good afternoon, have a great {today}.')
    else:
        speak(f'good evening, have a great {today}.')

    speak("you can call me Cat")
    speak("how can i help you today?")


def username():
    speak("what can i call you?")
    uname = takeCommand()
    speak(f'hello, {uname}')
    print(f'your username is identified as {uname}')
    speak('tell me a keyword')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening through your input channel...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("detecting what you said")
        query = r.recognize_google(audio, language='en-in')
        print(f'you said:                 "{query}"')
    except Exception as e:
        print(e)
        print("I didn't understand. can you try again?")
        return None
    return query.lower()


def query_wolfram_alpha(query):
    print(query)
    try:
        result = client.query(query)
        return next(result.results).text
    except Exception as e:
        return f"Error: {e}"

class ChatApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Chat App")
        self.master.geometry("100x300")

        self.label = tk.Label(master, text="Welcome to Chat App!")
        self.label.pack()

        self.button = tk.Button(master, text="Start Chatting", command=self.start_chat)
        self.button.pack()

    def start_chat(self):
        self.label.config(text="Chat started...")
        wishMe()
        username()
        self.listen_for_commands()

    def listen_for_commands(self):
        while True:
            query = takeCommand()
            if query == 'exit':
                speak("Goodbye!")
                self.label.config(text="Chat ended.")
                break
            elif query is None:
                speak("Didn't hear anything, exiting")
                self.label.config(text="Chat ended.")
                break
            else:
                response = query_wolfram_alpha(query)
                speak(response)

if __name__ == '__main__':
    root = tk.Tk()
    app = ChatApp(root)
    root.mainloop()





