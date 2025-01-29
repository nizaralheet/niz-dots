# wpgtk dynamic RICE
- all config files that i have customized for every thing im my system are here
<p align="center">
  <img src="https://github.com/user-attachments/assets/6761664b-9d31-4a6d-9085-2d3a6df7e37c" alt="new1" width="45%" style="margin-right: 5px;"/>
  <img src="https://github.com/user-attachments/assets/a52024e8-7c9d-4e22-9764-6df6b6dce2f4" alt="new3" width="45%"/>
</p>

<p align="center">
  <img src="https://github.com/user-attachments/assets/2b959804-6a56-467f-a620-8ed6711e2e8c" alt="new2" width="60%"/>
</p>



## ⚠️ Important notes ⚠️
- QTILE & qtile-extras >= 30.0 
- make sure to make the autostart.sh excutable by running this command ```chmod +x .config/qtile/autostart.sh```

## Dependencies 

-Run this command on arch to install the Dependencies 
for yay :
```
yay -S --needed rofi rofimoji rofi-emoji  pango  python python-cairocffi  alsa-utils python-dbus-next python-dbus-fast python-psutil  qtile-extras  python-pywal wpgtk feh startup-notification  dunst  upower python-attrs python-pulsectl Python-psutil python-pulsectl-asyncio kitty python-pywalfox ttf-iosevka-nerd skippy-xd diodon betterlockscreen  xidlehook plank
```
for paru :
```
paru -S --needed rofi rofimoji rofi-emoji  pango  python python-cairocffi  alsa-utils python-dbus-next python-dbus-fast python-psutil  qtile-extras  python-pywal wpgtk feh startup-notification  dunst  upower python-attrs python-pulsectl Python-psutil python-pulsectl-asyncio kitty python-pywalfox ttf-iosevka-nerd skippy-xd-git diodon betterlockscreen xidlehook plank
```
- For the gtk theme and icons i use flatcolor theme and lina-nord-dark theme they came with [wpgtk here](https://github.com/deviantfero/wpgtk/wiki/Installation) and i use [Promix-icons](https://github.com/nizaralheet/Promix) for rofi 
- For themeing [chromium based browsers](https://github.com/metafates/ChromiumPywal) and firefox [python-pywalfox](https://github.com/Frewacom/pywalfox/) install the extension for every one of them
- the font : ```ttf-iosevka-nerd```
## For installation 
- make sure to backup you config files first
- And make sure that you have all the Dependencies
- then run this :
 ```
 git clone https://github.com/nizaralheet/niz-dots
 cd niz-dots 
 cp -r .config/ ~/.config/
 wpg -ta .config/dunst/dunstrc
 wpg -ta ~/.config/rofi/themes/wpgtk-colors.rasi.bak
 mv -f .config/wpg/config_dunst_dunstrc.base .config/wpg/templates/ 
 mv -f .config/wpg/rofi_themes_wpgtk-colors.rasi.base .config/wpg/templates/
```
## Key Bindings 



| **Key Combination**                      | **Action**                                     |
|------------------------------------------|------------------------------------------------|
| **System Controls**                      |                                                |
| `Print`                                  | 🖼️ Take a screenshot with Flameshot            |
| `mod + L`                                | 🔒 Lock the screen using Betterlockscreen       |
| `XF86MonBrightnessUp`                    | 🔆 Increase brightness                          |
| `XF86MonBrightnessDown`                  | 🔅 Decrease brightness                          |
| `XF86AudioMute`                          | 🔇 Mute volume                                  |
| `XF86AudioLowerVolume`                   | 🔉 Decrease volume                              |
| `XF86AudioRaiseVolume`                   | 🔊 Increase volume                              |
| `mod + Control + R`                      | 🔄 Reload the Qtile config                      |
| `mod + Control + Q`                      | ❌ Shutdown Qtile                               |
| `mod + N`                                | 🔄 Reset all window sizes                       |
| **Application Launchers & Rofi**         |                                                |
| `mod + [`                                | 🖼️ Run a wallpaper select Rofi script           |
| `mod + E`                                | 📂 Open Thunar file manager                     |
| `alt + Tab`                              | 🔄 Open Rofi window switcher                    |
| `mod + ,`                                | 😀 Open Rofi emojis picker                      |
| `mod + V`                                | 📋 Show diodon clipboard manager                 |
| `mod + R`                                | 🚀 Spawn Rofi app launcher                      |
| `mod + B`                                | 🌐 Spawn browser                                |
| **Window Management**                    |                                                |
| `mod + Left`                             | ⬅️ Move focus to the left                       |
| `mod + Right`                            | ➡️ Move focus to the right                      |
| `mod + Down`                             | ⬇️ Move focus downward                          |
| `mod + Up`                               | ⬆️ Move focus upward                            |
| `mod + Space`                            | 🔄 Move window focus to another window          |
| `mod + Shift + Left`                     | ⬅️ Move window to the left                      |
| `mod + Shift + Right`                    | ➡️ Move window to the right                     |
| `mod + Shift + Down`                     | ⬇️ Move window downward                         |
| `mod + Shift + Up`                       | ⬆️ Move window upward                           |
| `mod + Control + Left`                   | ⬅️ Grow window to the left                      |
| `mod + Control + Right`                  | ➡️ Grow window to the right                     |
| `mod + Control + Down`                   | ⬇️ Grow window downward                         |
| `mod + Control + Up`                     | ⬆️ Grow window upward                           |
| `mod + Shift + Return`                   | 🔀 Toggle between split and unsplit sides of stack |
| `mod + Tab`                              | 🔄 Toggle between layouts                       |
| `mod + W`                                | ❌ Kill the focused window                      |
| `mod + F`                                | 🔳 Toggle fullscreen                            |
| `mod + M`                                | 🗜️ Toggle minimize                              |
| `mod + T`                                | 🗂️ Toggle floating                              |
| **Group Management**                     |                                                |
| `mod + PgDn`                             | ⬇️ Jump to the next group                       |
| `mod + PgUp`                             | ⬆️ Jump to the previous group                   |
| `mod + 1-5`                              | 🔢 Switch to group 1-5                          |
| `mod + Shift + 1-5`                      | 🔢 Switch to & move focused window to group 1-5   |

---

