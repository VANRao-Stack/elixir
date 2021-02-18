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
from kivy_garden.graph import Graph,MeshLinePlot,LinePlot
from math import sin
from kivy.utils import get_color_from_hex as rgb
from kivy.uix.modalview import ModalView
"""import elixir as ex
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np"""


Builder.load_string("""
<BackgroundColor@Widget>:
    background_color: (1, 1, 1, 1)
    canvas.before:
        Color:
            rgba: root.background_color
        Rectangle:
            size: self.size
            pos: self.pos
<HomeButton@MDIconButton>:
    icon:"home-circle-outline"
    theme_text_color:"Custom"
    #text_color:(135/255,0,106/255,1)
    text_color:(1,1,1,1)
    user_font_size: "80sp"
    on_release:
        app.root.current = "input"
<AboutButton@MDIconButton>:
    icon:"help"
    theme_text_color:"Custom"
    #text_color :(135/255,0,106/255,1)
    text_color:(1,1,1,1)
    user_font_size : "80sp"
<SideBar@BoxLayout>:
    orientation:"vertical"
    canvas.before:
        Color:
            rgba:(0/255,155/255,133/255,1)
        Rectangle:
            size:self.size
            pos:self.pos
    Label:
        size_hint:(1,0.3)
        text:"Elixir"
        font_size:"30sp"
    HomeButton:
        size_hint:(1,.5)
        #pos_hint:{"center_x":.5,"center_y":.5}
        #icon:"home-variant-outline"
    AboutButton:
        size_hint:(1,0.5)
    BoxLayout:
<ColorLabel@BackgroundColor+Label>:
    background_color:(0/255,155/255,133/255,1)
    color:(1,1,1,1)
<ColorTextInput@TextInput>:
    background_color:(135/255,0,106/255,1)
<InputScreen>:
    name : "input"
    upStr:upStr
    downStr:downStr
    timePeriod:timePeriod
    length:length
    BoxLayout:
        orientation: "horizontal"
        SideBar:
            size_hint : 0.3,1
      
        RelativeLayout:
            #Image:
            #    source: "./Media/BlueCum.jpg"
            #    allow_stretch: True
            #    keep_ratio: False
            canvas.before:
                Color:
                    rgba:(1,1,1,1)
                    #rgba:(.5,.5,.5,.5)
                Rectangle:
                    pos:root.pos
                    size:root.size
            BoxLayout:
                pos_hint: {"center_x":.5,"center_y":.5}
                size_hint : .6,.65
                orientation:"vertical"
                canvas.before:
                    Color:
                        rgba:(1,1,1,1)
                    Rectangle:
                        pos:self.pos
                        size:self.size
                GridLayout:
                    cols:2
                    rows:4
                    spacing:[0,20]
                    padding:[20,20]
                    size_hint: (1,.8)
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
                    ColorLabel:
                        text:"Length"
                    TextInput:
                        id:length
                BoxLayout:
                    orientation:"horizontal"
                    size_hint:1,0.1  
                    RelativeLayout:
                        MDFillRoundFlatButton:
                            text: "Advanced"
                            #text_size:self.width, None 
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            md_bg_color: (0/255,155/255,133/255,1)
                            size_hint : 0.5,0.7
                            pos_hint:{'center_x':.5,'center_y':.7}
                            on_release:
                                app.root.current = "advancedinput"
                    RelativeLayout:
                        MDFillRoundFlatButton:
                            text: "Submit"
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            md_bg_color: (0/255,155/255,133/255,1)
                            size_hint : 0.5,0.7
                            pos_hint:{'center_x':.5,'center_y':.7}
                            on_release:
                                root.on_submit()
<AdvancedInputScreen>:
    name : "advancedinput"
    upStr:upStr
    downStr:downStr
    timePeriod:timePeriod
    length:length
    deltab:deltab
    reynold:reynold
    e:e
    h:h
    qzer:qzer
    activation:activation
    numsamp:numsamp
    BoxLayout:
        orientation: "horizontal"
        SideBar:
            size_hint : 0.3,1
      
        RelativeLayout:
            #Image:
            #    source: "./Media/BlueCum.jpg"
            #    allow_stretch: True
            #    keep_ratio: False
            canvas.before:
                Color:
                    rgba:(1,1,1,1)
                    #rgba:(.5,.5,.5,.5)
                Rectangle:
                    pos:root.pos
                    size:root.size
                
            BoxLayout:
                pos_hint: {"center_x":.5,"center_y":.5}
                size_hint : .7,.8
                orientation:"vertical"
                canvas.before:
                    Color:
                        rgba:(1,1,1,1)
                    Rectangle:
                        pos:self.pos
                        size:self.size
                GridLayout:
                    cols:2
                    rows:11
                    spacing:[0,10]
                    padding:[20,20]
                    size_hint: (1,.8)
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
                    
                    ColorLabel:
                        text:"Length"
                    TextInput:
                        id:length
                    
                    ColorLabel:
                        text:"Delta B"
                    TextInput:
                        id:deltab
                    
                    ColorLabel:
                        text:"Reynold's Number"
                    TextInput:
                        id:reynold
                    
                    ColorLabel:
                        text:"E"
                    TextInput:
                        id:e
                    
                    ColorLabel:
                        text:"H"
                    TextInput:
                        id:h
                    
                    ColorLabel:
                        text:"q_0"
                    TextInput:
                        id:qzer
                    
                    ColorLabel:
                        text:"Activation"
                    TextInput:
                        id:activation
                    
                    ColorLabel:
                        text:"Sample Count"
                    TextInput:
                        id:numsamp
                    
                BoxLayout:
                    orientation:"horizontal"
                    size_hint:1,0.1  
                    RelativeLayout:
                        MDFillRoundFlatButton:
                            text: "Back"
                            #text_size:self.width, None 
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            md_bg_color: (0/255,155/255,133/255,1)
                            size_hint : 0.5,0.7
                            pos_hint:{'center_x':.5,'center_y':.7}
                            on_release:
                                app.root.current = "input"
                    RelativeLayout:
                        MDFillRoundFlatButton:
                            text: "Submit"
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            md_bg_color: (0/255,155/255,133/255,1)
                            size_hint : 0.5,0.7
                            pos_hint:{'center_x':.5,'center_y':.7}
                            on_release:
                                root.on_submit()
<LoadingScreen>:
    name : "load"
    BoxLayout:
        orientation: "horizontal"
        SideBar:
            size_hint : 0.3,1     
        RelativeLayout:
            Image:
                source: "./Media/BlueCum.jpg"
                allow_stretch: True
                keep_ratio: False
            #canvas.before:
            #    Color:
            #        rgba:(1,1,1,1)
            #        #rgba:(.5,.5,.5,.5)
            #    Rectangle:
            #        pos:root.pos
            #        size:root.size
            Label:
                pos_hint: {"center_x":0.5, "center_y":0.5}
                size_hint: (1, 0.3)
                text: "Loading..."
                font_size: "30sp"
<GraphWaitScreenRadius>:
    name : "graphwaitradius"
    BoxLayout:
        orientation: "horizontal"
        SideBar:
            size_hint : 0.3,1     
        RelativeLayout:
            #Image:
            #    source: "./Media/BlueCum.jpg"
            #    allow_stretch: True
            #    keep_ratio: False
            canvas.before:
                Color:
                    rgba:(1,1,1,1)
                    #rgba:(.5,.5,.5,.5)
                Rectangle:
                    pos:root.pos
                    size:root.size
            Label:
                pos_hint: {"center_x":0.5, "center_y":0.5}
                size_hint: (1, 0.3)
                text: "Loading..."
                font_size: "30sp"
<GraphWaitScreenFlow>:
    name : "graphwaitflow"
    BoxLayout:
        orientation: "horizontal"
        SideBar:
            size_hint : 0.3,1     
        RelativeLayout:
            #Image:
            #    source: "./Media/BlueCum.jpg"
            #    allow_stretch: True
            #    keep_ratio: False
            canvas.before:
                Color:
                    rgba:(1,1,1,1)
                    #rgba:(.5,.5,.5,.5)
                Rectangle:
                    pos:root.pos
                    size:root.size
            Label:
                pos_hint: {"center_x":0.5, "center_y":0.5}
                size_hint: (1, 0.3)
                text: "Loading..."
                font_size: "30sp"
<ResultOptionScreen>:
    name : "resultoption"
    BoxLayout:
        orientation: "horizontal"
        SideBar:
            size_hint : 0.3,1
        RelativeLayout:
            #Image:
            #    source: "./Media/BlueCum.jpg"
            #    allow_stretch: True
            #    keep_ratio: False
            canvas.before:
                Color:
                    rgba:(1,1,1,1)
                    #rgba:(.5,.5,.5,.5)
                Rectangle:
                    pos:root.pos
                    size:root.size
            BoxLayout:
                pos_hint: {"center_x":.5,"center_y":.5}
                size_hint : .6,.65
                #padding:[20,20]
                #spacing:[0,20]
                orientation:"vertical"
                canvas.before:
                    Color:
                        rgba:(1,1,1,1)
                    Rectangle:
                        size:self.size
                        pos:self.pos
                RelativeLayout:
                    MDFillRoundFlatButton:
                        text: "Predictor"
                        font_size:"20sp"
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        md_bg_color: (0/255,155/255,133/255,1)
                        size_hint : 0.7,0.6
                        pos_hint:{'center_x':.5,'center_y':.5}
                        on_release:
                            root.predictor()
                RelativeLayout:
                    MDFillRoundFlatButton:
                        text: "Flow Graph"
                        font_size:"20sp"
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        md_bg_color: (0/255,155/255,133/255,1)
                        size_hint : 0.7,0.6
                        pos_hint:{'center_x':.5,'center_y':.5}
                        on_release:
                            root.flow()
                RelativeLayout:
                    MDFillRoundFlatButton:
                        text: "Radii Graph"
                        font_size:"20sp"
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        md_bg_color: (0/255,155/255,133/255,1)
                        size_hint : 0.7,0.6
                        pos_hint:{'center_x':.5,'center_y':.5}  
                        on_release:
                            root.radius()
<PredictorScreen>:
    name:"predictor"
    z:z
    t:t
    q:q
    r:r
    BoxLayout:
        orientation: "horizontal"
        SideBar:
            size_hint : 0.3,1
        RelativeLayout:
            #Image:
            #    source: "./Media/BlueCum.jpg"
            #    allow_stretch: True
            #    keep_ratio: False
            canvas.before:
                Color:
                    rgba:(1,1,1,1)
                    #rgba:(.5,.5,.5,.5)
                Rectangle:
                    pos:root.pos
                    size:root.size
            BoxLayout:
                pos_hint: {"center_x":.5,"center_y":.5}
                size_hint : .6,.65
                #padding:[20,20]
                #spacing:[0,20]
                orientation:"vertical"
                canvas.before:
                    Color:
                        rgba:(1,1,1,1)
                    Rectangle:
                        size:self.size
                        pos:self.pos   
                GridLayout:
                    cols:2
                    rows:4
                    spacing:[0,20]
                    padding:[20,20]
                    size_hint: (1,.8)
                    ColorLabel:
                        text:"Location (z)"
                    TextInput:
                        id:z
                        fill_color:(.5,.5,0,1)
                        #hint_text: "Up stream Radius"
                        #hint_text_color: (1,0,0,1)
                    ColorLabel:
                        text:"Time (t) "
                    TextInput:
                        id:t
                    ColorLabel:
                        text:"Predicted q"
                    ColorLabel:
                        id:q
                        background_color:(1,1,1,1)
                        color:(0,0,0,1)
                        #text:""
                    ColorLabel:
                        text:"Predicted R"
                    ColorLabel:
                        id:r
                        background_color:(1,1,1,1)
                        color:(0,0,0,1)
                        #text:""
                BoxLayout:
                    orientation:"horizontal"
                    size_hint:(1,.2)
                    RelativeLayout:
                        MDFillRoundFlatButton:
                            text:"Back"
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            md_bg_color: (0/255,155/255,133/255,1)
                            size_hint : 0.7,0.6
                            pos_hint:{'center_x':.5,'center_y':.5}
                            on_release:
                                #app.root.current = "resultoption"
                                app.root.current = "input"
                    RelativeLayout:
                        
                        MDFillRoundFlatButton:
                            text:"Compute"
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            md_bg_color: (0/255,155/255,133/255,1)
                            size_hint : 0.7,0.6
                            pos_hint:{'center_x':.5,'center_y':.5}
                            on_release:
                                root.predict()
                
<FlowInputScreen>:
    name:"flowinput"
    t:t
    BoxLayout:
        orientation: "horizontal"
        SideBar:
            size_hint : 0.3,1
        RelativeLayout:
            #Image:
            #    source: "./Media/BlueCum.jpg"
            #    allow_stretch: True
            #    keep_ratio: False
            canvas.before:
                Color:
                    rgba:(1,1,1,1)
                    #rgba:(.5,.5,.5,.5)
                Rectangle:
                    pos:root.pos
                    size:root.size
            BoxLayout:
                pos_hint: {"center_x":.5,"center_y":.5}
                size_hint : .7,.4
                #padding:[20,20]
                #spacing:[0,20]
                orientation:"vertical"
                canvas.before:
                    Color:
                        rgba:(1,1,1,1)
                    Rectangle:
                        size:self.size
                        pos:self.pos   
                #BoxLayout:
                BoxLayout:
                    orientation:"vertical"
                    spacing:[0,20]
                    padding:[20,20]
                    #size_hint: (1,.8)
                    BoxLayout:
                        ColorLabel:
                            text:"Time Value (t)"
                        TextInput:
                            id:t
                            fill_color:(.5,.5,0,1)
                            #hint_text: "Up stream Radius"
                            #hint_text_color: (1,0,0,1)
                #BoxLayout:
                BoxLayout:
                    orientation:"horizontal"
                    #size_hint:(1,.2)
                    RelativeLayout:
                        MDFillRoundFlatButton:
                            text:"Back"
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            md_bg_color: (0/255,155/255,133/255,1)
                            size_hint : 0.7,0.4
                            pos_hint:{'center_x':.5,'center_y':.5}
                            on_release:
                                app.root.current = "resultoption"
                    RelativeLayout:
                        
                        MDFillRoundFlatButton:
                            text:"Plot Graph"
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            md_bg_color: (0/255,155/255,133/255,1)
                            size_hint : 0.7,0.4
                            pos_hint:{'center_x':.5,'center_y':.5}
                            on_release:
                                root.flowgraph()
<FlowOutputScreen>:
    name:"flowoutput"
    #im:im
    box:box
    BoxLayout:
        orientation: "horizontal"
        SideBar:
            size_hint : 0.3,1
        RelativeLayout:
            #Image:
            #    source: "./Media/BlueCum.jpg"
            #    allow_stretch: True
            #    keep_ratio: False
            canvas.before:
                Color:
                    rgba:(1,1,1,1)
                    #rgba:(.5,.5,.5,.5)
                Rectangle:
                    pos:root.pos
                    size:root.size
            BoxLayout:
                pos_hint: {"center_x":.5,"center_y":.5}
                size_hint : .7,.65
                #padding:[20,20]
                #spacing:[0,20]
                orientation:"vertical"
                canvas.before:
                    Color:
                        rgba:(1,1,1,1)
                    Rectangle:
                        size:self.size
                        pos:self.pos   
                #BoxLayout:
                BoxLayout:
                    id:box
                    size_hint:1,.8
                    canvas.before:
                        Color:
                            rgba:(1,1,1,1)
                        Rectangle:
                            size:self.size
                            pos:self.pos
                    #Image:
                    #    id:im
                        #source: root.graphimage
                    #    keep_ratio:False
                    #    allow_stretch:True
                #BoxLayout:
                RelativeLayout:
                    size_hint:1,.2
                    MDFillRoundFlatButton:
                        text:"Back"
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        md_bg_color: (0/255,155/255,133/255,1)
                        size_hint : 0.5,0.4
                        pos_hint:{'center_x':.5,'center_y':.5}
                        on_release:
                            app.root.current = "resultoption"
                
<RadiusOutputScreen>:
    name:"radiusoutput"
    #im:im
    BoxLayout:
        orientation: "horizontal"
        SideBar:
            size_hint : 0.3,1
        RelativeLayout:
            #Image:
            #    source: "./Media/BlueCum.jpg"
            #    allow_stretch: True
            #    keep_ratio: False
            canvas.before:
                Color:
                    rgba:(1,1,1,1)
                    #rgba:(.5,.5,.5,.5)
                Rectangle:
                    pos:root.pos
                    size:root.size
            BoxLayout:
                pos_hint: {"center_x":.5,"center_y":.5}
                size_hint : .7,.6
                #padding:[20,20]
                #spacing:[0,20]
                orientation:"vertical"
                canvas.before:
                    Color:
                        rgba:(1,1,1,1)
                    Rectangle:
                        size:self.size
                        pos:self.pos   
                #BoxLayout:
                BoxLayout:
                    size_hint:1,.7
                    #Image:
                    #    id:im
                        #source: root.graphimage
                    #    keep_ratio:False
                    #    allow_stretch:True
                #BoxLayout:
                RelativeLayout:
                    size_hint:1,.3
                    MDFillRoundFlatButton:
                        text:"Back"
                        theme_text_color: "Custom"
                        text_color: 1, 1, 1, 1
                        md_bg_color: (0/255,155/255,133/255,1)
                        size_hint : 0.7,0.3
                        pos_hint:{'center_x':.5,'center_y':.5}
                        on_release:
                            app.root.current = "resultoption"
                
<RadiusInputScreen>:
    name:"radiusinput"
    t:t
    BoxLayout:
        orientation: "horizontal"
        SideBar:
            size_hint : 0.3,1
        RelativeLayout:
            #Image:
            #    source: "./Media/BlueCum.jpg"
            #    allow_stretch: True
            #    keep_ratio: False
            canvas.before:
                Color:
                    rgba:(1,1,1,1)
                    #rgba:(.5,.5,.5,.5)
                Rectangle:
                    pos:root.pos
                    size:root.size
            BoxLayout:
                pos_hint: {"center_x":.5,"center_y":.5}
                size_hint : .7,.4
                #padding:[20,20]
                #spacing:[0,20]
                orientation:"vertical"
                canvas.before:
                    Color:
                        rgba:(1,1,1,1)
                    Rectangle:
                        size:self.size
                        pos:self.pos   
                #BoxLayout:
                BoxLayout:
                    orientation:"vertical"
                    spacing:[0,20]
                    padding:[20,20]
                    #size_hint: (1,.8)
                    BoxLayout:
                        ColorLabel:
                            text:"Time Value (t)"
                        TextInput:
                            id:t
                            fill_color:(.5,.5,0,1)
                            #hint_text: "Up stream Radius"
                            #hint_text_color: (1,0,0,1)
                #BoxLayout:
                BoxLayout:
                    orientation:"horizontal"
                    #size_hint:(1,.2)
                    RelativeLayout:
                        MDFillRoundFlatButton:
                            text:"Back"
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            md_bg_color: (0/255,155/255,133/255,1)
                            size_hint : 0.7,0.4
                            pos_hint:{'center_x':.5,'center_y':.5}
                            on_release:
                                app.root.current = "resultoption"
                    RelativeLayout:
                        
                        MDFillRoundFlatButton:
                            text:"Plot Graph"
                            theme_text_color: "Custom"
                            text_color: 1, 1, 1, 1
                            md_bg_color: (0/255,155/255,133/255,1)
                            size_hint : 0.7,0.4
                            pos_hint:{'center_x':.5,'center_y':.5}
                            on_release:
                                root.radiusgraph()                     
""")

