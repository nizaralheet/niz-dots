#!/bin/bash
picom &
#wal -R ;
nohup skippy-xd --start-daemon &
nohup dunst &
firewall-applet &
diodon &
plank &
./.config/qtile/idle-manager.sh &
#xinput set-prop 9 317 0 &&
