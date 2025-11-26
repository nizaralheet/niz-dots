import subprocess
import re
import datetime
from libqtile import qtile
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras.popup.toolkit import (
    PopupRelativeLayout,
    PopupText,
    PopupImage,
    PopupWidget,
    PopupGridLayout,
)
from qtile_extras.popup.menu import PopupMenuItem, PopupMenuSeparator
from libqtile.lazy import lazy
import colors
############################
#     _       __          #
#    | |     / _|         #
#  __| | ___| |_   ___    #
# / _` |/ _ \  _| / __|   #
# | (_| |  __/ |   \__ \   #
# \__,_|\___|_|   |___/   #
#                         #
##########################


# these two function are together make a simple app menu , to edit it you shoule change the icons , label and the action
def create_icon(filename, row, col):
    return PopupImage(
        filename=filename,
        row=row,
        col=col,
    )


# Define a function to create a text label with associated action
def create_label(
    text,
    row,
    col,
    command,
    font="JetBrainsMono Nerd Font",
    fontsize=15,
    foreground_highlighted=colors.Color0,
    highlight=colors.Color7,
    highlight_radius=9,
    highlight_border=5,
):
    return PopupText(
        text=text,
        row=row,
        col=col,
        col_span=9,  # Span across 9 columns
        mouse_callbacks={"Button1": lazy.spawn(command)},
        font=font,
        fontsize=fontsize,
        foreground_highlighted=foreground_highlighted,
        highlight=highlight,
        highlight_radius=highlight_radius,
        highlight_border=highlight_border,
    )


def qtile_menu(qtile):
    controls = [
        create_icon(
            "~/.local/share/icons/Promix/scalable@2x/apps/firefox.svg", 0, 0
        ),
        create_icon(
            "~/.local/share/icons/Promix/scalable@2x/apps/thunar.svg",
            1,
            0,
        ),
        create_icon(
            "~/.local/share/icons/Promix/scalable@2x/apps/neovim.svg",
            2,
            0,
        ),
        create_icon(
            "~/.local/share/icons/Promix/scalable@2x/apps/kitty.svg", 3, 0
        ),
        create_label(" Browser", 0, 1, "firefox"),
        create_label(" File Manager", 1, 1, "thunar"),
        create_label(" Text Editor", 2, 1, "kitty -e nvim"),
        create_label(" Terminal", 3, 1, "kitty"),
        create_label(" Reload config", 4, 1, "qtile cmd-obj -o root -f reload_config"),
        PopupText(
            " ", row=4, col=0, col_span=1, font="JetBrainsMono Nerd Font ", fontsize=16,
        ),
    ]

    layout = PopupGridLayout(
        qtile,
        rows=5,  # Adjust rows dynamically
        cols=10,
        height=170,
        width=200,
        controls=controls,
        # border_width=3,
        border=colors.Color7,
        background=colors.Color1,
        hide_on_timeout=4,
        hide_interval=1,
    )
    layout.show(
        x=10,
        y=38,
        hide_on_timeout=4,
    )


# tthis function choose what is the action should be when click yes on are_you_sure
def chooser(option):
    def choose(qtile):
        action = None
        if option == "logout":
            action = lazy.shutdown()
        elif option == "suspend":
            action = lazy.spawn("systemctl suspend")
        elif option == "poweroff":
            action = lazy.spawn("poweroff")
        are_you_sure(qtile, action)

    return choose


#######################################
def show_power_menu(qtile):  # this is for power options like power off or  sleep
    time = subprocess.check_output(
        "uptime -p | awk '{print \"Uptime: \" $2, $3, $4, $5}'", shell=True, text=True
    )
    time = time.strip()
    controls = [
        PopupImage(
            filename="/home/nizar/.local/share/icons/Promix/32@2x/actions/system-log-out.svg",
            pos_x=0.125,
            pos_y=0.3,
            width=0.14,
            height=0.5,
            highlight=colors.Color1,
            highlight_border=-15,
            highlight_radius=57,
            mouse_callbacks={"Button1": lazy.function(chooser("logout"))},
        ),
        PopupImage(
            filename="/home/nizar/.local/share/icons/Promix/32@2x/actions/system-suspend.svg",
            pos_x=0.43,
            pos_y=0.3,
            width=0.14,
            height=0.5,
            highlight=colors.Color1,
            highlight_border=-15,
            highlight_radius=57,
            mouse_callbacks={"Button1": lazy.function(chooser("suspend"))},
        ),
        PopupImage(
            filename="/home/nizar/.local/share/icons/Promix/32@2x/actions/system-shutdown.svg",
            pos_x=0.735,
            pos_y=0.3,
            width=0.14,
            height=0.5,
            highlight_border=-15,
            highlight_radius=57,
            highlight="A00000",
            mouse_callbacks={"Button1": lazy.function(chooser("poweroff"))},
        ),
        PopupWidget(
            widget=widget.TextBox(
                text=time,
                padding=45,
                foreground="#ffffff",
                # background=Color9,
                fontsize=16,
                markup=True,
                decorations=[
                    RectDecoration(
                        colour=colors.Color1,
                        radius=[0, 0, 11, 11],
                        filled=True,
                        extrawidth=0,
                        padding_x=20,
                        # group=True
                    )
                ],
            ),
            pos_x=0.25,
            pos_y=-0.05,
            width=0.5,
            height=0.28,
        ),
    ]

    layout = PopupRelativeLayout(
        qtile,
        width=700,
        border_width=3,
        border=colors.Color1,
        height=200,
        controls=controls,
        background="00000060",
        initial_focus=None,
    )

    layout.show(centered=True)


