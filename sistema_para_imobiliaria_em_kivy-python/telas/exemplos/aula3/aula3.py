# -*- coding: utf-8 -*-

######    Bibliotecas #####
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
##################################
class MinhaGrid(GridLayout):
      def __init__(self, **kwargs):
          super(MinhaGrid,self).__init__(**kwargs)
          self.cols=1
          self.dentro = GridLayout()
          self.dentro.cols = 2
      
          self.dentro.add_widget(Label(text="Primeiro nome"))
          self.nome = TextInput(multiline=False)
          self.dentro.add_widget(self.nome)
      
          self.dentro.add_widget(Label(text="Sobrenome"))
          self.sobrenome = TextInput(multiline=False)
          self.dentro.add_widget(self.sobrenome)
      
          self.add_widget(self.dentro)
       
          self.mandar = Button(text="Mandar", font_size=40)
          self.mandar.bind(on_press=self.mandar_texto)
          self.add_widget(self.mandar)
          
      def mandar_texto(self, instancia):
          nome = self.nome.text
          sobrenome = self.sobrenome.text
          
          print(" Seu nome é %s  e seu sobrenome é %s" %(nome,sobrenome))




class MeuApp(App):
    def build(self):
        return MinhaGrid()

if __name__=="__main__":
  MeuApp().run()

