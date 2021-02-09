from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen,ScreenManager,CardTransition
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFillRoundFlatButton,MDIconButton
from kivymd.uix.label import MDIcon

Builder.load_string("""
<BackgroundColor@Widget>:
    background_color: (1, 1, 1, 1)
    canvas.before:
        Color:
            rgba: root.background_color
        Rectangle:
            size: self.size
            pos: self.pos
<ColorLabel@BackgroundColor+Label>:
    background_color:(135/255,0,106/255,1)
    color:(0,22/255,112/255,1)

<ColorTextInput@TextInput>:
    background_color:(135/255,0,106/255,1)

<InputScreen>:
    name : "input"
    BoxLayout:
        orientation: "horizontal"
        BoxLayout:
            size_hint : 0.3,1
            orientation:"vertical"
            canvas.before:
                Color:
                    rgba:(0,22/255,112/255,1)
                Rectangle:
                    size:self.size
                    pos:self.pos
            Label:
                size_hint:(1,0.3)
                text:"Elixir"
                font_size:"30sp"
            MDIconButton:
                size_hint:(1,.5)
                #pos_hint:{"center_x":.5,"center_y":.5}
                #icon:"home-variant-outline"
                icon:"home-circle-outline"
                theme_text_color:"Custom"
                text_color:(135/255,0,106/255,1)
                user_font_size: "80sp"
            MDIconButton:
                size_hint:(1,0.5)
                icon:"help"
                theme_text_color:"Custom"
                text_color :(135/255,0,106/255,1)
                user_font_size : "80sp"
            BoxLayout:
                
        RelativeLayout:
            canvas.before:
                Color:
                    rgba:(0,2/255,46/255,1)
                    #rgba:(.5,.5,.5,.5)
                Rectangle:
                    pos:root.pos
                    size:root.size
            BoxLayout:
                pos_hint: {"center_x":.5,"center_y":.5}
                size_hint : .5,.5
                orientation:"vertical"
                spacing:[30,50]
                GridLayout:
                    cols:2
                    rows:3
                    upStr : upStr
                    downStr : downStr
                    timePeriod : timePeriod
                    spacing:[0,20]
                    ColorLabel:
                        text:"Upstream Radius (Ru)"
                    TextInput:
                        id:upStr
                        fill_color:(.5,.5,0,1)
                        #hint_text: "Up stream Radius"
                        #hint_text_color: (1,0,0,1)
                    ColorLabel:
                        text:"Downstream Radius (Rd) "
                    TextInput:
                        id:downStr
                    ColorLabel:
                        text:"Time period"
                    TextInput:
                        id:timePeriod
                RelativeLayout:
                    size_hint:1,0.2  
                    MDFillRoundFlatButton:
                        text: "Submit"
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        md_bg_color: (135/255,0,106/255,1)
                        size_hint : 0.5,0.7
                        pos_hint:{'center_x':.5,'center_y':.5}
                        on_release:
                            app.root.current = "load"

<LoadingScreen>:
    name : "load"
    BoxLayout:
        orientation: "horizontal"
        BoxLayout:
            size_hint : 0.3,1
            orientation:"vertical"
            canvas.before:
                Color:
                    rgba:(0,22/255,112/255,1)
                Rectangle:
                    size:self.size
                    pos:self.pos
            Label:
                size_hint:(1,0.3)
                text:"Elixir"
            MDIconButton:
                size_hint:(1,.5)
                #pos_hint:{"center_x":.5,"center_y":.5}
                #icon:"home-variant-outline"
                icon:"home-circle-outline"
                theme_text_color:"Custom"
                text_color:(135/255,0,106/255,1)
                user_font_size: "80sp"
            MDIconButton:
                size_hint:(1,0.5)
                icon:"help"
                theme_text_color:"Custom"
                text_color :(135/255,0,106/255,1)
                user_font_size : "80sp"
            BoxLayout:
                
        RelativeLayout:
            canvas.before:
                Color:
                    rgba:(0,2/255,46/255,1)
                    #rgba:(.5,.5,.5,.5)
                Rectangle:
                    pos:root.pos
                    size:root.size
            
""")

class InputScreen(Screen):
    upStr = ObjectProperty(None)
    downStr = ObjectProperty(None)
    timePeriod = ObjectProperty(None)
    def on_enter(self):
        print("Entered input")
    
    def on_submit(self):
        #create the model object and then pass it to the loading screen
        """
        head = artery()
        LoadingScreen.arteryObj = head
        """
        pass

class LoadingScreen(Screen):
    arteryObj = None
    def on_enter(self):
        print("Entered test")
        for i in range(10000):
            print(i)
        app = App.get_running_app()
        app.root.current = "input"
        """
        ResultsScreen.model = self.arteryObj.sci_train()
        ResultsScreen.arteryObj = arteryObj
        app = App.get_running_app()
        app.root.current = "main"
        """

class ResultScreen(Screen):
    arteryObj = None
    model = None
    pass

class v1App(MDApp):
    def build(self):
        sm = ScreenManager(transition=CardTransition())
        sm.add_widget(InputScreen())
        sm.add_widget(LoadingScreen())
        return sm



if __name__ == "__main__":
    v1App().run()


