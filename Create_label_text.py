from kivymd.app import MDApp
from kivymd.uix.label import MDLabel,MDIcon

class DemoApp(MDApp):
    def build(self):
        my_label=MDLabel(text="hello world",halign="center",theme_text_color="Custom"
                         ,text_color=(128/256,0/256,128/256,1)
                         ,font_size=45)
        icon_label=MDIcon()
        return my_label

DemoApp().run()