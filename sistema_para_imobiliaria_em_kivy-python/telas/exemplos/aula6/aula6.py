# -*- coding: utf-8 -*-
######    Bibliotecas #####
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
##################################

class MeuApp(App):
    def build(self):
        return FloatLayout()

if __name__=="__main__":
  MeuApp().run()

