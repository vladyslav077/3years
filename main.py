from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager


class Winder(Screen):


  def __init__(self, **kw):
    super().__init__(**kw)
    line = BoxLayout(orientation='horizontal')
    lin5 = BoxLayout(orientation='vertical')
    helboy = Label(text='Hi, ШПІЦ')
    line.add_widget(helboy)
    kipish = Button(text='Г')
    kipis1 = Button(text='Е')
    kipis2 = Button(text='М')
    kipis3 = Button(text='Б')
    line.add_widget(lin5)
    lin5.add_widget(kipish)
    lin5.add_widget(kipis1)
    lin5.add_widget(kipis2)
    lin5.add_widget(kipis3)
    self.add_widget(line)


class SecondWinder(Screen):


  def __init__(self, **kw):
    super().__init__(**kw)
    line = BoxLayout(orientation='vertical')
    one = Button(text='SecondWindow', on_press=self.second())
    line.add_widget(one)
    self.add_widget(line)


def second(self):
    print(123)


class MyApp(App):


  def build(self):
    sm = ScreenManager()
    sm.add_widget(Winder())

    return sm


MyApp().run()