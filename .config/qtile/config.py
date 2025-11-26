import os
import time
import subprocess
import qtile_extras.hook
from libqtile import bar, qtile, hook
from qtile_extras import widget, layout
from qtile_extras.widget.decorations import RectDecoration
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import send_notification
from functions import calendar, show_power_menu,  show_power_profile
from qtile_menu import qtile_menu
import colors


Btop = {"Button1": lazy.spawn("kitty -e btop")}

mod = "mod4"
alt = "mod1"
terminal = "kitty"
home = os.path.expanduser("~")

##############################
# _                 _        #
# | |__   ___   ___ | | _____ #
# | '_ \ / _ \ / _ \| |/ / __|#
# | | | | (_) | (_) |   <\__ \#
# |_| |_|\___/ \___/|_|\_\___/#


@hook.subscribe.startup
def run_every_startup():  # this for reload_config
    send_notification("Qtile", "config is loaded successfully.")


@hook.subscribe.startup_complete
@qtile_extras.hook.subscribe.up_battery_low
def battery_low(battery_name):
    send_notification("Power HQ", "Battery is running low.")


@qtile_extras.hook.subscribe.up_battery_critical
def battery_critical(battery_name):
    send_notification(
        "Power HQ", "Battery is critically low. Plug in the power cable.")


@qtile_extras.hook.subscribe.up_power_connected
def plugged_in():
    send_notification(
        "Power HQ", "The power have been pluged in , Charging Up")
    qtile.spawn("ffplay -nodisp -autoexit ~/.config/qtile/assets/power-plug.oga")


@qtile_extras.hook.subscribe.up_power_disconnected
def unplugged():
    send_notification(
        "Power HQ", "The power cable is disconnected , Discharging")
    qtile.spawn(
        "ffplay -nodisp -autoexit ~/.config/qtile/assets/power-unplug.oga")


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.Popen([home])
    qtile.spawn("bash -c 'sleep 1 && notify-send \"Welcome\" \"What are you gonna do today?\"'")
    qtile.spawn("bach -c  'paplay ~/.config/qtile/assets/desktop-login.oga'")


if "resume_hook_registered" not in globals():

    @hook.subscribe.resume
    def wakeup():
        time.sleep(3)
        qtile.spawn("notify-send 'Welcome Back!' 'The system successfully awakened from sleep'")

    resume_hook_registered = True


def run_script(qtile):
    an = os.path.expanduser("~/.config/rofi/theme-rofi.sh")
    subprocess.call(["/bin/bash", an])


##########################################################
# _  __            ____  _           _ _                 #
# | |/ /           |  _ \(_)         | (_)                #
# | ' / ___ _   _  | |_) |_ _ __   __| |_ _ __   __ _ ___ #
# |  < / _ | | | | |  _ <| | '_ \ / _` | | '_ \ / _` / __|#
# | . |  __| |_| | | |_) | | | | | (_| | | | | | (_| \__ \#
# |_|\_\___|\__, | |____/|_|_| |_|\__,_|_|_| |_|\__, |___/#
#           __/ |                               __/ |    #
#          |___/                               |___/     #
##########################################################


