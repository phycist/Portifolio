#Bibliotecas###########
from locadorlib import *
#########################################
##################

class locadorApp(App):
    def build(self):
        return locadorJanela()

cj = locadorApp()
cj.run()

