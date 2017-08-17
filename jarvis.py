import pyaudio
import wave
from tkinter import *
import threading
from nlp import nlp

CHUNK=1024
FORMAT=pyaudio.paInt16
RATE=44100
CHANNELS=2
OUTPUT="output.wav"



class Jarvis:
    def __init__(self,root):
        self.isRecording=False
        self.button=Button(root,text="say")
        self.button.bind("<Button-1>", self.startrecording)
        self.button.bind("<ButtonRelease-1>", self.stoprecording)
        self.entry=Entry(width=50)
        self.label=Label(root,width=55,height=40,background="white",text='',anchor=NW)
        self.entry.grid(column=0,row=0,columnspan=3)
        self.button.grid(column=4,row=0)
        self.label.grid(row=1,column=0,columnspan=5)
       
        
    def startrecording(self,event):
        self.isRecording=True
        t=threading.Thread(target=self.record)
        t.start()
 
    def stoprecording(self,event):
        self.isRecording=False
        print("analyzing...")


        

    def record(self):
        print("")
        p=pyaudio.PyAudio()
        stream=p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)
        frames=[]

        while self.isRecording:
              data=stream.read(CHUNK)
              frames.append(data)
        stream.stop_stream()
        stream.close()
        p.terminate()
        wf = wave.open(OUTPUT, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        text1=nlp().speech_to_text()
        text=self.label.cget("text")+text1
        self.label.configure(text=text)
              

root=Tk()
Jarvis(root)
root.mainloop()
        
