from kivymd.app import MDApp
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.core.window import Window
import time
from kivy.clock import Clock, mainthread
from kivymd.uix.list import OneLineListItem
from kivymd.theming import ThemeManager
from kivymd.uix.picker import  MDThemePicker
from ScreenManager import Screen_build
from kivymd.uix.dialog import MDDialog
import time
from kivymd.uix.button import MDRectangleFlatButton
from kivy.config import Config
from kivy.animation import Animation
from kivy.uix.image import Image
Window.clearcolor = (1,1,0.4,1)
Window.size = (360, 600)




    
    
   
class ClassScreen(Screen):
    pass  
class WindowManager(Screen):
    pass
class BeginnerScreen(Screen):
    pass
class IntermediateScreen(Screen):
    pass
class AdvancedScreen(Screen):
    pass
    


sm = ScreenManager()

sm.add_widget(ClassScreen(name = 'class'))
sm.add_widget(WindowManager(name = 'first', ))
sm.add_widget(BeginnerScreen(name = 'basic'))
sm.add_widget(IntermediateScreen(name = 'mediate'))
sm.add_widget(AdvancedScreen(name = 'proff'))

class Tips_For_DlsApp(MDApp):
   
    
    
    def build(self):
        
        self.icon = 'strategy.png'
        self.theme_cls.primary_palette = 'Green'
        
        self.theme_cls.theme_style = 'Light'

        
    
        build_screen = Builder.load_string(Screen_build)
    
        
        return build_screen
   
    Theme_cls = ThemeManager()
    

    def show_theme(self):
        picker = MDThemePicker()
        picker.open()
    def coffee(self):
        pass
    
    def quit_data(self):
       
        yes_btn = MDRectangleFlatButton(text = 'Yes', on_release = quit)
        No_btn = MDRectangleFlatButton(text = 'No', on_release = self.close_dialog)

        self.dialog = MDDialog(title = 'QUIT',text = 'Are you sure you want to quit?',size_hint = (0.9, 1), buttons = [yes_btn, No_btn])
        self.dialog.open()
        


    def close_dialog(self, obj):
        self.dialog.dismiss()

if __name__ == "__main__":
    Tips_For_DlsApp().run()