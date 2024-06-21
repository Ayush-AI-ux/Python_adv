# import speech_recognition as sr
# import webbrowser as web

# # path="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"
# path = "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Edge.lnk"
# r=sr.Recognizer()

# with sr.Microphone() as mic:
#     r.adjust_for_ambient_noise(mic)
#     audio=r.listen(mic)
    
#     try:
#         text=r.recognize_google(audio)
#         print("URl :-", text)
        
#         web.get(path).open(text)
        
#     except Exception as e:
#         print(str(e))


import os
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as mic:
    r.adjust_for_ambient_noise(mic)
    audio = r.listen(mic)

    try:
        text = r.recognize_google(audio)
        print("URL:", text)
        
        # Use the Microsoft Edge protocol to open the URL
        # Ensure the URL starts with http:// or https://
        if not text.startswith(('http://', 'https://')):
            text = 'http://' + text
        command = f"start microsoft-edge:{text}"
        os.system(command)
        
    except Exception as e:
        print(str(e))
