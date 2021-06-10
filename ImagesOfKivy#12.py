from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image

#from different file
Builder.load_file("ImagesOfKivy.kv")
#from same file


class MyLayout(Widget):
    pass
class  MyApp(App):
    def build(self):
        #Background color
        Window.clearcolor=(1,1,1,1)
        return MyLayout()


if __name__ == '__main__':
    MyApp().run()