keys = [

    Key([mod, "shift"], "e", lazy.spawn("kitty -e nvim"), desc="spawn neovim"),
    Key(
        ["control", "shift"],
        33,
        lazy.spawn("firefox --private-window"),
        desc="open firefox private-window",
    ),
    Key(
        [], "Print", lazy.spawn("flameshot gui"), desc="take a screenshot by flameshot"
    ),
    # Changed lock screen to mod+alt+l for better ergonomics and meaning
    Key(
        [mod, alt],
        "l",
        lazy.spawn("betterlockscreen -l dimblur"),
        desc="lock the screen using betterlockscreen",
    ),
    Key(
        [mod], 34, lazy.function(run_script), desc="run a wallpaper select rofi script"
    ),
    # i have the keys binded to the keycode so isntall xorg-xev to see all keys
    Key([mod], "e", lazy.spawn("thunar"), desc="mod+e open thunar"),
    Key(
        [alt],
        "Tab",
        lazy.spawn("skippy-xd --expose --next"),
        desc="alt+tab opens rofi window",
    ),
    Key(
        [mod],
        "comma",
        lazy.spawn(
            "rofi -config ~/.config/rofi/emoji.rasi -show emoji -modi emoji -emoji-format '{emoji}'"
        ),
        desc="mod+comma opens rofi emojis",
    ),
    # that is for my clipboard add yours
    Key(
        [mod],
        "v",  # 55,
        lazy.spawn("/usr/bin/diodon"),
        desc="mod+v shows copyq clipboard",
    ),
    # here is the brightness control
    Key(
        [mod],
        "XF86AudioRaiseVolume",
        lazy.spawn("brightnessctl set +5%"),
        desc="raise the brighteness level",
    ),
    Key(
        [mod],
        "XF86AudioLowerVolume",
        lazy.spawn("brightnessctl set 5%-"),
        desc="lower the brighteness level",
    ),
    Key(
        [],
        "XF86MonBrightnessUp",
        lazy.spawn("brightnessctl set +5%"),
        desc="raise the brighteness level",
    ),
    Key(
        [],
        "XF86MonBrightnessDown",
        lazy.spawn("brightnessctl set 5%-"),
        desc="lower the brighteness level",
    ),
    # audion control
    Key([], "XF86AudioMute", lazy.spawn("pamixer -t"), desc="mute the volume"),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("pamixer -d 5"),
        lazy.spawn("paplay .config/qtile/assets/audio-volume-change.oga"),
    ),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("pamixer -i 5"),
        lazy.spawn("paplay .config/qtile/assets/audio-volume-change.oga"),
    ),
    # ARROW KEYS for moving and changing window focus
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),

    # HJKL KEYS for moving and changing window focus (same functionality)
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),

    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    # ARROW KEYS for moving windows
    Key(
        [mod, "shift"],
        "Left",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        [mod, "shift"],
        "Right",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # HJKL KEYS for moving windows (same functionality)
    Key(
        [mod, "shift"],
        "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left",
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    # ARROW KEYS for growing windows
    Key(
        [mod, "control"],
        "Left",
        lazy.layout.grow_left(),
        desc="Grow window to the left",
    ),
    Key(
        [mod, "control"],
        "Right",
        lazy.layout.grow_right(),
        desc="Grow window to the right",
    ),
    Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),

    # HJKL KEYS for growing windows (same functionality)
    Key(
        [mod, "control"],
        "h",
        lazy.layout.grow_left(),
        desc="Grow window to the left",
    ),
    Key(
        [mod, "control"],
        "l",
        lazy.layout.grow_right(),
        desc="Grow window to the right",
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),

    Key([mod], "n", lazy.layout.normalize(),
        desc="mod + n Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn("kitty"), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="mod+w Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="mod+f Toggle fullscreen",
    ),
    Key([mod], "m", lazy.window.toggle_minimize(),
        desc="mod + m will toggle minimize"),
    Key([mod], "t", lazy.window.toggle_floating(),
        desc="mod +t Toggle floating"),
    Key(
        [mod, "control"],
        "r",
        lazy.reload_config(),
        desc="mod +ctrl + r Reload the config",
    ),
    Key([mod, "control"], "q", lazy.shutdown(),
        desc="mod + ctrl +q Shutdown Qtile"),
    Key(
        [mod], "r", lazy.spawn("rofi -show drun"), desc="mod +r Spawn rofi app laucher"
    ),
    # edit and add the browser you use
    Key([mod], "b", lazy.spawn("firefox"), desc="mod +b spawn brave browser"),
    Key(
        [mod],
        "Next",
        lazy.screen.next_group(),
        desc="mod + PgDn jump to the next group",
    ),
    Key(
        [mod],
        "Prior",
        lazy.screen.prev_group(),
        desc="mod + PgUp jump to the perior group",
    ),
]
###########################################
#   ______                                #
#  / ____/_____ ____   __  __ ____   _____#
# / / __ / ___// __ \ / / / // __ \ / ___/#
# / /_/ // /   / /_/ // /_/ // /_/ /(__  ) #
# \____//_/    \____/ \__,_// .___//____/  #
#                         /_/             #
###########################################
# groups = [Group(i) for i in "12345"]

groups = [
    Group("1", label="-"),
    Group("2", label="="),
    Group("3", label="≡"),
    Group("4", label="△"),
    Group("5", label="□"),
    # Group("6",label= "⬠"),
]

