# import speech_recognition as sr
# import pyttsx3

# r=sr.Recognizer()
# p=pyttsx3.init()

# while True:
#     print("speak...")
#     try:
#         with sr.Microphone() as mic:
#             r.adjust_for_ambient_noise(mic,duration=0.2)
#             audio = r.listen(mic)
#             print(audio)
#             text = r.recognize_google(audio)
#             text= text.lower()
            
#             print(f"Recognized : {text}")
            
#             p.say(text)
#             p.runAndWait()
        
#     except sr.UnknownValueError():
#         r= sr.Recognizer()
#         continue

import tkinter as tk
from tkinter import scrolledtext
import threading
import speech_recognition as sr
import pyttsx3

# Function to handle speech recognition
def recognize_speech():
    r = sr.Recognizer()
    p = pyttsx3.init()
    
    with sr.Microphone() as mic:
        r.adjust_for_ambient_noise(mic, duration=0.2)
        audio_text.insert(tk.END, "Listening...\n")
        audio_text.see(tk.END)  # Scroll to the bottom
        audio = r.listen(mic)
        
        try:
            text = r.recognize_google(audio)
            text = text.lower()
            audio_text.insert(tk.END, f"Recognized: {text}\n")
            audio_text.see(tk.END)  # Scroll to the bottom
            
            p.say(text)
            p.runAndWait()
        except sr.UnknownValueError:
            audio_text.insert(tk.END, "Sorry, I did not get that.\n")
            audio_text.see(tk.END)  # Scroll to the bottom
        except sr.RequestError as e:
            audio_text.insert(tk.END, f"Could not request results; {e}\n")
            audio_text.see(tk.END)

def start_listening():
    # Using a thread to prevent the GUI from freezing
    threading.Thread(target=recognize_speech).start()

# Setting up the GUI
root = tk.Tk()
root.title("Speech Recognition")

frame = tk.Frame(root)
frame.pack(pady=20)

# Adding a scrolled text area where speech recognition results will appear
audio_text = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=50, height=10)
audio_text.pack(pady=20)

# Button to start speech recognition
listen_button = tk.Button(frame, text="Start Listening", command=start_listening)
listen_button.pack(pady=20)

root.mainloop()


# import tkinter as tk
# from tkinter import scrolledtext
# import threading
# import speech_recognition as sr
# import pyttsx3

# # Initialize recognizer
# r = sr.Recognizer()

# # Global flag to control the recording state
# stop_listening = False

# def recognize_speech():
#     global stop_listening
#     p = pyttsx3.init()
#     with sr.Microphone() as mic:
#         r.adjust_for_ambient_noise(mic, duration=0.2)
#         audio_text.insert(tk.END, "Listening...\n")
#         audio_text.see(tk.END)  # Scroll to the bottom

#         # Listen in a non-blocking manner, checking stop_listening flag
#         while not stop_listening:
#             try:
#                 audio = r.listen(mic, phrase_time_limit=5)
#                 text = r.recognize_google(audio)
#                 text = text.lower()
#                 audio_text.insert(tk.END, f"Recognized: {text}\n")
#                 audio_text.see(tk.END)  # Scroll to the bottom
                
#                 p.say(text)
#                 p.runAndWait()
#             except sr.UnknownValueError:
#                 audio_text.insert(tk.END, "Sorry, I did not get that. Please speak again.\n")
#                 audio_text.see(tk.END)  # Scroll to the bottom
#                 break  # Break the loop if nothing is recognized
#             except sr.RequestError as e:
#                 audio_text.insert(tk.END, f"Could not request results; {e}\n")
#                 audio_text.see(tk.END)
#                 break  # Break the loop on request errors
#             except Exception as e:
#                 audio_text.insert(tk.END, f"An error occurred: {e}\n")
#                 audio_text.see(tk.END)
#                 break  # Break the loop on any other exceptions

# def start_listening():
#     global stop_listening
#     stop_listening = False
#     threading.Thread(target=recognize_speech).start()

# def stop_listening_command():
#     global stop_listening
#     stop_listening = True
#     audio_text.insert(tk.END, "Stopped listening.\n")
#     audio_text.see(tk.END)

# # Setting up the GUI
# root = tk.Tk()
# root.title("Speech Recognition")

# frame = tk.Frame(root)
# frame.pack(pady=20)

# # Adding a scrolled text area where speech recognition results will appear
# audio_text = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=50, height=10)
# audio_text.pack(pady=20)

# # Button to start speech recognition
# listen_button = tk.Button(frame, text="Start Listening", command=start_listening)
# listen_button.pack(side=tk.LEFT, padx=(0, 10))

# # Button to stop speech recognition
# stop_button = tk.Button(frame, text="Stop Listening", command=stop_listening_command)
# stop_button.pack(side=tk.RIGHT, padx=(10, 0))

# root.mainloop()
