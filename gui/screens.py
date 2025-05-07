# gui/screens.py
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
import os

kv_path = os.path.join(os.path.dirname(__file__), 'menu_principal.kv')
Builder.load_file(kv_path)

class MenuPrincipal(Screen):
    pass
