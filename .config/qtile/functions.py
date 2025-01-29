import time 
import psutil
from qtile_extras.widget import decorations
import subprocess 
import os
import json
import re 
import datetime
from libqtile import qtile
from libqtile.widget import TextBox
from qtile_extras import widget, layout
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras.popup.toolkit import PopupRelativeLayout, PopupText, PopupImage ,PopupWidget,PopupGridLayout
from libqtile.lazy import lazy


colors = os.path.expanduser('~/.cache/wal/colors.json')
colordict = json.load(open(colors))
Color0=(colordict['colors']['color0'])
Color1=(colordict['colors']['color1'])
Color2=(colordict['colors']['color2'])
Color3=(colordict['colors']['color3'])
Color4=(colordict['colors']['color4'])
Color5=(colordict['colors']['color5'])
Color6=(colordict['colors']['color6'])
Color7=(colordict['colors']['color7'])
Color8=(colordict['colors']['color8'])
Color9=(colordict['colors']['color9'])
Color10=(colordict['colors']['color10'])
Color11=(colordict['colors']['color11'])
Color12=(colordict['colors']['color12'])
Color13=(colordict['colors']['color13'])
Color14=(colordict['colors']['color14'])
Color15=(colordict['colors']['color15'])
############################
#     _       __          #
#    | |     / _|         #
#  __| | ___| |_   ___    #
# / _` |/ _ \  _| / __|   #
#| (_| |  __/ |   \__ \   #
# \__,_|\___|_|   |___/   #
#                         #
##########################



     #these two function are together make a simple app menu , to edit it you shoule change the icons , label and the action 
def create_icon(filename, row, col):
    return PopupImage(
        filename=filename,
        row=row,
        col=col,
    )

# Define a function to create a text label with associated action
def create_label(text, row, col, command, font="Iosevka NF SemiBold",fontsize=15,foreground_highlighted=Color0,highlight=Color7,highlight_radius=9,highlight_border=5,):
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
        create_icon("~/.local/share/icons/Deepin2022-Dark/scalable@2x/apps/firefox.svg", 0, 0),
        create_icon("~/.local/share/icons/Deepin2022-Dark/scalable@2x/apps/file-manager.svg", 1, 0 ),
        create_icon("~/.local/share/icons/hicolor/24x24/apps/lvim.svg", 2, 0, ),
        create_icon("~/.local/share/icons/Deepin2022-Dark/scalable@2x/apps/kitty.svg", 3, 0 ),
        
        create_label(" Browser", 0, 1, "firefox"),
        create_label(" File Manager", 1, 1, "thunar"),
        create_label(" Text Editor", 2, 1, "kitty -e lvim"),
        create_label(" Terminal", 3, 1, "kitty"),
        create_label(" Reload config", 4, 1, "qtile cmd-obj -o root -f reload_config"),
        PopupText(" ",row=4,col=0,col_span=1,font="Iosevka NF SemiBold",fontsize=16)
    ]

    layout = PopupGridLayout(
        qtile,
        rows=5,  # Adjust rows dynamically
        cols=10,
        height=170,
        width=200,
        controls=controls,
        #border_width=3,
        border=Color7,
        background=Color1,
        hide_on_timeout=4,
        hide_interval=1,
    )
    layout.show(x=10, y=38,hide_on_timeout=4,)


######################################tthis function choose what is the action should be when click yes on are_you_sure
def chooser(option): 
    def choose(qtile):
        action =None
        if option == "logout":
            action = lazy.shutdown()
        elif option == "suspend":
            action = lazy.spawn("systemctl suspend")
        elif option == "poweroff":
            action = lazy.spawn("poweroff")
        are_you_sure(qtile, action)
    return choose
