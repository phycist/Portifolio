########Bibliotecas###########
from locatariolib import *
#############################
class locatarioApp(App):
    def build(self):
        return locatarioJanela()

cj = locatarioApp()
cj.run()