for i in groups:

    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group ",
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )
###################################################
#      __                                __       #
#     / /   ____ _ __  __ ____   __  __ / /_ _____#
#    / /   / __ `// / / // __ \ / / / // __// ___/#
#   / /___/ /_/ // /_/ // /_/ // /_/ // /_ (__  ) #
#  /_____/\__,_/ \__, / \____/ \__,_/ \__//____/  #
#               /____/                            #
###################################################
layouts = [
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(border_width=3, margin= 6, border_focus="ffffff", border_normal="ffff44", active_bg="99ccff", active_fg="ffffff",sections=[""]),
    # layout.VerticalTile(),
    # layout.Zoomy( margin=9,border_focus="cce6ff",border_normal="0059b3",border_on_single=True,border_width= 5),
    layout.MonadTall(
        auto_maximize=True,
        change_ratio=0.10,
        min_secondary_size=150,
        change_size=20,
        ratio=0.55,
        min_ratio=0.30,
        max_ratio=0.75,
        margin=7,
        border_focus=colors.Color1,
        border_normal=colors.Color0,
        border_on_single=False,
        border_width=2,
    ),
    layout.MonadWide(
        auto_maximize=True,
        change_ratio=0.10,
        min_secondary_size=400,
        change_size=20,
        ratio=0.55,
        min_ratio=0.30,
        max_ratio=0.75,
        margin=7,
        border_focus=colors.Color1,
        border_normal=colors.Color0,
        border_on_single=False,
        border_width=2,
    ),
    layout.Columns(
        margin=7,
        border_focus=colors.Color1,
        border_normal=colors.Color0,
        border_on_single=False,
        border_width=2,
    ),
    layout.Max(margin=0, border_focus=colors.Color7,
               border_normal=colors.Color1, border_width=0),
    layout.Spiral(
        margin=7,
        border_focus=colors.Color7,
        border_normal=colors.Color1,
        border_on_single=True,
        border_width=2,
    ),
    # layout.Floating( border_focus="#ffffff", border_normal= colors.Color1 ,border_width=5),
]
#########################################
# __        ___     _            _       #
# \ \      / (_) __| | __ _  ___| |_ ___ #
# \ \ /\ / /| |/ _` |/ _` |/ _ | __/ __|#
#  \ V  V / | | (_| | (_| |  __| |_\__ \#
#   \_/\_/  |_|\__,_|\__, |\___|\__|___/#
#  __| | ___ / _| __ |___/ _| | |_ ___  #
# / _` |/ _ | |_ / _` | | | | | __/ __| #
# | (_| |  __|  _| (_| | |_| | | |_\__ \ #
# \__,_|\___|_|  \__,_|\__,_|_|\__|___/ #
#########################################
widget_defaults = dict(
    font="JetBrainsMono Nerd Font",
    foreground="#fff",
    fontsize=16,
    padding=3,
)


extension_defaults = widget_defaults.copy()

circle = {
    "decorations": [
        RectDecoration(
            colour=colors.Color1,
            radius=14,  # [0,11,0,11],
            filled=True,
            extrawidth=0,
            group=True,
        )
    ]
}
circle1 = {
    "decorations": [
        RectDecoration(
            colour=colors.Color1,
            radius=14,  # [0,11,0,11],
            filled=True,
            extrawidth=0,
            group=True,
        ),
        RectDecoration(
            colour="#800000",
            radius=11,
            filled=True,
            padding_y=3,
            group=False,
            padding_x=3
        ),
    ]
}
circle2 = {
    "decorations": [
        RectDecoration(
            colour=colors.Color1,
            radius=14,  # [0,11,0,11],
            filled=True,
            extrawidth=0,
            group=True,
        ),
        RectDecoration(
            colour=colors.Color7,
            radius=11,  # [0,11,0,11],
            filled=True,
            padding_y=3,
            padding_x=3,
            extrawidth=0,
            group=False,
        ),
    ]
}


##################################################
#         _____                                  #
#        / ___/ _____ _____ ___   ___   ____     #
#        \__ \ / ___// ___// _ \ / _ \ / __ \    #
#       ___/ // /__ / /   /  __//  __// / / /    #
#      /____/ \___//_/    \___/ \___//_/ /_/     #
##################################################
def get_wireless_interface():
    """
    Dynamically detect the wireless network interface.

    Returns:
        str: Name of the wireless network interface.
    """
    result = subprocess.run(
        ["ip", "link"], capture_output=True, text=True, check=True)
    for line in result.stdout.split("\n"):
        if "wlan" in line or "wlp" in line:
            return line.split(":")[1].strip()
    return "wlan0"


