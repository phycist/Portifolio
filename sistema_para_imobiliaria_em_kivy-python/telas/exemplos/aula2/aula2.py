# -*- coding: utf-8 -*-

######    Bibliotecas #####
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
##################################


class MinhaGrid(GridLayout):
      def __init__(self, **kwargs):
          super(MinhaGrid,self).__init__(**kwargs)
          self.cols = 11 
          self.add_widget(Label(text="Name:"))
          self.name = TextInput(multiline=False)
          self.add_widget(self.name)






class MeuApp(App):
    def build(self):
        return MinhaGrid()

if __name__=="__main__":
  MeuApp().run()

