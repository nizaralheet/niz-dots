from libqtile import widget, bar
from libqtile.widget.base import _Widget

class StaticImageTextWidget(_Widget):
    def __init__(self, image_path, text, **config):
        _Widget.__init__(self, length=bar.CALCULATED, **config)
        self.image_path = image_path
        self.text = text
        self.textbox = widget.TextBox(text=self.text, **config)
        self.imagebox = widget.Image(filename=self.image_path)

    def draw(self):
        # Draw the image first
        self.imagebox.draw()

        # Move the cursor to the right of the image
        self.offsetx += self.imagebox.width

        # Draw the text
        self.textbox.draw()

    def calculate_length(self):
        return self.imagebox.width + self.textbox.calculate_length()

def my_static_widget():
    return StaticImageTextWidget(
        image_path='/home/nizar/.local/share/icons/Deepin2022-Dark/scalable@2x/apps/brave.svg', 
        text='Text',
        foreground='ffffff',  # text color
        fontsize=14,          # font size for the text
        background='000000',  # background color of the widget
    )