screens = [
    Screen(
        top=bar.Bar(
            [
                # widget.PulseVolumeExtra(step=5,mode="popup",popup_layout=VOLUME_POPUP,limit_max_volume=True,),
                # there are some good shit that i can do here
                # widget.Mpris2(popup_layout=COMPACT_LAYOUT),
                widget.Spacer(
                    width=10,
                    length=0,
                ),
                widget.TextBox(
                    "     ",
                    foreground=colors.Color0,
                    **circle2,
                    fontsize=15,
                    mouse_callbacks={"Button1": lazy.function(qtile_menu)},
                ),
                widget.Spacer(length=9, **circle),
                widget.CurrentLayoutIcon(
                    **circle,
                    scale=0.8,
                ),
                widget.GroupBox(
                    fontsize=21,
                    active="ffffff",
                    highlight_method="block",
                    inactive=colors.Color15,
                    block_highlight_text_color=colors.Color0,
                    this_current_screen_border=colors.Color7,
                    padding_y=-3,
                    padding_x=4,
                    margin_x=3,
                    **circle,
                    center_aligned=True,
                    max_chars=50,
                ),
                widget.Spacer(length=10, **circle),
                widget.WindowName(
                    padding=10,
                    fontshadow=colors.Color0,
                    font="JetBrainsMono Nerd Font Bold",
                    foreground=colors.Color7,
                    format="   {state}{name}",
                    empty_group_string="What a great wallpaper...",
                ),
                widget.Spacer(length=15),
                widget.Spacer(length=15, **circle),
                widget.Clock(
                    fontsize=16,
                    format="󰸗 %a %d %b ",
                    # foreground=colors.Color0,
                    spacing="2",
                    mouse_callbacks={"Button1": lazy.function(calendar)},
                    **circle,
                ),
                widget.Clock(
                    fontsize=16,
                    format=" 󰥔 %I:%M %p ",
                    foreground=colors.Color0,
                    padding=2,
                    **circle2,
                ),
                widget.OpenWeather(
                    location="Austin",
                    format="{weather} {icon} {main_temp:.0f}°C",
                    metric=True,
                    padding=10,
                    fontsize=16,
                    weather_symbols={
                        "Unknown": "",
                        "01d": " ",
                        "01n": " ",
                        "02d": " ",
                        "02n": "󰼱 ",
                        "03d": "󰖐 ",
                        "03n": "󰖐 ",
                        "04d": " ",
                        "04n": " ",
                        "09d": "󰖖 ",
                        "09n": "󰖖 ",
                        "10d": " ",
                        "10n": " ",
                        "11d": "󰖓 ",
                        "11n": "󰖓 ",
                        "13d": " ",
                        "13n": " ",
                        "50d": "🌫",
                        "50n": "🌫",
                    },
                    **circle,
                ),
                widget.Spacer(length=(bar.STRETCH)),
                #
                #

                widget.Spacer(length=15, **circle),
                widget.Pomodoro(**circle),
                widget.TextBox(
                    fontsize=16,
                    text="  ",
                    mouse_callbacks=Btop,
                    **circle,
                ),
                widget.Memory(
                    mouse_callbacks=Btop,
                    format="{MemPercent:.0f}% ",
                    **circle,
                ),
                widget.TextBox(
                    mouse_callbacks=Btop,
                    fontsize=19,
                    text="󰍛 ",
                    **circle,
                ),
                widget.Spacer(length=-6, **circle),
                widget.CPU(
                    mouse_callbacks=Btop,
                    format="{load_percent:.0f}%",
                    update_interval=1,
                    **circle,
                ),
                widget.ThermalSensor(
                    mouse_callbacks=Btop,
                    format=" 󰔏 {temp:.0f}{unit} ",
                    tag_sensor="Core 0",
                    update_interval=1,
                    threshold=80,
                    foreground_alert="800000",
                    **circle,
                ),
                widget.Spacer(
                    width=0,
                    length=10,
                ),
                widget.WidgetBox(
                    widgets=[
                        widget.Spacer(
                            width=0,
                            length=10,
                            **circle
                        ),
                        widget.TextBox(
                            text="󱅫 ",
                            **circle,
                            mouse_callbacks={
                                "Button1": lazy.spawn("dunstctl history-pop")
                            },
                        ),

                        widget.CheckUpdates(
                            distro="Arch_checkupdates",
                            no_update_string="",
                            colour_have_updates="ffffff",
                            colour_no_updates="ffffff",
                            fontsize=15,
                            display_format=" {updates}",
                            mouse_callbacks={
                                "Button1": lazy.spawn("kitty -e ./.config/qtile/update.sh")
                            },
                            **circle,
                        ),
                        widget.StatusNotifier(
                            highlight_colour=colors.Color7,
                            menu_foreground=colors.Color7,
                            menu_foreground_highlighted=colors.Color0,
                            menu_background=colors.Color1,
                            separator_colour=colors.Color7,
                            menu_offset_y=0,
                            padding=7,
                            **circle,
                            icon_size=20,
                            icon_theme="Promix",
                        ),
                        widget.Systray(**circle),
                    ],
                    **circle2,
                    close_button_location="right",
                    text_closed="  ",
                    text_open="  ",
                    foreground=colors.Color0,
                ),
                widget.Spacer(length=9, **circle),
                widget.PulseVolume(
                    **circle,
                    icon_size=12,
                    # theme_path="/usr/share/icons/Qogir-dark/16@2x/panel/",
                    emoji=True,
                    emoji_list=['  ', '  ', '  ', '  '],
                ),
                widget.Spacer(length=-8, **circle),
                widget.PulseVolumeExtra(
                    **circle,
                    mode="bar",
                    bar_height=4,
                    bar_colour_high=colors.Color7,
                    bar_colour_loud=colors.Color7,
                    bar_colour_mute=colors.Color7,
                    bar_colour_normal=colors.Color7,
                    bar_background=colors.Color1,
                    background=colors.Color1,
                    bar_width=40,
                    unmute_format="",
                    fontsize=15,
                ),
                widget.Spacer(
                    width=0,
                    length=8,
                    **circle
                ),
                widget.Spacer(
                    width=0,
                    length=8,
                    **circle
                ),
                widget.WiFiIcon(
                    interface=get_wireless_interface(),
                    padding=8,
                    **circle,
                    mouse_callbacks={
                        "Button1": lambda: qtile.spawn(
                            "networkmanager_dmenu -theme ~/.config/rofi/networkmenu.rasi"
                        )
                    },

                ),
                widget.Spacer(
                    width=0,
                    length=8,
                    **circle
                ),
                widget.UPowerWidget(
                    border_colour="#ffffff",
                    border_critical_colour="#cc0000",
                    border_charge_colour="#ffffff",
                    fill_low="#ffff00",
                    fill_charge="#00cc66",
                    fill_critical="#cc0000",
                    fill_normal="#ffffff",
                    percentage_low=0.4,
                    percentage_critical=0.25,
                    text_charging="({percentage:.0f}%)",
                    text_discharging="{percentage:.0f}%",
                    text_displaytime=3666,
                    battery_height=13,
                    battery_width=27,
                    spacing=6,
                    **circle,
                    mouse_callbacks={
                        "Button3": lazy.function(show_power_profile)},
                ),
                widget.Spacer(length=10, **circle),
                widget.TextBox(
                    "⏻ ",
                    **circle1,
                    padding=20,
                    fontsize=15,
                    mouse_callbacks={
                        "Button1": lazy.function(show_power_menu)},
                ),
            ],
            30,
            # this ^^ is the bar hight
            border_width=[0, 0, 0, 0],  # Draw top and bottom borders
            border_color=["#00000000", "0070cc", "#00000000", "0070cc"],
            x=0,
            y=0,
            width=1920,
            hight=1080,
            margin=[5, 10, 0, 10],
            # Borders are magenta (UP,SIDE,DOWN,SIDE)
            opacity=1,
            background="#00000000",
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 400,
    ),
]
####################################################
#          __  ___                                 #
#         /  |/  /____   __  __ _____ ___          #
#        / /|_/ // __ \ / / / // ___// _ \         #
#       / /  / // /_/ // /_/ /(__  )/  __/         #
#      /_/  /_/ \____/ \__,_//____/ \___/          #
####################################################
# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
    Click([mod, "shift"], "Button2", lazy.window.move_to_bottom()),
]
#####################################################################################
#         ____   __   __                  ______ __     _                           #
#        / __ \ / /_ / /_   ___   _____  /_  __// /_   (_)____   ____ _ _____       #
#       / / / // __// __ \ / _ \ / ___/   / /  / __ \ / // __ \ / __ `// ___/       #
#      / /_/ // /_ / / / //  __// /      / /  / / / // // / / // /_/ /(__  )        #
#      \____/ \__//_/ /_/ \___//_/      /_/  /_/ /_//_//_/ /_/ \__, //____/         #
#                                                             /____/                #
#####################################################################################


def set_keep_above(window):
    wm_class = window.window.get_wm_class()
    if wm_class and "plank" in [c.lower() for c in wm_class]:
        window.keep_above = True


dgroups_key_binder = None
dgroups_app_rules = []  # type: list
main = None
follow_mouse_focus = True
bring_front_click = True
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    margin=7,
    border_focus="cce6ff",
    border_normal=colors.Color1,
    border_on_single=True,
    border_width=0,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="nm-connection-editor"),
        Match(wm_class="qalculate-gtk"),  # gitk
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="copyq"),
        Match(wm_class="wpg"),
        Match(wm_class="lxappearance"),
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="korganizer"),  # GPG key password entry
        Match(wm_class="cairo-dock"),
    ],
)
auto_fullscreen = True
focus_on_window_activation = "never"
reconfigure_screens = True


# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java"s whitelist.
wmname = "LG3D"
