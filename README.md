Study Resource - https://youtu.be/l8Imtec4ReQ?list=PLLbbi0_jHZaTbzr15tjYl4S5vih83FzXb 

### Install Kivy 
pip install kivy


### Create Main file
main.py 

### import App and Widget 
from kivy.app import App
from kivy.uix.widget import Widget

import Widget is for interface

### Create kv file. The file's name should be exactly the same as App class
class TheLabApp(App):
    pass

mkdir TheLab.kv


## KIVY LAYOUTS

### 1) Box Layout 
stack vertically or horizontally

### 2) Anchor Layout


### 3) Grid Layout


### 4) Stack Layout


### 5) Scroll Layout


### 6) Page Layout


Float/Reative/Scatter Layout

## Add Button and Label 
InterfaceName:

<InterfaceName>:
    Button:
        text: "buttonText"
        size: width, height  # "40dp", "40dp"
        pos: x, y  # "100dp", "100dp"
        color: r, g, b, a 

Example -        
<MainWidget>:
    Button:
        text: "Hello"
        size: "100dp", "80dp"
        pos: "100dp", "200dp"
        color: 0, 0, 1, 1

    Label:
        text: "Hello2"
        size: "100dp", "80dp"
        pos: "200dp", "200dp"
        color: 1, 0, 0, 1
