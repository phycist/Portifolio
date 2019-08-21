#Bibliotecas###########
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner 
from kivy.uix.floatlayout import FloatLayout 
from kivy.core.window import Window
#########################################
##################

class locatarioJanela(BoxLayout):
       #   Inicializar o app
    def __init__(self, **kwargs):
        super(locatarioJanela,self).__init__(**kwargs)
        self.valor='' 
    ###############################################

    def spinner_clicked(self, value):
        print(value)
        if value == 'locador':
           print("chamando locatario")
           self.valor = value
        else:
           if value == 'locatario':
              print("Chamando corretor")
              self.valor = value
        
        print("voce escolheu")
        print(self.valor)

     
     


