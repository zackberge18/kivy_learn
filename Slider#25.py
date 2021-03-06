from kivy.lang import Builder
from kivymd.app import MDApp

KV = """
MDScreen:

    MDFlatButton:
        text: 'MDFlatButton'
        pos_hint: {'center_x': 0.5, 'center_y': 0.9}

    MDRaisedButton:
        text: 'MDRaisedButton'
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}

    MDRectangleFlatButton:
        text: 'MDRectangleFlatButton'
        pos_hint: {'center_x': 0.5, 'center_y': 0.7}

    MDRectangleFlatIconButton:
        icon: 'language-python'
        text: 'MDRectangleFlatIconButton'
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}

    MDRoundFlatButton:
        text: 'MDRoundFlatButton'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

    MDRoundFlatIconButton:
        icon: 'language-python'
        text: 'MDRoundFlatIconButton'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}

    MDFillRoundFlatIconButton:
        icon: 'language-python'
        text: 'MDFillRoundFlatIconButton'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}

    MDFillRoundFlatButton:
        text: 'MDFillRoundButton'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}

    MDTextButton:
        text: 'MDTextButton'
        pos_hint: {'center_x': 0.3, 'center_y': 0.1}

    MDIconButton:
        icon: 'language-python'
        pos_hint: {'center_x': 0.7, 'center_y': 0.1}

    MDFloatingActionButtonSpeedDial:
        data: app.data
        rotation_root_button: True

"""


class Example(MDApp):
    data = {
        "language-python": "Python",
        "language-php": "PHP",
        "language-cpp": "C++",
    }

    def build(self):
        return Builder.load_string(KV)


Example().run()
