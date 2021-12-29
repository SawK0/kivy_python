# pip install kivy - installing kivy

from kivy.app import App
from kivy.uix.widget import Widget


class MainWidget(Widget):  # Create interface. need to import Widget
    pass


class TheLabApp(App):  # start app. Need to import App
    pass


TheLabApp().run()
