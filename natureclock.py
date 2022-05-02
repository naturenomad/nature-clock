
#################################################################################
#
# Clock description
#
# This clock currently functions as a wake-up timer only.
# Its function is to provide a dawn chorus sound at the set time.
#
# The clock needs two-digit 24hr format hours and minutes as the textbox inputs.
# 
# The clock is now made into a class to keep its properties and functions tidily together.
# Tbd play the sound in a seperate thread so that it is possible to
# interrupt it with an added stop button.
#
# Author : naturenomad : https://github.com/naturenomad
#
################################################################################


import datetime
import time
from tkinter import *
#from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play
import pyaudio # pyaudio isn't working
from threading import Thread


class NatureClock:

    def __init__(self, clock):
        
        #clock = Frame(master=master)
        #clock.pack(expand=True, fill="both")
        
        clock.title("Nature Clock")
        clock.geometry("300x200")
        
        self.active = False
        
        self.img = PhotoImage(file="bluebell-wood.png")
        self.label = Label(clock, image=self.img)
        self.label.place(x=0, y=0)
        
        self.lbTitle = Label(clock, text="Set wake time", fg="white", bg="#003300").place(x=30, y=25)
        self.lbHour = Label(clock, text="Hour", fg="white", bg="#6600ff").place(x=30, y=65)
        self.lbMin = Label(clock, text="Minute", fg="white", bg="#6600ff").place(x=120, y=65)
        
        # The Tkinter StringVar helps to manage the value of a widget such as a Label or Entry 
        # more effectively.
        # These hour/min variables are set in the text boxes beneath
        self.hour = StringVar()
        self.minute = StringVar()
        
        # Text boxes
        self.hourTime= Entry(clock, textvariable=self.hour, width=10)
        self.hourTime.place(x=30, y=90)
        self.hourTime.focus_set()
        self.minTime= Entry(clock, textvariable=self.minute, width=10)
        self.minTime.place(x=120, y=90)
        
        # Buttons
        self.btStart = Button(clock, text="Set", fg="black", width=10, \
            command=self.setClock).place(x=30, y=140)
        self.btStop = Button(clock, text="Stop", fg="black", width=10, command=self.stopClock)
        self.btStop.place(x=140, y=140)
    
        
    #def scanning(self):
    #    while True :   
    #        song = AudioSegment.from_mp3("98371_1635617-lq_englishcountryside.freesound.org.mp3") 
    #        play(song)
    #        if active == False :
    #            break
    #
    #
    #def setClock(self):
    #    # For a Tkinter.IntVar object - need to call its get method to access the value that it 
    #    # represents   
    #    wakeTime = "{}:{}".format(self.hour.get(), self.minute.get())
    #    while True :
    #        time.sleep(1)
    #        now = datetime.datetime.now().strftime("%H:%M")
    #        if now == wakeTime :
    #            global active 
    #            active = True
    #            t = Thread (target = self.scanning)
    #            t.start()        
    #            
    #            #playsound("98371_1635617-lq_englishcountryside.freesound.org.mp3")
    #            #song = AudioSegment.from_mp3("98371_1635617-lq_englishcountryside.freesound.org.mp3")
    #            #play(song)
    #            #break


    def setClock(self):
        # For a Tkinter.IntVar object - need to call its get method to access the value that it 
        # represents   
        self.active = True
        print(self.active)
        wakeTime = "{}:{}".format(self.hour.get(), self.minute.get())
        #print(wakeTime)
        while True :
            time.sleep(1)
            now = datetime.datetime.now().strftime("%H:%M")
            if now == wakeTime :
                #playsound("98371_1635617-lq_englishcountryside.freesound.org.mp3")
                song = AudioSegment.from_mp3("98371_1635617-lq_englishcountryside.freesound.org.mp3")
                play(song)
                break


    def stopClock(self):
        self.active = False
        print(self.active)

## Compile the previous configuration and run the application
root = Tk()
clock = NatureClock(root)
#root.protocol("WM_DELETE_WINDOW", handle_close)
root.mainloop()






