import os
import signal
from tkinter import *
from tkinter.ttk import Notebook
from tkinter.ttk import Combobox #
from tkinter import filedialog


root = Tk()

#setting window size
root.geometry("570x300")
root.title('PiFmGUI - Graphical User Interface for PiFmAdv (Made by AndreiAlinPopa)')
currentDir = os.path.dirname(os.path.abspath(__file__))

iconDir = currentDir + '/doc/icon.ico'
root.iconbitmap(str(iconDir))

#tabs
tab_parent = Notebook(root)
tab1 = Frame(tab_parent)
tab2 = Frame(tab_parent)

tab_parent.add(tab1, text="Simple")
tab_parent.add(tab2, text="Advanced")
tab_parent.pack(expand=1, fill='both')

#~~~~~~~~~~~~~~~~~~~~~~tab1 content~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#Frequency text
freqLabel = Label(tab1, text="Frequency (FM): ")
freqLabel.place(x=10, y=20)
freqEntry = Entry(tab1, width=8)
freqEntry.place(x=150, y=20)


#Audio text
audioLabel = Label(tab1, text="Audio (16-bit wav):")
audioLabel.place(x=10, y=55)
#Browse button
def browsefunc():
    global audioFile
    filename = filedialog.askopenfilename()
    audioFile = filename
    pathlabel0.config(text="..."+audioFile[-33:-1]+audioFile[-1], foreground='blue')
browsebutton = Button(tab1, text="Browse", command=browsefunc)
browsebutton.place(x=150, y=50)
pathlabel0 = Label(tab1)
pathlabel0.place(x=10, y=78)

#broadcast station name
broadcastName = Label(tab1, text="Station Name (Limit 8): ")
broadcastName.place(x=10, y=100)
broadcastNameEntry = Entry(tab1, width=66)
broadcastNameEntry.place(x=150, y=100)

#broadcast radiotext
radioText = Label(tab1, text="Radio Text (Limit 64): ")
radioText.place(x=10, y=130)
radioTextEntry = Entry(tab1, width=66)
radioTextEntry.place(x=150, y=130)

#card image for first tab
cardLoc =(currentDir + "/doc/card.png")
card = PhotoImage(file=cardLoc)

panel = Label(tab1, image=card)
panel.place(x=10, y=160)




#Begin broadcast
def start_broadcast():
    """
    Returns a bash command that is piped into terminal
    """

    try:
        if freqEntry.get() and audioFile and broadcastNameEntry.get() and radioTextEntry.get():


            frequencyInput = freqEntry.get()
            #audioFile already declared
            broadcastNameInput = broadcastNameEntry.get()
            radioTextEntryInput = radioTextEntry.get()

            print("Frequency = {0}, audio = {1}, station name = {2}, radiotext = {3}".format(frequencyInput, audioFile, broadcastNameInput, radioTextEntryInput)) #}}}}}}}}
            print('sudo ' + os.path.dirname(os.path.abspath(__file__)) + '/src/pi_fm_adv ' + '--freq ' + frequencyInput + ' --audio ' + audioFile + ' --ps ' + broadcastNameInput + ' --rt ' + radioTextEntryInput)
            os.system('sudo ' + os.path.dirname(os.path.abspath(__file__)) + '/src/pi_fm_adv ' + '--freq ' + frequencyInput + ' --audio ' + audioFile + ' --ps ' + broadcastNameInput + ' --rt ' + radioTextEntryInput)
            
        else:
            print("Ensure you have entered a frequency, audio file, station name, and radiotext")
            return 0
            
    except:
        print("Ensure you have entered a frequency, audio file, station name, and radiotext")
        return 0





#End broadcast
def end_broadcast():
    """
    Sends a system interrupt
    """
    pass
    

#Begin button / end button
startBroadcast = Button(tab1, height=3, width=20, text="Start Broadcast", command=start_broadcast)
startBroadcast.place(x=230, y=20)

stopBroadcast = Button(tab1, height=3, width=20, text="End Broadcast", command=end_broadcast)
stopBroadcast.place(x=400, y=20)

#~~~~~~~~~~~~~~~~~~~~~~tab2 content~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
"""
as a quick note, the adv (tab 2) variables are the same, but instead of capitalization distinguishing words, we have _u_n_d_e_r_s_c_o_r_e_s_
"""

#Frequency text adv
freq_label = Label(tab2, text="Frequency (FM): ")
freq_label.place(x=10, y=20)
freq_entry = Entry(tab2, width=8)
freq_entry.place(x=150, y=20)

#Audio text adv #{{{{{{{{{{{
audioLabel = Label(tab2, text="Audio (16-bit wav):")
audioLabel.place(x=10, y=55)
#Browse button
def browsefunc():
    global audioFile
    filename = filedialog.askopenfilename()
    audioFile = filename
    pathlabel.config(text="..."+audioFile[-33:-1]+audioFile[-1], foreground='blue')
browsebutton = Button(tab2, text="Browse", command=browsefunc)
browsebutton.place(x=150, y=50)
pathlabel = Label(tab2)
pathlabel.place(x=10, y=78)

#broadcast station name adv
broadcast_name = Label(tab2, text="Station Name (Limit 8): ")
broadcast_name.place(x=10, y=100)
broadcast_name_entry = Entry(tab2, width=66)
broadcast_name_entry.place(x=150, y=100)

#broadcast radiotext adv
radio_text = Label(tab2, text="Radio Text (Limit 64): ")
radio_text.place(x=10, y=130)
radio_text_entry = Entry(tab2, width=66)
radio_text_entry.place(x=150, y=130)

