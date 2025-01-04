import pyttsx3 as tts # pyttsx3 is used to convert the text to speech
import speech_recognition as sr # speech_recognition is used to recognize the speech
import webbrowser # webbrowser is used to open the website
import datetime
import pyjokes # pyjokes is used to get jokes

def spText():
    recognizer = sr.Recognizer() 
    with sr.Microphone() as source: 
        print("Listenning...")
        recognizer.adjust_for_ambient_noise(source) 
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        
        try :
            print("Recognizing...")
            data = recognizer.recognize_google(audio, language="en-US") 
            print("You said: " + data)
            return data
        
        except sr.UnknownValueError: 
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return ""
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for speech.")
            return "" 
        
def speechTx(x):
    engine = tts.init()
    voices = engine.getProperty('voices') # getProperty is used to get the properties of the engine
    engine.setProperty('voice', voices[1].id) # setProperty is used to set the properties of the engine
    engine.setProperty('rate', 150) # setProperty is used to set the properties of the engine
    engine.say(x) # say is used to say the text
    engine.runAndWait()
    
if __name__ == '__main__':
    text = spText()
    if text.lower() == "hello":
        print("You said hello")
        speechTx("Hello how can i assist you?")