def are_you_sure(
    qtile, action
):  # it's clear what it dose , it show are you sure window for power optons like
    qtile.spawn(
        "ffplay -nodisp -autoexit /usr/share/sounds/ocean/stereo/dialog-question.oga"
    )
    controls = [
        PopupWidget(
            widget=widget.TextBox(
                "  Are you sure about that?",
                foreground="#ffffff",
                background=colors.Color1,
                fontsize=21,
                padding=60,
            ),
            pos_x=-0.02,
            pos_y=0.1,
            width=1.05,
            height=0.2,
            h_align="center",
        ),
        PopupText(
            fontsize=20,
            text="Yes",
            pos_x=0.2,
            h_align="center",
            pos_y=0.5,
            width=0.2,
            height=0.3,
            highlight=colors.Color1,
            highlight_method="block",
            mouse_callbacks={"Button1": action},
        ),
        PopupText(
            fontsize=20,
            text="No",
            pos_x=0.6,
            h_align="center",
            pos_y=0.5,
            width=0.2,
            height=0.3,
            highlight=colors.Color1,
            highlight_method="block",
            mouse_callbacks={"Button1": lazy.spawn("")},
        ),
    ]
    layout_sure = PopupRelativeLayout(
        qtile,
        width=400,
        hight=170,
        controls=controls,
        background="0000007f",
        border_width=3,
        border=colors.Color1,
    )
    layout_sure.show(centered=True)


class CalendarPopup:
    # test={"Button1": lazy.spawn("kitty")}
    def __init__(self):
        self.started = False
        self.hidden = True

    def _create_layout(self):

        # Get the calendar from the shell command
        today = datetime.datetime.now().day
        cal_output = subprocess.check_output("cal", shell=True, text=True)
        cal_lines = cal_output.splitlines()
        highlighted_cal = []
        for line in cal_lines:
            highlighted_line = re.sub(
                rf"\b{today}\b",
                f'<span background="#f0f0f0" foreground="#0f0f0f" weight="bold">{today}</span>',
                line,
            )
            highlighted_cal.append(highlighted_line)
        highlighted_cal_output = "\n".join(highlighted_cal)
        #############

        controls = [
            PopupText(
                highlighted_cal_output,
                font="JetBrainsMono Nerd Font",
                markup=True,
                fontsize=18,
                row=1,
                col=1,
                row_span=8,
                col_span=8,
                # mouse_callbacks={ "Button1": lambda: self.hide_popup()} # This also works but in a less effective way
            )
        ]

        self.layout = PopupGridLayout(
            qtile,
            rows=10,
            cols=10,
            height=210,
            width=300,
            close_on_click=False,
            controls=controls,
            background=colors.Color1,
            hide_on_timeout=0,
        )
        self.layout.bind_callbacks()  # This seems not to work; tested with other callbacks that work

    def hide_popup(self):
        self.hidden = True
        self.layout.hide()

    def toggle(self, x=0, y=0):
        if not self.started:
            self._create_layout()
            self.layout.show(qtile=qtile, x=x, y=y, relative_to_bar=True, relative_to=2)
            self.started = True
            self.hidden = False
        elif self.hidden:
            # self.layout.update_controls(relative_to_bar=True)
            self.layout.show(qtile=qtile, x=x, y=y, relative_to_bar=True, relative_to=2)
            self.hidden = False
        else:
            self.layout.hide()
            self.hidden = True


show_cal = CalendarPopup()


def calendar(qtile):
    show_cal.toggle(x=-110, y=10)


"""
class KBPopup:
    def __init__(self):
        self.hidden = True
        self.started = False

    def _create_layout(self, initial_text):
        controls = [
            PopupText(
                name="layout",
                text=initial_text,
                font="Iosevka NF SemiBold",
                fontsize=22,
                background=colors.Color1,
                pos_x=0.0,
                pos_y=0.0,
                height=1,
                width=1,
                h_align="center",
            )
        ]
        self.layout = PopupRelativeLayout(
            qtile,
            width=200,
            height=60,
            controls=controls,
            close_on_click=True,
            hide_on_timeout=2,
        )

    def toggle(self, text="", x=0, y=0):
        if not self.started:
            self._create_layout(text)
            self.layout.show(qtile=qtile, x=x, y=y)
            self.started = True
            self.hidden = False
        elif self.hidden:
            self.layout.update_controls(layout=text)
            self.layout.show(x=x, y=y)
            self.hidden = False
        else:
            self.layout.hide()
            self.hidden = True


kb_layout = KBPopup()

def keylay(qtile):
    thelay = subprocess.check_output("setxkbmap -query | grep layout | awk '{print $2}' | tr 'a-z' 'A-Z'", shell=True, text=True)
    thelay = "󰌌 : " + thelay.strip()
    kb_layout.toggle(x=860, y=140)
"""
# powerprofiles


