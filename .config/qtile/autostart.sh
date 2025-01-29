#!/bin/bash
picom &
#wal -R ;
nohup skippy-xd --start-daemon &
nohup dunst &
nohup udiskie &
firewall-applet &
nohup /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
diodon &
rclone mount niz: /home/nizar/google-drive/   --vfs-cache-mode full \
            --vfs-read-chunk-size 32M \
            --vfs-read-chunk-size-limit 2G \
            --buffer-size 256M \
            --drive-chunk-size 32M \
            --dir-cache-time 96h \
            --timeout 1h \
            --vfs-cache-max-size 10G \
            --vfs-cache-max-age 336h \
            --attr-timeout 1s \
            --drive-pacer-min-sleep 1ms \
            --drive-pacer-burst 5000 \
            --transfers 32 \
            --checkers 16 \
            --drive-acknowledge-abuse \
            --drive-server-side-across-configs \
            --fast-list \
            --daemon ;
kdeconnect-indicator &
plank &
./.config/qtile/idle-manager.sh &
#xinput set-prop 9 317 0 &&
