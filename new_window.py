from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

import random

#convert_color accepts four parameters: (red,green,blue,alpha)
#where each value is a number between 0-255
#and returns a tuple in the kivy format (0-1) instead of (0-255)
def convert_color(r,g,b,a):
    return (r/255,g/255,b/255,a/255)


Window.clearcolor = convert_color(108, 172, 212,255)
Window.clear()

red = [1,0,0,.5]
green = [0,1,0,.5]
blue =  [0,0,1,.5]
purple = [1,0,1,.5]

button_padding = (100,100)
options = ["Calendar", "Quick Log","Weekly Summary", "Meditation"]

sm = ScreenManager()

class AwesomeApp(App):
    

    def build(self):
        global sm 
        # this is the call back function that registers the four menu buttons 
        # also allows on button press to switch windows
        def on_press_button(instance):
            global sm 
            if instance.text == options[0]:
                sm.current = "calendar"
            elif instance.text == options[1]:
                sm.current = "quick log"
            elif instance.text == options[2]:
                sm.current = "weekly summary"
            else: 
                sm.current = "meditation"

        main_layout = BoxLayout(orientation="vertical")
        colors = [red, green, blue, purple]
        top_layout = BoxLayout(orientation="horizontal")
        bottom_layout = BoxLayout(orientation="horizontal")
        for i in range(4):
            in_layout = BoxLayout(orientation="horizontal", padding=button_padding)
            btn = Button(background_color=colors[i],text=options[i])
            btn.bind(on_press=on_press_button)
            in_layout.add_widget(btn) 
            if(i<2):
                top_layout.add_widget(in_layout)
            else:
                bottom_layout.add_widget(in_layout)
        main_layout.add_widget(top_layout)
        main_layout.add_widget(bottom_layout)

        screen = Screen(name="main_menu")
        screen_calendar = Screen(name="calendar")
        screen_log = Screen(name="quick log")
        screen_summary = Screen(name="weekly summary")
        screen_meditation = Screen(name="meditation")

        screen.add_widget(main_layout)

        sm.add_widget(screen)
        sm.add_widget(screen_calendar)
        sm.add_widget(screen_log)
        sm.add_widget(screen_summary)
        sm.add_widget(screen_meditation)

        # add for loop for each option later

        #necessary for the code to run!
        return sm

if __name__ == '__main__':
    AwesomeApp().run()