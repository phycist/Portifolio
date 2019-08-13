# -*- coding: utf-8 -*-
###########################
#######Bibliotecas#########
import MySQLdb as mdb
from Querys import Querys
##########################
'''
Nesse módulo vamos criar uma classe: que realiza
a conecxão com o banco de dados e realiza as cosultas 
'''
class Mysql(Querys):
      def __init__(self, host, login, password, database):
        #host = endereço do database  127.0.0.1
        # login, senha para conectar no database root
          # variaveis do banco
          self.host = host
          self.login = login
          self.password = password
          self.database = database

          #Conexão do database
          self.connected = False
          self.conexao = None
          self.cursor = None
      
###########Conexões##################################
      def conectando_database(self):
          try:
              self.conexao = mdb.connect(self.host, self.login, self.password, self.database)
          except:
              print("Erro ao conectar")
          else:
              self.connected = True
              print("Estamos conectados ")
              self.cursor = self.conexao.cursor()
       
      def disconectando_database(self):
          self.conexao.close()
          self.connected = False
#####################################################
      
      
#############Preparação querys ##########
      def query_com_resultado(self):
          try:
             self.cursor.execute(self.query)
          except:
              raise Exception("Falhao ao retornar resultados")
          return self.cursor.fetchall()
      
      def query_sem_resultado(self):
          try:
              self.cursor.execute(self.query)
          except: 
              raise Exception("Falha ao executar a query")
          else:
               
              return self.cursor.fetchall()
                  
################as consultas ##########################################
      def obter_colunas(self,tabela):
          if self.connected != True:
             self.conectando_database()
          Querys.Obter_nome_colunas(self,tabela)
          resultado = self.query_com_resultado()
          self.disconectando_database()
          return resultado
       
      def selecionar_todos_os_dados(self,tabela):
          if self.connected != True:
             self.conectando_database()
          Querys.select_todos_dados(self,tabela)
          #print(self.query)
          resultado = self.query_com_resultado()
          # print(type(resultado)) ---> tupla
          #print(resultado)
          self.disconectando_database()
          return resultado
      
      def inserir_dados(self, tabela, valores1, valores2):
          if self.connected != True:
             self.conectando_database()
          Querys.inserir_dados(self, tabela, valor1,valor2)
          self.query_sem_resultado()
          self.disconectando_database()

      def deletar_um_dado(self,tabela,id_tabela):
          if self.connected != True:
             self.conectando_database()
          Querys.deletando_um_dado(self,tabeela,id_tabela)
          self.query_sem_resultado()
          self.disconectando_database()

'''
                O script passou
###############Testes 1#####################################
print("criando um conector a base de dados")
# (host, login, password, database)
# host 127.0.0.1
# login imobiliaria
# password imob
# database imobiliaria
input("Configurando a ligação do banco de dados")
mysql_conex = Mysql("127.0.0.1","imobiliaria","imob","imobiliaria") 
input("Conectando a base de dados")
mysql_conex.conectando_database()
input("vamos realizar as query a base de dados")
####################################################
#mysql_conex.selecionar_todos_os_dados("corretor")
mysql_conex.obter_colunas("corretor")

######################################################
input("Desconectando a base de dados")
if mysql_conex.connected == True:
   mysql_conex.disconectando_database()
else:
    pass
############################################################
'''   





