###############resolver os paths ##################
import sys, os
sep=os.sep
path=os.path.dirname(os.path.abspath(__file__))
sys.path.append(path)
sys.path.append(path+sep+"Biblioteca")
sys.path.append(path+sep+"Biblioteca"+sep+'Projeçoes')
sys.path.append(path+sep+"Biblioteca"+sep+"Analizador")
sys.path.append(path+sep+"Biblioteca"+sep+"EstatisticaSimulacao")
sys.path.append(path+sep+"Biblioteca"+sep+"Dados")
#################################################

