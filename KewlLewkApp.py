import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button, ButtonBehavior
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader, Sound
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from kivy.uix.checkbox import CheckBox

#running with stated kivy version
kivy.require("1.11.1")


# create basic outfit dictionary

#create basic outfit dicitionary

outfit = {
    "black shirt" : "10211",
    "white jeans" : "20222",
    "black boots" : "11132",
    "red top" : "30441",
    "red jacket" : "30313",
    "yellow shorts" : "60421",
    "yellow raincoat" : "61211",
    "green winterjacket" : "41112"
    }


#
# initial
#

accepted_rain = 1,2
accepted_temperature = 1,2,3,4
accepted_style = 1,2,3,4
accepted_colour = 1,2,3,4,5,6

choice_rain = 0
choice_temperature = 0
choice_style = 0
choice_colour = 0

rain_options = ["Yes" , "No"]
temperature_options = ["<5" , "5-15" , "16-25" , ">25"]
style_options = ["cool" , "cosy" , "fancy" , "sexy"]
colour_options = ["black" , "white" , "red" , "blue" , "green" , "yellow"]




#start defining classes of the screens

class StartScreen(Screen):
    pass

class RainScreen(Screen):
    pass

class TempScreen(Screen):
    pass

class StyleScreen(Screen):
    pass

class ColourScreen(Screen):
    pass

class FinalScreen(Screen):
    pass

class ImageButton(ButtonBehavior, Image):
    pass

class TempBoxLayout(BoxLayout):
    pass


#using the Builder module to integrate kivy language files
GUI = Builder.load_file("main.kv")

class MainApp(App):
    def build(self):

        #setting the background to pink colour
        Window.clearcolor = (1, 0.7, 0.95, 1)

        #adding mp3 file via SoundLoader module
        sound = SoundLoader.load('Jamiroquai.mp3')
        sound.loop = True
        sound.play()

        return GUI

    def change_screen(self, screen_name):
        #Get the screen manager from the kv file

        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name

    def results_choices(self, choice_rain, choice_temperature, choice_style, choice_colour):
        #print the results of the choices that were made

        print(" ")
        print("rain: ", rain_options[choice_rain - 1])
        print("temperature: ", temperature_options[choice_temperature - 1])
        print("style: ", style_options[choice_style - 1])
        print("colour: ", colour_options[choice_colour - 1])
        print(" ")

if __name__ == "__main__":
    MainApp().run()