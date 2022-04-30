from tkinter import *
import datetime
import playsound

def setClock():
    pass

clock = Tk()
clock.title("Nature Clock")
clock.geometry("300x200")


#img = PhotoImage(file="pythontTkinter-adding-image-to-background-.png")
img = PhotoImage(file="bluebell-wood.png")
label = Label(
    clock,
    image=img
)
label.place(x=0, y=0)


#Adding transparent background property
#clock.wm_attributes('-transparentcolor', '#ab23ff')

#Create a Label
#Label(win, text= "This is a New line Text", font= ('Helvetica 18'), bg= '#ab23ff').pack(ipadx= 50, ipady=50, padx= 20)



lbTitle = Label(clock, text="Set the time", fg="white", bg="#003300").place(x=30, y=25)
lbHour = Label(clock, text="Hour", fg="white", bg="#6600ff").place(x=30, y=65)
lbMin = Label(clock, text="Minute", fg="white", bg="#6600ff").place(x=120, y=65)

# The Tkinter StringVar helps to manage the value of a widget such as a Label or Entry more effectively.
# These hour/min variables are set in the text boxes beneath
hour = StringVar()
minute = StringVar()

# Text boxes
hourTime= Entry(clock, textvariable = hour, width = 10).place(x=30, y=90)
minTime= Entry(clock, textvariable = minute, width = 10).place(x=120, y=90)

# Button 
submit = Button(clock, text = "Set", fg="black", width = 10, command = setClock).place(x=30, y=140)

# Compile the previous configuration and run the application
clock.mainloop()


