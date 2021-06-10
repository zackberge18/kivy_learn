from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.image import Image

#from different file
Builder.load_file("SimpleCalculator.kv")
#from same file

##set the  app size

Window.size=(500,700)



class MyLayout(Widget):
    def clear(self,no):
        if no==1:
            self.ids.calc_input.text=""
        elif no==2:
            ex_number=self.ids.calc_input.text
            new_number=ex_number[:-1]
            self.ids.calc_input.text=new_number
    def press(self,number):
        ex_number=self.ids.calc_input.text
        self.ids.calc_input.text=ex_number+str(number)
    def add_fu(self,no):
        self.called=True
        if no==1:
            ex_number = self.ids.calc_input.text
            self.ids.calc_input.text = ex_number + "+"
        elif no==2:
            ex_number = self.ids.calc_input.text
            self.ids.calc_input.text = ex_number + "-"
        elif no==3:
            ex_number = self.ids.calc_input.text
            self.ids.calc_input.text = ex_number + "*"
        else:
            ex_number = self.ids.calc_input.text
            self.ids.calc_input.text = ex_number + "/"
    def equal_fu(self):
            ex_number=self.ids.calc_input.text
            self.ids.calc_input.text=str(eval(ex_number))
    def dot(self):
        ex_number = self.ids.calc_input.text
        dot_str=""
        if "." in ex_number:
            if self.called:
                dot_str=ex_number+"."
                self.ids.calc_input.text=dot_str
            else:
                pass
        else:
            self.ids.calc_input.text = ex_number +"."
        called=False
    def pos_neg(self):
        ex_number=self.ids.calc_input.text
        if "+" in ex_number :
            #pos_neg = ex_number[1:]
            #new_number="-"+pos_neg
            #self.ids.calc_input.text = new_number
            new_number=ex_number.replace("+","-")
            self.ids.calc_input.text = new_number
        elif "-" in ex_number:
            #new_number = "+" + ex_number[1:]
            #self.ids.calc_input.text = new_number
            new_number=ex_number.replace("-","+")
            self.ids.calc_input.text = new_number
        else:
            new_number = "+" +ex_number
            self.ids.calc_input.text = new_number







class  MyApp(App):
    def build(self):
        #Background color
        return MyLayout()


if __name__ == '__main__':
    MyApp().run()