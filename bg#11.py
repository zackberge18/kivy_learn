from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
#from different file
Builder.load_file("bg.kv")
#from same file


class MyLayout(Widget):
    pass
class  MyApp(App):
    def build(self):
        #Background color
        Window.clearcolor=(1,0,0,1)
        return MyLayout()


if __name__ == '__main__':
    MyApp().run()