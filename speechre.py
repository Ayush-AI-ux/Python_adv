import speech_recognition as sr
import pyttsx3
import gtts
import playsound as ps

r=sr.Recognizer()
def save_text():
    while(1):
        try:
            with sr.Microphone() as source2:
                #prepare recognizer to receive input
                r.adjust_for_ambient_noise(source2, duration= 0)
                #listens for the user's input
                audio2=r.listen(source2)
                #using google to recognize audio
                text=r.recognize_google(audio2)

                return text


        except sr.RequestError as e:
            print("could not request results; {0}". format(e))

        except sr.UnknownValueError:
            print("unknown error occurred")


def output(text):
    print(text)

def play(t):
    # t=input("enter ")
    sound=gtts.gTTS(t, lang='en')
    sound.save("play.mp3")
    ps.playsound("play.mp3")

while(1):
    a=int(input())
    if a==1:
        text=save_text()
        output(text)
        print("Wrote text")
    elif a==2:
        play(text)