class InputScreen(Screen):
    upStr = ObjectProperty(None)
    downStr = ObjectProperty(None)
    timePeriod = ObjectProperty(None)
    length = ObjectProperty(None)
    def on_enter(self):
        print("Entered input")

    
    def on_submit(self):
        #create the model object and then pass it to the loading screen
        """head = ex.artery(Ru=float(self.upStr.text), Rd=float(self.downStr.text), timeperiod=float(self.timePeriod.text))
        LoadingScreen.arteryObj = head"""
        #print(self.upStr.text)
        app = App.get_running_app()
        app.root.current = "load"

class AdvancedInputScreen(Screen):
    upStr = ObjectProperty(None)
    downStr = ObjectProperty(None)
    timePeriod = ObjectProperty(None)
    length = ObjectProperty(None)
    deltab = ObjectProperty(None)
    reynold = ObjectProperty(None)
    e = ObjectProperty(None)
    h = ObjectProperty(None)
    qzer = ObjectProperty(None)
    activation = ObjectProperty(None)
    numsamp = ObjectProperty(None)
    def on_submit(self):
        if(self.upStr.text == ""):
            print("Empty")
        """head = ex.artery(Ru=float(self.upStr.text), Rd=float(self.downStr.text), timeperiod=float(self.timePeriod.text), L=float(self.length.text),
                         delta_b=float(self.deltab.text), Reynolds_no=float(self.reynold.text), E=float(self.e.text), h=float(self.h.text),
                         q_0=float(self.qzer.text), activation=float(self.activation.text), num_train_samples=float(self.numsamp.text))
        LoadingScreen.arteryObj = head"""
        app = App.get_running_app()
        app.root.current = "load"

