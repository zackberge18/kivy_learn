from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image

#from different file
Builder.load_file("UpdateLabel.kv")
#from same file


class MyLayout(Widget):
    def press(self):
        name=self.ids.name_input.text
        #update the albel
        self.ids.name_label.text=name
        self.ids.name_input.text=""


        self.ids
class  MyApp(App):
    def build(self):
        #Background color
        return MyLayout()


if __name__ == '__main__':
    MyApp().run()