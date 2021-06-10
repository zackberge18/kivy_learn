import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    #initialize infinite keyword
    def __init__(self,**kwargs):
        #call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)

        #set columns
        self.cols=2


        ##ad widgets
        self.add_widget(Label(text="name: "))
        #add input box
        self.name=TextInput(multiline=False)
        self.add_widget(self.name)
        ##ad widgets
        self.add_widget(Label(text="pizza: "))
        # add input box
        self.pizza = TextInput(multiline=False)
        self.add_widget(self.pizza)
        ##ad widgets
        self.add_widget(Label(text="color: "))
        # add input box
        self.color = TextInput(multiline=False)
        self.add_widget(self.color)
        self.submit=Button(text="submit",font_size=100)
        #bind the button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)
    def press(self,instance):
        name= self.name.text
        pizza=self.pizza.text
        color=self.color.text
        print(f"{name}+{pizza}+{color}")
        self.add_widget(Label(text=f"{name}+{pizza}+{color}"))
        ##cLEAN text boxes
        
        self.name.text=""
        self.pizza.text=""
        self.color.text=""

class MyApp(App):
    def build(self):
       return  MyGridLayout()



if __name__ == '__main__':
    MyApp().run()