#######################################
def show_power_menu(qtile): # this is for power options like power off or  sleep 
    time=subprocess.check_output("uptime -p | awk '{print \"Uptime: \" $2, $3, $4, $5}'", shell=True, text=True)
    time=time.strip()
    controls = [

        PopupImage(
            filename="/home/nizar/.local/share/icons/Deepin2022-Dark/32@2x/actions/system-log-out.svg",
            pos_x=0.125,
            pos_y=0.3,
            width=0.14,
            height=0.5,
            highlight=Color1,
            highlight_border=-15,
            highlight_radius=57,
            mouse_callbacks={
                "Button1": lazy.function(chooser("logout")) 
            }
        ),
        PopupImage(
            filename="/home/nizar/.local/share/icons/Promix/32@2x/actions/system-suspend.svg",
            pos_x=0.43,
            pos_y=0.3,
            width=0.14,
            height=0.5,
            highlight=Color1,
            highlight_border=-15,
            highlight_radius=57,
            mouse_callbacks={
                "Button1": lazy.function(chooser("suspend"))
            }
        ),
        PopupImage(
             filename="/home/nizar/.local/share/icons/Deepin2022-Dark/32@2x/actions/system-shutdown.svg",
             pos_x=0.735,
             pos_y=0.3,
             width=0.14,
            height=0.5,
            highlight_border=-15,
            highlight_radius=57,
            highlight="A00000",
            mouse_callbacks={
                "Button1": lazy.function(chooser("poweroff"))
            }
         ),

        PopupWidget(
            widget=widget.TextBox(
                text=time,
                padding=60,
                foreground="#ffffff",
                #background=Color9,
                fontsize=16,
                markup=True,
                decorations=[
                    RectDecoration(
                    colour=Color1,
                    radius=[0,0,11,11],
                    filled=True,
                    extrawidth=0,
                    padding_x=20
                    #group=True
                    )
                ]
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
        border=Color1,
        height=200,
        controls=controls,
        background="00000060",
        initial_focus=None,

    )

    layout.show(centered=True)


def are_you_sure(qtile,action): # it's clear what it dose , it show are you sure window for power optons like
    qtile.spawn("ffplay -nodisp -autoexit /usr/share/sounds/ocean/stereo/dialog-question.oga")
    controls=[
        PopupWidget(
            widget=widget.TextBox(
                "  Are you sure about that?",
                foreground="#ffffff",
                background=Color1,
                fontsize=21,
                padding=60,
                ),
            pos_x=-0.02,
            pos_y=0.1,
            width=1.05,
            height=0.2,
            h_align="center"
        ),

        PopupText(
            fontsize=20,
            text="Yes",
            pos_x=0.2,
            h_align="center",
            pos_y=0.5,
            width=0.2,
            height=0.3,
            highlight=Color1,
            highlight_method="block",
            mouse_callbacks={
                "Button1": action
            }
        ),

        PopupText(
            fontsize=20,
            text="No",
            pos_x=0.6,
            h_align="center",
            pos_y=0.5,
            width=0.2,
            height=0.3,
            highlight=Color1,
            highlight_method="block",
            mouse_callbacks={
                "Button1":lazy.spawn("") }  )
        ]
    layout_sure = PopupRelativeLayout(
        qtile,
        width=400,
        hight=170,
        controls=controls,
        background="0000007f",
        border_width=3,
        border=Color1,
    )
    layout_sure.show(centered=True)





class CalendarPopup:
    #test={"Button1": lazy.spawn("kitty")}
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
                line
            )
            highlighted_cal.append(highlighted_line)
        highlighted_cal_output = "\n".join(highlighted_cal)  
        #############

        controls = [
            PopupText(
                highlighted_cal_output,
                font="Iosevka NF SemiBold",
                markup=True,
                fontsize=18,
                row=1,
                col=1,
                row_span=8,
                col_span=8,
                #mouse_callbacks={ "Button1": lambda: self.hide_popup()} # This also works but in a less effective way
            )
        ]

        self.layout = PopupGridLayout(
            qtile,
            rows=10, 
            cols=10,
            height=210,
            width=250,
            close_on_click=False,
            controls=controls,
            background=Color1,
            hide_on_timeout=0, 
        )
        self.layout.bind_callbacks()  # This seems not to work; tested with other callbacks that work

    def hide_popup(self):
        self.hidden = True
        self.layout.hide()

    def toggle(self, x=0, y=0):
        if not self.started:
            self._create_layout()
            self.layout.show(qtile=qtile, x=x, y=y, relative_to_bar=True)
            self.started = True
            self.hidden = False
        elif self.hidden:
            # self.layout.update_controls(relative_to_bar=True)
            self.layout.show(qtile=qtile, x=x, y=y, relative_to_bar=True)
            self.hidden = False
        else:
            self.layout.hide()
            self.hidden = True

show_cal = CalendarPopup()

def calendar(qtile):
    show_cal.toggle(x=720, y=10)
'''
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
                background=Color1,
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
''' 
##### POWER PROFILE########

def show_power_profile(qtile): # this for power profiles in stead of using the Terminal every time you want to change them 
    current_profile = subprocess.check_output("powerprofilesctl get", shell=True, text=True).strip()

    def create_profile_image(filename, row, highlight_filename, profile_name):
        return PopupImage(
            filename=filename,
            row=row,
            col=1,
            col_span=3,
            row_span=6,
            highlight=Color8,
            #highlight_method="",
            highlight_filename=highlight_filename,
            mouse_callbacks={
                "Button1": lazy.spawn(f"powerprofilesctl set {profile_name}")
            }
        )

    def create_profile_indicator(row, profile_name):
        return PopupWidget(
            widget=TextBox(
                text="⯈" if current_profile == profile_name else "",
                foreground=Color7,
                fontsize=24,
            ),
            col=0,
            row=row,
            row_span=4
        )

    controls = [
        create_profile_image("~/.config/qtile/assets/power-profile-power-saver.svg", 2,"~/.config/qtile/assets/power-profile-power-saver-dark.svg", "power-saver"),
        create_profile_image("~/.config/qtile/assets/power-profile-balanced.svg", 10,"~/.config/qtile/assets/power-profile-balanced-dark.svg", "balanced"),
        create_profile_image("~/.config/qtile/assets/power-profile-performance.svg", 18,"~/.config/qtile/assets/power-profile-performance-dark.svg", "performance"),
        
        create_profile_indicator(3, "power-saver"),
        create_profile_indicator(11, "balanced"),
        create_profile_indicator(19, "performance"),

    ]



    layout= PopupGridLayout(
        qtile,
        rows=26,
        cols=4,
        height=200,
        width=110,
        controls=controls,
        #border_width=0,
        #border=Color7,
        background=Color1,
        hide_on_timeout=4,
        hide_interval=1,
    )
    layout.show(x=1765,y=38)
'''
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
        background=Color1,
        hide_interval=10,
    )
    layout_cal.show(relative_to_bar=True,x=720,y=10,hide_on_timeout=False)

    
'''