class LoadingScreen(Screen):
    arteryObj = None
    """def on_enter(self):        
        ResultOptionScreen.model = self.arteryObj.sci_train()
        ResultOptionScreen.arteryObj = self.arteryObj
        app = App.get_running_app()
        app.root.current = "resultoption"""
    def on_enter(self):
        PredictorScreen.arteryObj = self.arteryObj
        app = App.get_running_app()
        app.root.current = "resultoption"


class ResultOptionScreen(Screen):
    arteryObj = None
    model = None
    def predictor(self):
        PredictorScreen.arteryObj = self.arteryObj
        app = App.get_running_app()
        app.root.current = "predictor"
    def flow(self):
        FlowInputScreen.arteryObj = self.arteryObj
        app = App.get_running_app()
        app.root.current = "flowinput"

    def radius(self):
        RadiusInputScreen.arteryObj = self.arteryObj
        app = App.get_running_app()
        app.root.current = "radiusinput"


class PredictorScreen(Screen):
    arteryObj = None
    z  = ObjectProperty(None)
    t = ObjectProperty(None)
    r = ObjectProperty(None)
    q = ObjectProperty(None)
    def predict(self):
        #print("predicting")
        """self.r.text=self.arteryObj.q_network[[float(self.z.text), float(self.t.text)]]
        self.q.text=self.arteryObj.R_network[[self.z.text, float(self.t.text)]]"""

