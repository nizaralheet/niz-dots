#!/bin/sh

# Start dunst in the background
nohup dunst &

# Run replacement scripts in parallel
/home/nizar/.local/share/icons/Promix/scripts/replace_script.sh &
/home/nizar/.local/share/icons/papwal/scripts/replace_script.sh &

# Update icon cache in background
gtk-update-icon-cache -f -t ~/.local/share/icons/Promix/ &

# Reload qtile configuration in background
qtile cmd-obj -o root -f reload_config &

# Check and update pywalfox in background if running
if [ "$(ps aux | grep pywalfox | awk '{print $NF}' | grep start)" = "start" ]; then
    pywalfox update &
fi

betterlockscreen -u ~/.config/wpg/.current  --fx dimblur
# Wait for all background processes to complete
wait

# Sequential commands (will run after everything else is done)

notify-send -i ~/.config/wpg/.current "Theme is applied successfully" "wallpaper $(wpg -c) is now set as a background"
