from kivy.lang import Builder
from kivymd.app import MDApp

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style="Dark"
        self.theme_cls.primary_palette="Indigo"
        self.theme_cls.accent_palette= "Red"
        return Builder.load_file("bbutton.kv")
    def presser(self):
        self.root.ids.my_label.text = "you fuck that"

MainApp().run()

