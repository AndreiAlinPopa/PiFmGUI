import os
from tkinter import *
from tkinter import filedialog


root = Tk()

#setting window size
root.geometry("500x130")


#Frequency text
freq_label = Label(root, text="Frequency (FM): ")
freq_label.place(x=10, y=20)
e = Entry(root, width=8)
e.place(x=150, y=20)


#Audio text
audio_label = Label(root, text="Audio (16-bit wav):")
audio_label.place(x=10, y=55)
#Browse button
def browsefunc():
    global audioFile
    filename = filedialog.askopenfilename()
    audioFile = filename
    pathlabel.config(text=filename)
browsebutton = Button(root, text="Browse", command=browsefunc)
browsebutton.place(x=150, y=50)
pathlabel = Label(root)
pathlabel.place(x=10, y=100)

#Begin broadcast
def start_broadcast():
    frequencyInput = e.get()
    #audioFile already declared
    #print("Frequency = {0}, audio = {1}".format(frequencyInput, audioFile))
    os.system('sudo ' + os.path.dirname(os.path.abspath(__file__)) + '/pi_fm_adv ' + '--freq ' + frequencyInput + ' --audio ' + audioFile)
    

#confirm button
myButton = Button(root, height=3, width=20, text="Start Broadcast", command=start_broadcast)
myButton.place(x=260, y=20)



root.mainloop()
