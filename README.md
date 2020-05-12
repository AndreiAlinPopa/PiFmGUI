PiFmGUI
========

## What is it?
The first section goes over some of the motivations for PiFmGUI. If you are looking for the direct tutorial, skip ahead to _____

PiFmGUI is an addon pack of scripts designed around the PiFmAdv repository written by Miegl. It features a grand total of 2 Bash files and 1 Python file alongside the original broadcast software. The purpose of PiFmGUI is to allow anybody from a radio novice to a radio enthusiast find a more affordable alternative to a typical HAM or CB radio they'd usually be forced to buy. This is all done to a more user-friendly graphical interface on how to begin broadcasting for someone completely unfamiliar with the Linux Operating environment - after all not everyone's got enough spare time on their hands for 'ol Tux!

Link to the PiFmAdv original repository: https://github.com/miegl/PiFmAdv

## Compatibility

The PiFmGUI repository was designed for use with the any release of the Raspbian OS after August 2015. Furthermore, it has also been tested and confirmed functional with the Raspberry Pi Zero W, Pi Zero, Pi 2 and Pi 3. To ensure the optimal functioning of this repository, please ensure the instructions below are followed using a fresh install of Raspbian OS (installed through NOOBS is fine) on one of the compatible Raspberry Pis.

Insutructions
========
**Equipment:**
- Raspberry Pi (Models Zero, Zero W, 2, and 3 are all acceptable) and appropriate charger
- SD Card (4gb minimum with NOOBS or Raspbian installed / ready to install. It is recommended the SD card is class 10)
- Associated peripherals for the Raspberry Pi desktop environment (i.e. HDMI, MicroHDMI, ethernet, monitor. Whatever is needed to use your raspberry Pi as a desktop computer.)
- ( Dipole equipment goes here )

**Optional Equipment:**
- Soldering iron + solder (Only if you are using a Pi Zero / W with no header pins, and you do not want to solder them on). This is more permanent.
- Portable power bank / battery (To power the Pi Radio while you are on the go)

## Initializing the Raspberry PI
1. Install Raspbian or NOOBS onto an SD card. A detailed guide is avaible here: https://www.raspberrypi.org/documentation/installation/installing-images/

2. Connect to your Raspberry Pi through HDMI and a mouse and keyboard. Alternatively, connect through SSH (tutorial to do that is here: https://www.youtube.com/watch?v=toWBmUsWD6M). Once connected, proceed through installation until you reach the Desktop.

3. Click on the terminal icon near the top left of your task bar. And run these commands one by one until they finish:
```
sudo apt-get install git
sudo git clone https://github.com/AndreiAlinPopa/PiFmGUI.git
cd /home/pi/PiFmGUI/src/
```
Once you have done this, you are ready to run the installer. Type again into console:
`sudo sh radio_setup.sh`
(Future versions of the program will place a shortcut to the PiFmGUI software onto desktop)
4. After waiting a bit, you are now able to finally run your PiFmGUI software. Do this through one of the following commands to access either the UI or GUI software respectively:

`sudo sh PiFmUI`
`sudo python3 PiFmUI`

5. Follow the onscreen promts to get your broadcoast up! To turn off your broadcast at any point, perform an interupt by pressing CTRL and C simultaneously while in terminal

##Building a dipole##
**DISCLAIMER: NEVER BUILD AND OPERATE ANY FORM OF ANTENNAE UNLESS YOUR ARE AUTHORIZED TO DO SO**

(---------------------)

## Unique files
**radio_setup.sh** - Accomplishes 4 tasks: installs libsndfile1-dev, adds 'gpu_freq=250' to /boot/config.txt, executes make clean on the src directory, executes make on the src directory

**PiFmUI.sh** - Echoes & reads the vast majority of commands and options applicable to the PiFmAdv software. It covers most bases, however you must make sure you give a valid response for all inputs, as there is no input validation.

**PiFmGUI.py** - The only Python script, it makes use of the tkinter library to create a GUI. Currently, it is very simplistic, only having a text box in which to input frequency, and a button that activates a file browser. It too has no input validation, but is more defensively programmed than its UI counterpart.


























## Warning and Disclaimer

PiFmAdv is an **experimental** program, designed **only for experimentation**. It is in no way intended to become a personal *media center* or a tool to operate a *radio station*, or even broadcast sound to one's own stereo system.

In most countries, transmitting radio waves without a state-issued licence specific to the transmission modalities (frequency, power, bandwidth, etc.) is **illegal**.

Therefore, always connect a shielded transmission line from the Raspberry Pi directly
to a radio receiver, so as **not** to emit radio waves. Never use an antenna.

Even if you are a licensed amateur radio operator, using PiFmAdv to transmit radio waves on ham frequencies without any filtering between the RaspberryPi and an antenna is most probably illegal because the square-wave carrier is very rich in harmonics, so the bandwidth requirements are likely not met.

I could not be held liable for any misuse of your own Raspberry Pi. Any experiment is made under your own responsibility.
--------
© AndreiAlinPopa
© [Miegl](https://miegl.cz) & [Christophe Jacquet](http://www.jacquet80.eu/) (F8FTK), 2014-2017. Released under the GNU GPL v3.
