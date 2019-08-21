#Bibliotecas###########
from entradabotao import *
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
#########################################

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%5
class entradaJanela(BoxLayout):
        #   Inicializar o app
      def __init__(self, **kwargs):
          super(entradaJanela,self).__init__(**kwargs)
          self.valor='' 
    ###############################################
      
#----------fucionalidades------------------------------------
      def spinner_clicked(self, value):
      
          if value == 'locador':
             print("chamando locador")
             self.valor = value
          elif value == 'locatario':
                 print("Chamando locatario")
                 self.valor = value
          elif value == 'corretor':
               print("Chamando corretor")
               self.valor = value
           
      
      
#----------------verificação do login --------------------
          # Buscando valores
      def pegar_valores(self):
          # pegar valor da escolha
          escolha = self.ids.spinner_id_head.text
          # pegar o valor login
          login = self.ids.text_input_login.text
          # pegar o valor password
          password = self.ids.text_input_password.text
          if login !="" and password !="": 
             return [escolha,login,password]
          else:
             return ['','']

      def validacao(self):
          dados = self.pegar_valores()
          if dados == ['','']:
             print("Não inseriu os dados")
          else:
             #realizar a validaçoes no BD
             ###########################
             #dados = ['corretor','']
             self.chamar_telas(dados)
          
       
            
      def chamar_telas(self,dados_tela):
          print("Chamar telas")
          # vamos chamar as telas
          if dados_tela[0] == "corretor":
             print("Chamando o corretor")
             import corretor

          elif dados_tela[0] == "locatario":
               print("chamando o locatario")
               import locatario


          elif dados_tela[0] == "locador":
               print("chamando o locador")
               import locador


          else:
              print("Erro")


            
             








       

          




              









     
          

