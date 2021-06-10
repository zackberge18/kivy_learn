import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


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


class  KivyDesingLanApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    KivyDesingLanApp().run()