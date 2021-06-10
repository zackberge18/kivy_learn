from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.spelling import Spelling

# Designate Our .kv design file
Builder.load_file('SpellChecker.kv')


class MyLayout(Widget):

    def press(self):
        #create a instance of spelling
        s=Spelling()

        #select the  language
        s.select_language("en_US")
        #grap word from text box
        word=self.ids.word_input.text

        option=s.suggest(word)
        x=""
        for i in option:
            x=f"{x} {i}"

        self.ids.word_label.text=f"{x}"



class AwesomeApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    AwesomeApp().run()
