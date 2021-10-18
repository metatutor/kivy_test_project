from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window



def getScreen():
    red = [1,0,0,.5]
    green = [0,1,0,.5]
    blue =  [0,0,1,.5]
    purple = [1,0,1,.5]

    button_padding = (100,100)
    options = ["Calendar", "Quick Log","Weekly Summary", "Meditation"]


    # this is the call back function that registers the four menu buttons 
    # also allows on button press to switch windows
    def on_press_button(instance):
        if instance.text == options[0]:
            print("hi")
        elif instance.text == options[1]:
            pass
        elif instance.text == options[2]:
            pass
        else: 
            print("we want to go back!")

    # this code defines the actual look of the calendar screen
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

    cs = Screen(name="calendar")
    cs.add_widget(main_layout)

    return cs