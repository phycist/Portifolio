#Bibliotecas###########
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner 
from kivy.uix.floatlayout import FloatLayout 
from kivy.core.window import Window
#########################################
##################

class CorretorJanela(BoxLayout):
       #   Inicializar o app
    def __init__(self, **kwargs):
        super(CorretorJanela,self).__init__(**kwargs)
        self.valor='' 
    ###############################################

    def spinner_clicked(self, value):
        print(value)
        if value == 'locador':
           print("chamando locador")
           self.valor = value
        else:
           if value == 'locatario':
              print("Chamando locatario")
              self.valor = value
        
        print("voce escolheu")
        print(self.valor)

     
     



class corretorApp(App):
    def build(self):
        return CorretorJanela()

if __name__=="__main__":
    cj = corretorApp()
    cj.run()

