from kivy.lang import Builder
from kivymd.app import MDApp

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style="Dark"
        self.theme_cls.primary_palette="Indigo"
        self.theme_cls.accent_palette= "Red"
        return Builder.load_string("""
BoxLayout:
    orientation: "vertical"

    MDToolbar:
        title:"bottom navbar"
        #md_bg_color:0.2,0.2,0.2,1
    MDBottomNavigation:
        #color stuff
        panel_color:0.5,0.5,0.5,1

        MDBottomNavigationItem:
            name:"screen1"
            text:"Python"
            icon:"language-python"

            MDLabel:
                name:"python"
                text:"python"
                halign: "center"
        MDBottomNavigationItem:
            name:"screen2"
            text:"instagram"
            icon:"language-python"

            MDLabel:
                name:"instagram"
                text:"instagram"
                halign: "center"

        MDBottomNavigationItem:
            name:"screen3"
            text:"codemy"
            icon:"language-python"

            MDLabel:
                name:"codemy"
                text:"codemy"
                halign: "center"
        """)
    def presser(self):
        self.root.ids.my_label.text = "you fuck that"

MainApp().run()

