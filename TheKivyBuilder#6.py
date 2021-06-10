from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
#from different file
#Builder.load_file("builder_kivy.kv")
#from same file
Builder.load_string("""
<MyGridLayout>
    name:name
    pizza:pizza
    color:color
    GridLayout:
        cols:1
        size:root.width,root.height

        GridLayout:
            cols:2

            Label:
                text:"name :"
            TextInput:
                id:name
                multiline:False
            Label:
                text:"pizza :"
            TextInput:
                multiline:False
                id:pizza
            Label:
                text:"color :"
            TextInput:
                multiline:False
                id:color
        Button:
            text:"Submit"
            font_size:40
            on_press:root.press()

""")

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