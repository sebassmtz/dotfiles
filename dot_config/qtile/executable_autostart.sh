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
xrandr --output eDP1 --mode 1920x1080 --pos 0x0 --rotate normal &
