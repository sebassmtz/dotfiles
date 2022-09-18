#!/bin/sh

#Settings english keyboard
setxkbmap us &

# System Icons

udiskie -t &

nm-applet &

cbatticon -u 5 &

blueman-applet &

#WallPaper

feh --bg-scale ~/Pictures/scenary01.jpg &

#Home Monitor
#Settings resolution
xrandr --output eDP-1 --mode 1366x768 --pos 1920x312 --rotate normal --output HDMI-1 --primary --mode 1920x1080 --pos 0x0 --rotate normal &
