import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    # initialize infinite keyword
    def __init__(self, **kwargs):
        # call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        # set columns
        self.cols = 1
        self.row_force_default=True
        self.row_default_height=100
        self.col_force_default=True
        self.col_default_width=100

        #create a second grid
        self.topGrid=GridLayout(
            row_force_default=True,
            row_default_height=40,
            col_force_default=True,
            col_default_width=100
        )
        #set number of column
        self.topGrid.cols=2
        self.add_widget(self.topGrid)

        ##ad widgets
        self.topGrid.add_widget(Label(text="name: "))
        # add input box
        self.name = TextInput(multiline=False)
        self.topGrid.add_widget(self.name)
        ##ad widgets
        self.topGrid.add_widget(Label(text="pizza: "))
        # add input box
        self.pizza = TextInput(multiline=False)
        self.topGrid.add_widget(self.pizza)
        ##ad widgets
        self.topGrid.add_widget(Label(text="color: "))
        # add input box
        self.color = TextInput(multiline=False)
        self.topGrid.add_widget(self.color)
        self.submit = Button(text="submit",
                             font_size=100,
                             size_hint_y=None,
                             height=100,
                             size_hint_x=None,
                             width=600)
        # bind the button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text
        print(f"{name}+{pizza}+{color}")
        self.add_widget(Label(text=f"{name}+{pizza}+{color}"))
        ##cLEAN text boxes

        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()