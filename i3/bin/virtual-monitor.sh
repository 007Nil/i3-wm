#!/usr/bin/bash

if [ $1 == "on" ]; then
screen1="1280x810_60.00"
xrandr --newmode "1280x810_60.00"   84.50  1280 1352 1480 1680  810 813 823 841 -hsync +vsync
xrandr --addmode VIRTUAL1 $screen1
sleep 2s

echo "added $screen1 resulation to VIRTUAL1"

xrandr --output VIRTUAL1 --mode $screen1 --left-of eDP1
sleep 2s

echo "All done!!!"
echo "Enjoy your virtual screen"

xrandr
fi

if  [ $1 == "off" ]; then
	xrandr  --output VIRTUAL1 --off
fi
