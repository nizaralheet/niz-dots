#!/bin/bash

case "$DUNST_URGENCY" in
    LOW)
        paplay /usr/share/sounds/ocean/stereo/message-new-instant.oga &
        ;;
    NORMAL)
        paplay /usr/share/sounds/ocean/stereo/dialog-information.oga &
        ;;
    CRITICAL)
        paplay /usr/share/sounds/ocean/stereo/dialog-error.oga &
        ;;
esac
