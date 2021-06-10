from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image

#from different file
Builder.load_file("RoundButton.kv")
#from same file


class MyLayout(Widget):
    def press(self):
        print("Zack")
class  MyApp(App):
    def build(self):
        #Background color
        return MyLayout()


if __name__ == '__main__':
    MyApp().run()