# ============================================
# MENU STYLING - CUSTOMIZE COLORS HERE
# ============================================

# Replace these with your actual color variables
MENU_STYLE = {
    'bg': colors.Color1,
    'fg': colors.Color15,
    'highlight': colors.Color0,
    'accent': colors.Color7,
    'border': colors.Color7,
    'active': '#9ece6a',
    'disabled': colors.Color15,
}


# ============================================
# MENU STATE
# ============================================

class MenuState:
    power_profile_menu = None


# ============================================
# MENU FUNCTION
# ============================================

def show_power_profile(qtile):
    """
    Display power profile menu popup
    """
    # Toggle: close if already open
    if MenuState.power_profile_menu:
        MenuState.power_profile_menu.hide()
        MenuState.power_profile_menu = None
        return

    # Get current profile
    current_profile = subprocess.check_output(
        "powerprofilesctl get", shell=True, text=True
    ).strip()

    def create_menu_item(text, profile_name, row):
        is_active = current_profile == profile_name
        return PopupMenuItem(
            text=text,
            row=row,
            col=0,
            col_span=1,
            row_span=2,
            font="JetBrainsMono Nerd Font ",
            background=MENU_STYLE['bg'],
            foreground=MENU_STYLE['fg'],
            foreground_highlighted=MENU_STYLE['highlight'],
            highlight=MENU_STYLE['accent'],
            toggle_box=True,
            toggled=is_active,
            mouse_callbacks={
                "Button1": lambda p=profile_name: set_profile_and_close(qtile, p)
            },
            fontsize=14,
        )

    controls = [
        PopupText(
            text="Power Profile",
            row=0,
            col=0,
            row_span=2,
            col_span=1,
            h_align="center",
            background=MENU_STYLE['bg'],
            foreground=MENU_STYLE['accent'],
            fontsize=16,
            font="JetBrainsMono Nerd Font Bold",
        ),

        PopupMenuSeparator(
            row=2,
            col=0,
            col_span=1,
            row_span=1,
            colour_above=MENU_STYLE['border'],
        ),

        create_menu_item("󰌪  Power Saver", "power-saver", 3),
        create_menu_item("󰾅  Balanced", "balanced", 5),
        create_menu_item("󰓅  Performance", "performance", 7),

        PopupText(
            text=f"Current: {current_profile}",
            row=9,
            col=0,
            row_span=1,
            col_span=1,
            h_align="center",
            background=MENU_STYLE['bg'],
            foreground=MENU_STYLE['disabled'],
            fontsize=11,
            font="sans italic",
        ),
    ]

    layout = PopupGridLayout(
        qtile,
        width=180,
        height=240,
        rows=10,
        cols=1,
        controls=controls,
        background=MENU_STYLE['bg'],
        opacity=0.95,
        border_width=2,
        border=MENU_STYLE['border'],
        margin=4,
        hide_on_mouse_leave=True,
        hide_on_timeout=4,
    )

    layout.show(relative_to_bar=True, relative_to=3, x=-15, y=10)
    MenuState.power_profile_menu = layout


def set_profile_and_close(qtile, profile):
    """Set power profile and close menu"""
    try:
        subprocess.run(["powerprofilesctl", "set", profile], check=True)
        print(f"Power profile set to: {profile}")
    except Exception as e:
        print(f"Error setting power profile: {e}")

    # Close menu
    if MenuState.power_profile_menu:
        MenuState.power_profile_menu.hide()
        MenuState.power_profile_menu = None


"""
def show_cal(qtile): # this function shows the calendar when you click at the date widget
    # Get today's day as an integer , to be able then to highligte it
    today = datetime.datetime.now().day
    # Run the `cal` command and capture the output
    cal_output = subprocess.check_output("cal", shell=True, text=True)
    # Split the calendar output into lines
    cal_lines = cal_output.splitlines()

    # Highlight the current day in the calendar output
    highlighted_cal = []
    for line in cal_lines:
        # Search for the current day in the calendar line , it uses pango markup
        highlighted_line = re.sub(rf"\b{today}\b", f'<span background="#f0f0f0" foreground="#0f0f0f" weight="bold">{today}</span>', line)
        highlighted_cal.append(highlighted_line)
    # Join the lines back together
    highlighted_cal_output = "\n".join(highlighted_cal)
    controls = [
        PopupText(

            highlighted_cal_output,
            font="Iosevka NF SemiBold",
            markup=True,
            fontsize=18,
            row=1,
            col=1,
            row_span=8,
            col_span=8
        )
    ]

    layout_cal = PopupGridLayout(
        qtile,
        rows=10,
        cols=10,
        height=210,
        width=250,
        controls=controls,
        background=colors.Color1,
        hide_interval=10,
    )
    layout_cal.show(relative_to_bar=True,x=720,y=10,hide_on_timeout=False)
"""
