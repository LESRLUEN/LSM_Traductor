# main.py
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from gui.screens import MenuPrincipal

class LSMTraductorApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuPrincipal(name='menu'))
        return sm

if __name__ == '__main__':
    LSMTraductorApp().run()
