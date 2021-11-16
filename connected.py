from kivy.uix.screenmanager import Screen, SlideTransition
from kivymd.uix.button import MDRaisedButton
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.toast import toast
from kivy.core.window import Window

marks = 0
flag = 1


class Home(Screen):
    def disconnect(self):
        self.ids.que1.text = ''
        self.ids.que2.text = ''
        self.ids.que3.text = ''
        self.ids.que4.text = ''
        self.ids.que5.text = ''
        self.ids.que6.text = ''
        self.ids.que7.text = ''
        self.ids.que8.text = ''
        self.ids.que9.text = ''
        self.ids.que10.text = ''
        self.ids.ans1.text = ''
        self.ids.ans2.text = ''
        self.ids.ans3.text = ''
        self.ids.ans4.text = ''
        self.ids.ans5.text = ''
        self.ids.ans6.text = ''
        self.ids.ans7.text = ''
        self.ids.ans8.text = ''
        self.ids.ans9.text = ''
        self.ids.ans10.text = ''
        self.ids.marks.text = ''
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login')

    def checkint(self, value):
        try:
            if value.isdigit():
                return ""
            return "Entered value is not integer"
        except Exception as e:
            print(e)

    def checkfloat(self, value):
        if isinstance(value, float):
            return ""
        return "Entered value is not decimal"

    def check1(self, ans):
        try:
            if len(ans) > 4:
                self.ids.ans1.text = "Year should 4 digit."
            if ans.isdigit():
                if ans == '1969':
                    self.ids.ans1.text = "Correct answer!"
                    global marks
                    marks += 1
                elif int(ans) > 2021:
                    self.ids.ans1.text = "Year should be of before 2021."
                else:
                    self.ids.ans1.text = "Incorrect answer."
            else:
                self.ids.ans1.text = "Year should contain only digits."
        except Exception as e:
            print(e)

    def check2(self, ans):
        try:
            if '.' in ans:
                a = ans.split('.')
                if len(a) > 2:
                    self.ids.ans2.text = "Enter valid decimal!"
                else:
                    if a[0] == '2' and a[1] == '71':
                        self.ids.ans2.text = "Correct answer!"
                        global marks
                        marks += 1
                    else:
                        self.ids.ans2.text = "Incorrect answer!"
            else:
                self.ids.ans2.text = "Please enter a decimal value!"
        except Exception as e:
            print(e)

    def check3(self, ans):
        try:
            if ans.isdigit():
                self.ids.ans3.text = "Please enter a valid name"
            if ans == 'Berlin' or ans == 'berlin' or ans == 'BERLIN':
                self.ids.ans3.text = "Correct answer!"
                global marks
                marks += 1
            else:
                self.ids.ans3.text = 'Incorrect answer!'
        except Exception as e:
            print(e)

    def check4(self, ans):
        try:
            if '.' in ans:
                a = ans.split('.')
                if len(a) > 2:
                    self.ids.ans4.text = "Enter valid decimal!"
                else:
                    if a[0] == '15' and a[1] == '3405':
                        self.ids.ans4.text = "Correct answer!"
                        global marks
                        marks += 1
                    else:
                        self.ids.ans4.text = "Incorrect answer!"
            else:
                self.ids.ans4.text = "Please enter a decimal value!"
        except Exception as e:
            print(e)

    def check5(self, ans):
        try:
            if '.' in ans:
                a = ans.split('.')
                if len(a) != 4:
                    self.ids.ans5.text = "Enter a valid subnet mask!"
                else:
                    if a[0] == '255' and a[1] == '255' and a[2] == '0' and a[3] == '0':
                        self.ids.ans5.text = "Correct answer!"
                        global marks
                        marks += 1
                    else:
                        self.ids.ans5.text = "Incorrect answer!"
            else:
                self.ids.ans5.text = "Invalid subnet mask!"
        except Exception as e:
            print(e)

    def check6(self, ans):
        try:
            if ans.isdigit():
                if ans == '4':
                    self.ids.ans6.text = "Correct answer!"
                    global marks
                    marks += 1
                else:
                    self.ids.ans6.text = "Incorrect answer!"
            else:
                self.ids.ans6.text = "Please enter a digit!"
        except Exception as e:
            print(e)

    def check7(self, ans):
        try:
            if ans.isdigit():
                if ans == '1854':
                    self.ids.ans7.text = "Correct answer!"
                    global marks
                    marks += 1
                else:
                    self.ids.ans7.text = "Incorrect answer!"
            else:
                self.ids.ans7.text = "Please enter a digit!"
        except Exception as e:
            print(e)

    def check8(self, ans):
        try:
            if ans == '':
                self.ids.ans8.text = "Invalid MAC address"
            elif ':' in ans:
                a = ans.split(':')
                if len(a) != 6:
                    self.ids.ans8.text = "Invalid MAC address"
                else:
                    flag = True
                    for i in a:
                        if len(i) != 2:
                            self.ids.ans8.text = "Invalid MAC address"
                            flag = False
                            break
                        if not (('F' >= i[0] >= 'A') or ('f' >= i[0] >= 'a') or ('9' >= i[0] >= '0')):
                            flag = False
                        if not (('F' >= i[1] >= 'A') or ('f' >= i[1] >= 'a') or ('9' >= i[1] >= '0')):
                            flag = False
                    if flag:
                        self.ids.ans8.text = "Correct answer!"
                        global marks
                        marks += 1
                    else:
                        self.ids.ans8.text = "Incorrect answer!"
            else:
                self.ids.ans8.text = "Please enter a valid MAC address."
        except Exception as e:
            print(e)

    def check9(self, ans):
        try:
            if ans.isdigit():
                if ans == '1963':
                    self.ids.ans9.text = "Correct answer!"
                    global marks
                    marks += 1
                else:
                    self.ids.ans9.text = "Incorrect answer!"
            else:
                self.ids.ans9.text = "Please enter ans integer!"
        except Exception as e:
            print(e)

    def check10(self, ans):
        try:
            if ans.isdigit():
                self.ids.ans10.text = "Please enter an alphabet!"
            if ans == 'c' or ans == 'C':
                self.ids.ans10.text = "Correct answer!"
                global marks
                marks += 1
            else:
                self.ids.ans10.text = "Incorrect answer!"
        except Exception as e:
            print(e)

    def submit(self, que1, que2, que3, que4, que5, que6, que7, que8, que9, que10):
        global flag
        if flag:
            self.check1(que1)
            self.check2(que2)
            self.check3(que3)
            self.check4(que4)
            self.check5(que5)
            self.check6(que6)
            self.check7(que7)
            self.check8(que8)
            self.check9(que9)
            self.check10(que10)

            self.ids.marks.text = 'You have submitted the test successfully.    Total marks obtained = ' + str(marks)
            flag = 0
            f = open('mis.txt', 'a')
            f.write(str(marks))
            f.write('\n')
            f.close()
        else:
            self.ids.marks.text = 'You have submitted the test once.    Total marks obtained = ' + str(marks) + '   No more submission.'

