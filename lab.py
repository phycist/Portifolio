###############################
from start import * # conector entre as pastas 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
from  Biblioteca.Analizador import Analizador

class  Lab(Analizador):
       def __init__(self,**kwargs):
            Analizador.__init__(self,**kwargs)
       
       def help(self):
           print(" \
           Help do analisador \n\
#####################################################################################################\n\
                Antes de qualquer analise\n\
                ################################\n\
                 #criação de lab simples\n\
-----------------------------------------------------------\n\
Como padão usramos o arquivo basededados.xlsx\n\
--> Simples criação de uma análise\n\
lab=Lab()\n\
                            funções que temos: \n\
                            *******************\n\
        *projeções\n\
*************************\n\
lab.read_xls\n\
lab.data_frame_ajust\n\
lab.gerar_projecao_usarios_sessoes\n\
lab.gerar_projecao_novos_usarios_sessoes\n\
\n\
        *estatística\n\
****************************\n\
lab.Medida_Desvio_padrao\n\
lab.Propabilidades_Usuarios\n\
\n\
*       *Simulações\n\
***************************\n\
lab.sim\n\
######################################################################################################\n\
     Você pode obter este help a qualquer momento este help dado o comando\n\
     lab.help()\n\
######################################################################################################\n")
        









##################################################################

lab=Lab(dado='.',path='.')
lab.help()


