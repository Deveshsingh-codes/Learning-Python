# Akhbar padhke sunao
from win32com.client import Dispatch

speak = Dispatch("SAPI.spVoice")

speak.Speak("Harry bhai How are you")


def speak(str):
    from win32com.client import Dispatch
    
    speak=Dispatch("SAPI.spVoice")
    
    speak.Speak("str")
    
if __name__ == ' __main__ ':
    speak("Harry bhai How are you")