class FlowInputScreen(Screen):
    arteryObj = None
    t = ObjectProperty(None)
    def flowgraph(self):
        GraphWaitScreenFlow.arteryObj = self.arteryObj
        GraphWaitScreenFlow.t = self.t.text
        app = App.get_running_app()
        app.root.current = "graphwaitflow"

class GraphWaitScreenFlow(Screen):
    arteryObj = None
    t = None
    def on_enter(self):
        """Write the code to generate x and y here
        FlowOutputScreen.x =
        FlowOutputScreen.y =
        """
        app = App.get_running_app()
        app.root.current = "flowoutput"


class FlowOutputScreen(Screen):
    box = ObjectProperty(None)
    x = None
    y = None
    def on_enter(self):
        #self.im.source = self.graphimage
        """self.box.add_widget(test_plot())
        print(self.graphimage)"""
        view = ModalView(size_hint = (.8,.8))
        view.add_widget(test_plot())
        view.open()
        view.bind(on_dismiss = return_options)
    def on_leave(self):
        #self.box.remove_widget(self.box.children[0])
        pass

def return_options(instance):
    app = App.get_running_app()
    app.root.current = "resultoption"


class RadiusInputScreen(Screen):
    arteryObj = None
    t = ObjectProperty(None)
    def radiusgraph(self):
        #name = plot(self.arteryObj.q_network, self.arteryObj.L, self.arteryObj.timeperiod, 'Radii')
        #RadiusOutputScreen.graphimage  = "./" + name
        GraphWaitScreenRadius.arteryObj = self.arteryObj
        GraphWaitScreenRadius.t = self.t.text
        app = App.get_running_app()
        app.root.current = "graphwaitradius"

