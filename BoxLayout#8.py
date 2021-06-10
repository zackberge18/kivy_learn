from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
#from different file
Builder.load_file("BoxLayout.kv")
#from same file


class MyLayout(Widget):
    pass





class  MyApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    MyApp().run()