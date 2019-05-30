#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
'//----------------------------------------------'
'''
Nesse script iremos realizar uma simples tarefa, adicionar um repositório 
e atualinar para o linux deepin e afins 

'''
#-----------Bibliotecas----------------------------------
import sh, os, platform, subprocess
#------------------------------------------------------
#variaveis
sim = "Y"
nao = "N"
#-------------------------------------------------------------------------------------
if platform.system() == 'Linux' :
   print('Seu sistema é linux: ')
   print('O nome de sua distribuição é: '+ platform.linux_distribution()[0])
   print('O seu repositório de São Paulo é:')
   comando1="cat /etc/apt/sources.list | grep -A 1 'SP'|grep deb"
   repositorio = subprocess.check_output(comando1, shell=True)
   
   print subprocess.check_output(comando1, shell=True)
   melhorar_repositorio1 = raw_input('gostaria de adicionar o repositório? (y/n)').upper()
   print(melhorar_repositorio1)
   #-------------------------------------------------------------------------------------
   
   if melhorar_repositorio1 == sim:
      opcao_automatica = raw_input("Ao adicionar,Você gostaria que está tafera seje automatica?(y/n)").upper()
      print(opcao_automatica)
      if opcao_automatica == sim:
                #  substitua 
                # comando2="sudo echo 'repositorio' >> repostorio.txt"
                # por 
                # comando2="sudo echo 'repositório' >> /etc/apt/sources.list "
         comando2="sudo echo 'repositorio' >> repostorio.txt"
         manual=subprocess.check_output(comando2, shell=True)
         print manual
         print 'repostorio adicionado '
      else:
         print "você escolheu adicionar o repositório manualmente cuidado "
         edndereco=raw_input("Digite o endereço do repositório\n")
                  #  substitua 
                # comando3='sudo echo "'+str(edndereco) +'" >> repositorio.txt'
                # por 
                # comando="sudo echo 'repositório' >> /etc/apt/sources.list "              
         comando3= 'sudo echo "'+str(edndereco) +'" >> repositorio.txt'
         manual=subprocess.check_output(comando3, shell=True)     
         print manual
         print "repositório adicinado"
   #------------------------------------------------------------------------------------ 
else:
   print 'O seu sistema não é Linux '
