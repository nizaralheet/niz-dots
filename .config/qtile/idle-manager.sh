#!/bin/bash

xidlehook --not-when-fullscreen  --not-when-audio --timer 120  "./.config/qtile/dec.sh"  "./.config/qtile/inc.sh"  &


xidlehook\
  --not-when-fullscreen \
  --not-when-audio \
  --timer 400 \
    'xset dpms force off' \
    'xset dpms force on' \
  --timer 400 \
    'xkb-switch -s us ; betterlockscreen -l dimblur' \
    '' \
  --timer 400 \
    'systemctl suspend' \
    ''

