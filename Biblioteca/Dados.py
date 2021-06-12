#bibliotecas
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import sys, os
from  Projecoes import Projecoes

#----------------------------------------------------------------------------------------
#       Esse módulo possui a funcionalidade  que adcionamos 
#       Simula os dados futuros 
#       #  Classe terminada 31/05

#----------------------------------------------------------------------------------------
class Dados(Projecoes):
    def __init__(self,**kwargs):
        pass
    
    def Gerar_Dados_projeção_Linear(self,x_nome,y_nome,**kwargs):
        func = kwargs['y_nome']
        N = kwargs['N']
        x = kwargs['x_nome']
        y = kwargs['a']*(np.array(x)) + kwargs['b']
        data_frame = pd.DataFrame(list(zip(lst, lst2)),
               columns =[x_nome, y_nome])
        return data_frame
    
    def Gerar_planilha(self,data_frame,tipo):
        with pd.ExcelWriter('dados_projecoes.xlsx') as writer:
             data_frame.to_excel(writer, sheet_name=tipo)
                                