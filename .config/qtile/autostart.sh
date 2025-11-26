#!/bin/bash
picom &
wal -R ;
nohup skippy-xd --start-daemon > /dev/null 2>&1 &
nohup dunst > /dev/null 2>&1 &
#nohup udiskie > /dev/null 2>&1 &
#firewall-applet &
#nohup /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 > /dev/null 2>&1 &
diodon &
#libinput-gestures-setup start;
#kdeconnect-indicator &
