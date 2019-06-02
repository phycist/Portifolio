#! /usr/bin/env python2.7
# -*- coding: utf-8 -*.-                                                                                                                  
######Biliotecas###################                                                                                                      
import Tkinter                                                                                                                           
from Tkinter import *                                                                                                                    
                                                                                                                      
##################################                                                                                                       
#     métodos 
#################################
def Sair():
    exit()
#################################

# criação
janela = Tk()
#################################
# barra de menu-horizontal
menubar = Menu(janela)

#  opçoes menu-horizontal-arquivo
arquivoMenuitens = Menu(menubar)

# arquivo-opçoes-conteudo
arquivoMenuitens.add_command(label="Sair", command=Sair)

#adicionar no menu-horizontal 
menubar.add_cascade(label="arquivo", menu=arquivoMenuitens)

#finalizando
janela.config(menu=menubar)
janela.mainloop()
#######################################################
