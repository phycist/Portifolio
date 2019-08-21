#Bibliotecas###########
from corretorlib import *
#########################################
##################

##################################################################################################
class corretorApp(App):
      def build(self):
          return CorretorJanela()

cj = corretorApp()
cj.run()

