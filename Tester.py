from kivymd.app import MDApp
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.core.window import Window
# from kivymd.uix.button import Button
from kivymd.uix.button import MDRaisedButton
from kivy.uix.scrollview import ScrollView
from kivy.core.text import LabelBase
from kivy.uix.textinput import TextInput
from kivy.lang import Builder
from kivymd.toast import toast
import requests
from connected import *

LabelBase.register(name='DelaGothic', fn_regular='.\Assest\DelaGothicOne-Regular.ttf')
LabelBase.register(name='Mukta-Medium', fn_regular='.\Assest\Mukta-Medium.ttf')
LabelBase.register(name='Mukta-SemiBold', fn_regular='.\Assest\Mukta-SemiBold.ttf')
LabelBase.register(name='VarelaRound', fn_regular='.\Assest\VarelaRound-Regular.ttf')
Window.clearcolor = (1,1,1,1)


def checkemail(email):
    try:
        c1 = 0
        for i in range(len(email)):
            if email[i] == '@':
                end = email.split('@')
                c1 += 1
        if c1 == 0:
            return "Incorrect email."
        return ""
    except Exception as e:
        print(e)


def checkmis(mis):
    try:
        if len(mis) != 9:
            return "Invalid MIS."
        dept = mis[-4:]
        if dept.isdigit():
            value = int(dept)
            if value < 3000 or value > 3100:
                return "Error! MIS does not belong to Comp Dept."
            else:
                return ''
        else:
            return "Please enter MIS."
    except Exception as e:
        print(e)


class Login(Screen):
    Window.size = (800, 600)

    def do_login(self, user, email, mis):
        app = MDApp.get_running_app()
        
        app.username = user
        app.email = email
        app.mis = mis
        # e = ''
        # m = ''

        e = checkemail(app.email)
        m = checkmis(app.mis)
        if e == '':
            if m == '':
                f = open('mis.txt', 'a')
                f.write(str(app.mis))
                f.write('\n')
                f.close()
                self.ids.loginerror.text = ""
                self.manager.transition = SlideTransition(direction="left")
                self.manager.current = 'home'
                Window.size = (800, 600)
            else:
                self.ids.loginerror.text = m
                self.ids.mis.text = ""
        else:
            self.ids.loginerror.text = e
            self.ids.email.text = ""
    def resetForm(self):
        self.ids['email'].text = ""


class Tester(MDApp):
    username = StringProperty(None)
    password = StringProperty(None)
    dialog = None

    def build(self):
        manager = ScreenManager()
        manager.add_widget(Login(name='login'))
        self.theme_cls.primary_palette = 'Indigo'
        manager.add_widget(Home(name='home'))
        return manager

    def navigation_draw(self):
        print("Navigation")


if __name__ == '__main__':
    Tester().run()
