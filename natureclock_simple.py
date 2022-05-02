
####################################################################################
#
# Clock description
#
# This clock currently functions as a wake-up timer only.
# Its function is to provide a dawn chorus sound at the set time.
#
# The clock needs two-digit 24hr format hours and minutes as the textbox inputs.
# 
# This is the simplest working version of the nature clock. It has some deficiencies
# but works at a basic level.
#
# Author : naturenomad : https://github.com/naturenomad
#
###################################################################################


from tkinter import *
import datetime
import time
#from playsound import playsound

from pydub import AudioSegment
from pydub.playback import play


def setClock():
    # For a Tkinter.IntVar object - need to call its get method to access the value that it 
    # represents   
    wakeTime = "{}:{}".format(hour.get(), minute.get())
    #print(wakeTime)
    while True :
        time.sleep(1)
        now = datetime.datetime.now().strftime("%H:%M")
        if now == wakeTime :
            #playsound("98371_1635617-lq_englishcountryside.freesound.org.mp3")
            song = AudioSegment.from_mp3("98371_1635617-lq_englishcountryside.freesound.org.mp3")
            play(song)
            break


clock = Tk()
clock.title("Nature Clock")
clock.geometry("300x200")

img = PhotoImage(file="bluebell-wood.png")
label = Label(
    clock,
    image=img
)
label.place(x=0, y=0)

lbTitle = Label(clock, text="Set wake time", fg="white", bg="#003300").place(x=30, y=25)
lbHour = Label(clock, text="Hour", fg="white", bg="#6600ff").place(x=30, y=65)
lbMin = Label(clock, text="Minute", fg="white", bg="#6600ff").place(x=120, y=65)

# The Tkinter StringVar helps to manage the value of a widget such as a Label or Entry more effectively.
# These hour/min variables are set in the text boxes beneath
hour = StringVar()
minute = StringVar()

# Text boxes
hourTime= Entry(clock, textvariable=hour, width=10).place(x=30, y=90)
minTime= Entry(clock, textvariable=minute, width=10).place(x=120, y=90)

# Button 
submit = Button(clock, text="Set", fg="black", width=10, command=setClock).place(x=30, y=140)

# Compile the previous configuration and run the application
clock.mainloop()

