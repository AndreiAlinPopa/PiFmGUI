sudo apt-get install libsndfile1-dev
sudo echo "gpu_freq=250" >> /boot/config.txt
sudo make -C /home/pi/PiFmGUI/src clean
sudo make -C /home/pi/PiFmGUI/src
