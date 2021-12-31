# pip install kivy - installing kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


# class GridLayoutExample(GridLayout):
    # pass
    # create class directly in ky file <ClassName@Parameter>:


class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
    pass
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.orientation = "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
    """

class MainWidget(Widget):  # Create interface. need to import Widget
    pass


class TheLabApp(App):  # start app. Need to import App
    pass


TheLabApp().run()
