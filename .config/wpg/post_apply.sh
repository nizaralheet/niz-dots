#!/bin/sh
# dunst kill it self after that i don't know why so you have to restat it 
dunst &
/home/nizar/.local/share/icons/Promix/scripts/replace_script.sh >/dev/null 2>&1 &
/home/nizar/.local/share/icons/papwal/scripts/replace_script.sh >/dev/null 2>&1 &

# Update icon cache
gtk-update-icon-cache -f -t ~/.local/share/icons/Promix/ >/dev/null 2>&1 &
# in case you have better lockscreen
betterlockscreen -u ~/.config/wpg/.current --fx dimblur >/dev/null 2>&1 &

qtile cmd-obj -o root -f reload_config &

if pgrep -f "pywalfox" >/dev/null; then
    pywalfox update >/dev/null 2>&1 &
fi


notify-send -i ~/.config/wpg/.current "Theme is being applied" "Your new wallpaper and theme are updating in the background." -u low 

