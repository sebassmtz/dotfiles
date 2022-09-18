#!/bin/sh

#Settings english keyboard
setxkbmap us &

#Settings resolution
#Home Monitor
xrandr --output eDP --mode 1366x768 --pos 1920x312 --rotate normal --output HDMI-A-0 --primary --mode 1920x1080 --pos 0x0 --rotate normal &

# System Icons

udiskie -t &

nm-applet &

cbatticon -u 5 &

#WallPaper
