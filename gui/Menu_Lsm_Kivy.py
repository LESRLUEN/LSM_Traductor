from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

# Categorías del menú
categorias = [
    ("Familia", "👨‍👩‍👧‍👦"),
    ("Alimentos", "🍎"),
    ("Juguetes", "🚂"),
    ("Animales", "🦁"),
    ("Colores", "🎨"),
    ("Números", "🔢"),
    ("Abecedario", "🔠")
]

# Pantalla principal del menú
class MenuPrincipal(Screen):
    def __init__(self, **kwargs):
        super(MenuPrincipal, self).__init__(**kwargs)

        layout = GridLayout(cols=2, spacing=15, padding=30)

        for nombre, icono in categorias:
            btn = Button(
                text=f"{icono}\n{nombre}",
                font_size=24,
                background_color=(0.4, 0.7, 1, 1),
                color=(1, 1, 1, 1),
                size_hint=(1, None),
                height=120
            )
            btn.bind(on_press=self.on_categoria)
            layout.add_widget(btn)

        contenedor = BoxLayout(orientation='vertical')
        titulo = Label(text='Menú de Aprendizaje de Señas', font_size=30, size_hint=(1, 0.2))
        contenedor.add_widget(titulo)
        contenedor.add_widget(layout)

        self.add_widget(contenedor)

    def on_categoria(self, instance):
        print(f"Has presionado: {instance.text}")
        # Aquí puedes cambiar a una nueva pantalla dependiendo del botón

class AppLSM(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuPrincipal(name='menu'))
        return sm

if __name__ == '__main__':
    AppLSM().run()
