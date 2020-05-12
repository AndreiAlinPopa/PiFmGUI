#!/bin/sh

echo "Welcome to the PiFmAdv Input Utility -  made by AndreiAlinPopa, powered by miegl"
sleep 3

echo "Frequency: "
read frequency
frequency="--freq ${frequency} "

echo "Audio (Audio must be 16-bit WAV) - To find path, right-click file, and click Copy Path(s): "
read audio
audio="--audio ${audio} "

echo "PI-Code of RDS BROADCAST (DEFAULT = FFFF): "
read PICode
PICode="--pi ${PICode} "

echo "Station name (8 character limit): "
read stationName
stationName="--ps ${stationName} "

echo "Radiotext (64 character limit): "
read radioText
radioText="--rt ${radioText} "

echo "Program type (0 - 31): "
read programType
programType="--pty ${programType} "

echo "Traffic information (DEFAULT = 0): "
read trafficInfo
trafficInfo="--tp ${trafficInfo} "

echo "Frequency deviation (in KHz) (DEFAULT = 25.0): "
read freqDev
freqDev="--dev ${freqDev} "

echo "Output mpx power (DEFAULT = 30): "
read mpx
mpx="--mpx ${mpx} "

echo "Drive strength of GPIO pads (0 = 2mA... 7 = 16mA)(Default 7): "
read power
power="--power ${power} "

echo "GPIO pin used for transmitting (4, 20, 32, 34. Default 4): "
read GPIO
GPIO="--gpio ${GPIO} "

echo "Cutoff Frequency (in Hz, used by PI's lowpass filter. Must be under 15000): "
read cutoff
cutoff="--cutoff ${cutoff} "

echo "Preemph (Europe choose 'eu', US chose 'us'): "
read preemph
preemph="--preemph ${preemph} "

echo "RDS broadcast switch: "
read RDS
RDS="--rds ${RDS} "



DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
echo ${DIR}/pi_fm_adv ${frequency}${audio}${PICode}${stationName}${radioText}${programType}${trafficInfo}${freqDev}${mpx}${power}${GPIO}${cutoff}${preemph}${RDS}
