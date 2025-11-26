import json
import os


colors = os.path.expanduser("~/.cache/wal/colors.json")
colordict = json.load(open(colors))
Color0 = colordict["colors"]["color0"]
Color1 = colordict["colors"]["color1"]
Color2 = colordict["colors"]["color2"]
Color3 = colordict["colors"]["color3"]
Color4 = colordict["colors"]["color4"]
Color5 = colordict["colors"]["color5"]
Color6 = colordict["colors"]["color6"]
Color7 = colordict["colors"]["color7"]
Color8 = colordict["colors"]["color8"]
Color9 = colordict["colors"]["color9"]
Color10 = colordict["colors"]["color10"]
Color11 = colordict["colors"]["color11"]
Color12 = colordict["colors"]["color12"]
Color13 = colordict["colors"]["color13"]
Color14 = colordict["colors"]["color14"]
Color15 = colordict["colors"]["color15"]
BgMain = Color0
BgSec = Color1
FgMain = Color7
FgSec = Color15

