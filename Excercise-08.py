# Akhbar padhke sunao
from win32com.client import Dispatch

speak = Dispatch("SAPI.spVoice")

speak.Speak("Harry bhai How are you")