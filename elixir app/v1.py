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
import elixir as ex
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


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
            Image:
                source: "./Media/BlueCum.jpg"
                allow_stretch: True
                keep_ratio: False
            #canvas.before:
                #Color:
                    #rgba:(0,2/255,46/255,1)
                    #rgba:(.5,.5,.5,.5)
                #Rectangle:
                    #pos:root.pos
                    #size:root.size
                
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
            Image:
                source: "./Media/BlueCum.jpg"
                allow_stretch: True
                keep_ratio: False
            #canvas.before:
                #Color:
                    #rgba:(0,2/255,46/255,1)
                    #rgba:(.5,.5,.5,.5)
                #Rectangle:
                    #pos:root.pos
                    #size:root.size
                
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
            Image:
                source: "./Media/BlueCum.jpg"
                allow_stretch: True
                keep_ratio: False
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
            Image:
                source: "./Media/BlueCum.jpg"
                allow_stretch: True
                keep_ratio: False
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
            Image:
                source: "./Media/BlueCum.jpg"
                allow_stretch: True
                keep_ratio: False
            #canvas.before:
                #Color:
                    #rgba:(0,2/255,46/255,1)
                    #rgba:(.5,.5,.5,.5)
                #Rectangle:
                    #pos:root.pos
                    #size:root.size
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
            Image:
                source: "./Media/BlueCum.jpg"
                allow_stretch: True
                keep_ratio: False
            #canvas.before:
                #Color:
                    #rgba:(0,2/255,46/255,1)
                    #rgba:(.5,.5,.5,.5)
                #Rectangle:
                    #pos:root.pos
                    #size:root.size
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
                                app.root.current = "resultoption"
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
            Image:
                source: "./Media/BlueCum.jpg"
                allow_stretch: True
                keep_ratio: False
            #canvas.before:
                #Color:
                    #rgba:(0,2/255,46/255,1)
                    #rgba:(.5,.5,.5,.5)
                #Rectangle:
                    #pos:root.pos
                    #size:root.size
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
    im:im
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
                #Color:
                    #rgba:(0,2/255,46/255,1)
                    #rgba:(.5,.5,.5,.5)
                #Rectangle:
                    #pos:root.pos
                    #size:root.size
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
                    Image:
                        id:im
                        #source: root.graphimage
                        keep_ratio:False
                        allow_stretch:True
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
                
<RadiusOutputScreen>:
    name:"radiusoutput"
    im:im
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
                #Color:
                    #rgba:(0,2/255,46/255,1)
                    #rgba:(.5,.5,.5,.5)
                #Rectangle:
                    #pos:root.pos
                    #size:root.size
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
                    Image:
                        id:im
                        #source: root.graphimage
                        keep_ratio:False
                        allow_stretch:True
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
            Image:
                source: "./Media/BlueCum.jpg"
                allow_stretch: True
                keep_ratio: False
            #canvas.before:
                #Color:
                    #rgba:(0,2/255,46/255,1)
                    #rgba:(.5,.5,.5,.5)
                #Rectangle:
                    #pos:root.pos
                    #size:root.size
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
        head = ex.artery(Ru=float(self.upStr.text), Rd=float(self.downStr.text), timeperiod=float(self.timePeriod.text))
        LoadingScreen.arteryObj = head
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
        head = ex.artery(Ru=float(self.upStr.text), Rd=float(self.downStr.text), timeperiod=float(self.timePeriod.text), L=float(self.length.text),
                         delta_b=float(self.deltab.text), Reynolds_no=float(self.reynold.text), E=float(self.e.text), h=float(self.h.text),
                         q_0=float(self.qzer.text), activation=float(self.activation.text), num_train_samples=float(self.numsamp.text))
        LoadingScreen.arteryObj = head
        app = App.get_running_app()
        app.root.current = "load"

class LoadingScreen(Screen):
    arteryObj = None
    def on_enter(self):        
        ResultOptionScreen.model = self.arteryObj.sci_train()
        ResultOptionScreen.arteryObj = self.arteryObj
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
        self.r.text=self.arteryObj.q_network[[float(self.z.text), float(self.t.text)]]
        self.q.text=self.arteryObj.R_network[[self.z.text, float(self.t.text)]]

class FlowInputScreen(Screen):
    arteryObj = None
    t = ObjectProperty(None)
    def flowgraph(self):
        """name = plot(self.arteryObj.R_network, self.arteryObj.L, self.arteryObj.timeperiod, 'Flow')
        FlowOutputScreen.graphimage  = "./" + name"""
        GraphWaitScreenFlow.arteryObj = self.arteryObj
        GraphWaitScreenFlow.t = self.t.text
        app = App.get_running_app()
        app.root.current = "graphwaitflow"

class GraphWaitScreenFlow(Screen):
    arteryObj = None
    t = None
    def on_enter(self):
        name = plot(self.arteryObj.R_network, self.arteryObj.L, float(self.t), 'Flow')
        FlowOutputScreen.graphimage  = "./" + name
        app = App.get_running_app()
        app.root.current = "flowoutput"


class FlowOutputScreen(Screen):
    graphimage= ""
    im = ObjectProperty(None)
    def on_enter(self):
        self.im.source = self.graphimage
        print(self.graphimage)

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
        name = plot(self.arteryObj.q_network, self.arteryObj.L, float(self.t), 'Radii')
        RadiusOutputScreen.graphimage  = "./" + name
        app = App.get_running_app()
        app.root.current = "radiusoutput"
        


class RadiusOutputScreen(Screen):
    graphimage= ""
    im = ObjectProperty(None)
    def on_enter(self):
        self.im.source = self.graphimage
        print(self.graphimage)
    

def plot(network, length, time, plot_type):
    x = np.linspace(0, int(length), int(length)*10)
    print(x.shape)
    y = []
    for i in x:
        y.append(network.predict([[i, time]]))
    y = np.asarray(y).reshape((int(length)*10, ))
    print(y.shape)
    sns.set_style('darkgrid')
    sns.set(rc={'figure.figsize':(11.7, 8.27)})
    sns.set(font_scale=1.4)
    d = {'Lenght':x, plot_type:y}
    sns.lineplot(data=d, x='Lenght', y=plot_type, palette=('red',), linewidth=2.5).set_title(plot_type)
    value = plot_type + '_t_' + str(time) + '.png'
    plt.savefig(value)
    return value    
    
    
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
