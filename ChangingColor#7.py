from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
#from different file
Builder.load_file("ChangingColor.kv")
#from same file


class MyGridLayout(Widget):
    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)

    def press(self):
        name =  self.name.text
        pizza = self.pizza.text
        color = self.color.text
        print(f"{name}+{pizza}+{color}")
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""


class  MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()