#multiselect
'''
gpios = ["4", "20", "32", "34"]

gpio = StringVar()
gpio.set(gpios[0])
gpio_select = OptionMenu(tab2, gpio, *gpios)
gpio_select.place(x=150, y=180)
'''

#frequency deviation
freq_dev = Label(tab2, text="Frequency deviation (kHz): ")
freq_dev.place(x=10, y=170)
freq_dev_entry = Entry(tab2, width=20)
freq_dev_entry.place(x=160, y=170)


#output mpx
broadcast_mpx = Label(tab2, text="Output mpx power: ")
broadcast_mpx.place(x=10, y=190)
broadcast_mpx_entry = Entry(tab2, width=20)
broadcast_mpx_entry.place(x=160, y=190)

#power #need some conversion
broadcast_power = Label(tab2, text="GPIO drv strgth (2-16mA): ")
broadcast_power.place(x=10, y=210)
broadcast_power_entry = Entry(tab2, width=20)
broadcast_power_entry.place(x=160, y=210)

#rds
broadcast_cutoff = Label(tab2, text="Cutoff frequency (<15000): ")
broadcast_cutoff.place(x=10, y=230)
broadcast_cutoff_entry = Entry(tab2, width=20)
broadcast_cutoff_entry.place(x=160, y=230)

#cutoff
broadcast_rds = Label(tab2, text="RDS broadcast switch: ")
broadcast_rds.place(x=290, y=170)
broadcast_rds_entry = Entry(tab2, width=20)
broadcast_rds_entry.place(x=425, y=170)

#ppm
broadcast_ppm = Label(tab2, text="Oscillator error (ppm) ")
broadcast_ppm.place(x=290, y=190)
broadcast_ppm_entry = Entry(tab2, width=20)
broadcast_ppm_entry.place(x=425, y=190)

#gpio
gpio_text = Label(tab2, text="GPIO Pin for transmission: ")
gpio_text.place(x=250, y=10)

g = IntVar()
g.get()
Radiobutton(tab2, text="Pin 4", variable=g, value=4).place(x=250, y=30)
Radiobutton(tab2, text="Pin 20", variable=g, value=20).place(x=325, y=30)
Radiobutton(tab2, text="Pin 32", variable=g, value=32).place(x=400, y=30)
Radiobutton(tab2, text="Pin 34", variable=g, value=34).place(x=475, y=30)

#preemph
preemph_text = Label(tab2, text="Preemph: ")
preemph_text.place(x=250, y=65)


euLoc = currentDir + "\\doc\\eu.png"
usaLoc = currentDir + "\\doc\\usa.png"

eu = PhotoImage(file=euLoc)
usa = PhotoImage(file=usaLoc)
                  
p = StringVar()
p.get()
Radiobutton(tab2, image=eu, variable=p, value='eu').place(x=340, y=65)
Radiobutton(tab2, image=usa, variable=p, value='us').place(x=420, y=65)


#start broadcast
def start_broadcast_adv():
    """
    Returns a bash command that is piped into terminal
    """
    frequency_input = freq_entry.get()
    #audioFile already declared
    broadcast_name_entry_input = broadcast_name_entry.get()
    radio_text_entry_input = radio_text_entry.get()
    freq_dev_entry_input = freq_dev_entry.get()
    broadcast_mpx_entry_input = broadcast_mpx_entry.get()
    broadcast_power_entry_input = broadcast_power_entry.get()
    broadcast_cutoff_entry_input = broadcast_cutoff_entry.get()
    broadcast_rds_entry_input = broadcast_rds_entry.get()
    broadcast_ppm_entry_input = broadcast_ppm_entry.get()
    ####maybe?
    gpio_input = g.get()
    preemph_input = p.get()





    advanced_attributes = (frequency_input, audioFile, broadcast_name_entry_input, radio_text_entry_input, freq_dev_entry_input, broadcast_mpx_entry_input, broadcast_power_entry_input, broadcast_cutoff_entry_input, broadcast_rds_entry_input, broadcast_ppm_entry_input, gpio_input, preemph_input)
    advanced_attributes_prefixes = (' --freq ', ' --audio ', ' --ps ', ' --rt ', ' --dev ', ' --mpx ', ' --power ', ' --cutoff ', ' --rds ', ' --ppm ', ' --gpio ', ' --preemph ')
    terminalParameters = ''
    counter = 0
    
    for value in advanced_attributes:
        try:
            if advanced_attributes[counter]:
                terminalParameters = (terminalParameters + advanced_attributes_prefixes[counter] + str(advanced_attributes[counter]))
        except:
            pass
        finally:
            print(terminalParameters)
            counter += 1

    #output

    os.system('sudo ' + currentDir + '/src/pi_fm_adv ' + terminalParameters)
    print("Frequency = {0}, audio = {1}, station name = {2}, radiotext = {3}, frequency deviation = {4}, mpx = {5}, power = {6}, cutoff = {7}, rds = {8}, ppm = {9}, gpio = {10}, preemph = {11}".format(frequency_input, audioFile, broadcast_name_entry_input, radio_text_entry_input, freq_dev_entry_input, broadcast_mpx_entry_input, broadcast_power_entry_input, broadcast_cutoff_entry_input, broadcast_rds_entry_input, broadcast_ppm_entry_input, gpio_input, preemph_input)) #}}}}}}}}



#End broadcast
def end_broadcast():
    """
    Sends a system interrupt
    """
    pass
    

#Begin button / end button
startBroadcast = Button(tab2, height=2, width=14, text="Start Broadcast", command=start_broadcast_adv)
startBroadcast.place(x=300, y=220)

stopBroadcast = Button(tab2, height=2, width=14, text="End Broadcast", command=end_broadcast)
stopBroadcast.place(x=440, y=220)





root.mainloop()
























