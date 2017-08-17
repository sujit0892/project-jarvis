import pyttsx3
from wit import Wit

class nlp:
    def __init__(self):
        self.client = Wit("KPFGFBZVFM4L7OJLRPU274SOCABPJQTD")
        self.engine=pyttsx3.init()
   
    def speech_to_text(self):
        resp=None
        with open('output.wav', 'rb') as f:
             resp = self.client.speech(f, None, {'Content-Type': 'audio/wav'})
        print('Yay, got Wit.ai response: ' + str(resp['_text']))
        return str(resp['_text']))
