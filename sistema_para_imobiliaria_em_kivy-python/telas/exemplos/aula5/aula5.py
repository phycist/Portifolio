# -*- coding: utf-8 -*-

######    Bibliotecas #####
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

##################################
class MinhaGrid(Widget):
      nome = ObjectProperty(None)
      email = ObjectProperty(None)


class MeuApp(App):
    def build(self):
        return MinhaGrid()

if __name__=="__main__":
  MeuApp().run()

