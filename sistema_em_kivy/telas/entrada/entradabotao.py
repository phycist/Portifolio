##########Biblioteca#################
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.properties import ListProperty
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse, Rectangle
####################################


class Botao(ButtonBehavior,Label):
      cor_normal = ListProperty([0.1,0.5,0.7,1])
      cor_press =  ListProperty([0.7,0.1,0.7,1])
      def __init__(self,**kwargs):
          super(Botao,self).__init__(**kwargs)
          self.atualizar()
      def on_pos(self,*args):
          self.atualizar()
      
      def on_size(self,*args):
          self.atualizar()

      def on_press(self, *args):
          self.cor_normal, self.cor_press = self.cor_press, self.cor_normal

      def on_release(self, *args):
          self.cor_normal, self.cor_press = self.cor_press, self.cor_normal 

      def on_cor_normal(self,*args):
          self.atualizar()

      def atualizar(self,*args): 
          self.canvas.before.clear()
          with self.canvas.before:
               Color(rgba=self.cor_normal)
               Ellipse(size=(10*self.height,self.height),
                           pos=(self.center_x-180,self.center_y - 20))