class GraphWaitScreenRadius(Screen):
    arteryObj = None
    t = None
    def on_enter(self):
        """name = plot(self.arteryObj.q_network, self.arteryObj.L, float(self.t), 'Radii')
        RadiusOutputScreen.graphimage  = "./" + name"""
        app = App.get_running_app()
        app.root.current = "radiusoutput"
        


class RadiusOutputScreen(Screen):
    graphimage= ""
    #im = ObjectProperty(None)
    def on_enter(self):
        #self.im.source = self.graphimage
        print(self.graphimage)
    
    
    
def test_plot():
    y=[0.031950610693602964,
    0.03194481197500933,
    0.031839240899471946,
    0.03261149720875123,
    0.035318570120934784,
    0.03878313701866755,
    0.04238573613993061,
    0.04602413486857117,
    0.049741388844395724,
    0.053591512586388015,
    0.057606653444064085,
    0.061798281482847446,
    0.06616619371831864,
    0.0707062524112668,
    0.07541470788936075,
    0.08028950738455903,
    0.08532965250364388,
    0.09053359512583906,
    0.09589739645656445,
    0.10141312243613443,
    0.10706775198182189,
    0.11284272335879741,
    0.11871412956181746,
    0.12465349436310197,
    0.1306290141769961,
    0.1366071294269646,
    0.14255428226160094,
    0.1484387168495126,
    0.15423218045233464,
    0.15991138889658346,
    0.16545913220539737,
    0.17086491832798104,
    0.176125086824129,
    0.18124236932291862,
    0.18622492632543908,
    0.19108494492368985,
    0.19583693205010577,
    0.20049587508848127,
    0.2050754590083632,
    0.2095865221197838,
    0.21403590069691683,
    0.2184257606264228,
    0.22275345085200954,
    0.22701185011711789,
    0.23119012625285065,
    0.23527479343151592,
    0.23925093946222153,
    0.24310349904366838,
    0.2468184631414876,
    0.25038393206695747,
    0.25379093551614873,
    0.2570339559133069,
    0.26011110492845285,
    0.2630239222658207,
    0.2657767956181362,
    0.26837604287000977,
    0.2708287490501172,
    0.2731415024832031,
    0.27531921410167887,
    0.2773642168267341,
    0.27927581763589904,
    0.2810504108810505,
    0.28268216626034237,
    0.28416419784337715,
    0.28549002679100144,
    0.28665509308698073,
    0.2876580643255614,
    0.2885017321566062,
    0.2891933663280758,
    0.2897444921164648,
    0.29017014919693107,
    0.29048776440199314,
    0.2907158204324336,
    0.29087252503362143,
    0.290974677705853,
    0.2910368879299887,
    0.2910712155395291,
    0.29108718966409003,
    0.2910920569869775,
    0.29109107980726506,
    0.29108779054557926,
    0.29108424496737106,
    0.2910813563042657,
    0.29107930058783893,
    0.29107789553986657,
    0.29107687143375244,
    0.2910760178074271,
    0.2910752294093475,
    0.291074487069738,
    0.2910738129705285,
    0.29107323261915635,
    0.29107275708711505,
    0.29107238191483087,
    0.2910720931782799,
    0.2910718738295515,
    0.29107170774258234,
    0.2910715814876797,
    0.29107148466392946,
    0.2910714095496088,
    0.29107135054217537]
    x = [0.0,
    0.10101010101010101,
    0.20202020202020202,
    0.30303030303030304,
    0.40404040404040403,
    0.5050505050505051,
    0.6060606060606061,
    0.7070707070707071,
    0.8080808080808081,
    0.9090909090909091,
    1.0101010101010102,
    1.1111111111111112,
    1.2121212121212122,
    1.3131313131313131,
    1.4141414141414141,
    1.5151515151515151,
    1.6161616161616161,
    1.7171717171717171,
    1.8181818181818181,
    1.9191919191919191,
    2.0202020202020203,
    2.121212121212121,
    2.2222222222222223,
    2.323232323232323,
    2.4242424242424243,
    2.525252525252525,
    2.6262626262626263,
    2.727272727272727,
    2.8282828282828283,
    2.929292929292929,
    3.0303030303030303,
    3.131313131313131,
    3.2323232323232323,
    3.3333333333333335,
    3.4343434343434343,
    3.5353535353535355,
    3.6363636363636362,
    3.7373737373737375,
    3.8383838383838382,
    3.9393939393939394,
    4.040404040404041,
    4.141414141414141,
    4.242424242424242,
    4.343434343434343,
    4.444444444444445,
    4.545454545454545,
    4.646464646464646,
    4.747474747474747,
    4.848484848484849,
    4.94949494949495,
    5.05050505050505,
    5.151515151515151,
    5.252525252525253,
    5.353535353535354,
    5.454545454545454,
    5.555555555555555,
    5.656565656565657,
    5.757575757575758,
    5.858585858585858,
    5.959595959595959,
    6.0606060606060606,
    6.161616161616162,
    6.262626262626262,
    6.363636363636363,
    6.4646464646464645,
    6.565656565656566,
    6.666666666666667,
    6.767676767676767,
    6.8686868686868685,
    6.96969696969697,
    7.070707070707071,
    7.171717171717171,
    7.2727272727272725,
    7.373737373737374,
    7.474747474747475,
    7.575757575757575,
    7.6767676767676765,
    7.777777777777778,
    7.878787878787879,
    7.979797979797979,
    8.080808080808081,
    8.181818181818182,
    8.282828282828282,
    8.383838383838384,
    8.484848484848484,
    8.585858585858587,
    8.686868686868687,
    8.787878787878787,
    8.88888888888889,
    8.98989898989899,
    9.09090909090909,
    9.191919191919192,
    9.292929292929292,
    9.393939393939394,
    9.494949494949495,
    9.595959595959595,
    9.696969696969697,
    9.797979797979798,
    9.8989898989899,
    10.0]

    label_options = {
                'color': rgb('009B85'),  # color of tick labels and titles
                'bold': True}
    graph = Graph(xlabel='X', ylabel='Y',
    x_ticks_major=(max(x)-min(x))/10, y_ticks_major=(max(y) - min(y))/5,
    y_grid_label=True, x_grid_label=True, padding=5,
    x_grid=True, y_grid=True, xmin=min(x), xmax=max(x) + 1, ymin=min(y), background_color = (1,1,1,.9), ymax=max(y) + .1,border_color = (0,0,0,1),label_options = label_options)
    plot = LinePlot(color=[0/255,155/255,133/255,1])
    plot.line_width = "2px"
    plot.points = list(zip(x,y))
    graph.add_plot(plot)
    return graph

class v1App(MDApp):
    def build(self):
        sm = ScreenManager(transition=CardTransition())
        sm.add_widget(InputScreen())
        sm.add_widget(LoadingScreen())
        sm.add_widget(ResultOptionScreen())
        sm.add_widget(PredictorScreen())
        sm.add_widget(FlowInputScreen())
        sm.add_widget(FlowOutputScreen())
        sm.add_widget(RadiusInputScreen())
        sm.add_widget(RadiusOutputScreen())
        sm.add_widget(AdvancedInputScreen())
        sm.add_widget(GraphWaitScreenRadius())
        sm.add_widget(GraphWaitScreenFlow())
        return sm



if __name__ == "__main__":
    v1App().run()
