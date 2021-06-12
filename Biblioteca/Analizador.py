#######Biblioteca########
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import sys, os
from  Projecoes import Projecoes
from EstatisticaSimulacao import EstatisticaSimulacao
from Dados import Dados
#---------------------
#----------------------------------------------------------------------------------------
#       Esse módulo etrutural 
#       Simula os dados futuros 
#       #  Classe terminada 29/05

#----------------------------------------------------------------------------------------
#########################
class  Analizador(Dados,EstatisticaSimulacao):
    def __init__(self,**kwargs):
        Dados.__init__(self,**kwargs)


