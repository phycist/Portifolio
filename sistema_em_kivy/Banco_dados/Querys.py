class Querys(object):
      def __init__(self):
          self.query =''
         #//////////////////////////////////////////////////////
          '`1`, `ana`, `paulo`' # tem que passar por string
      def montador_valores(self,lista,bet="`",sep=","):
          string = ""#5
          for i in range(len(lista)):
              if i != len(lista) - 1:
                 string += bet + str(lista[i]) + bet + sep + " "
              else:
                 string += bet + str(lista[i]) + bet
          # qualquer coisa muda-se retorno
          return string
        #/////////////////////////////////////////////////////////
      
      
##############################################################################################################
      def Obter_nome_colunas(self,tabela):
          self.query = "SELECT column_name FROM information_schema.columns WHERE table_name =\""+str(tabela)+ "\";"
          return self.query
       
      def select_todos_dados(self, tabela):
          self.query="SELECT * FROM `"+str(tabela) +"`;" 
          return self.query

      def inserir_dados(self, tabela, valores1, valores2):
          # Primeira declaração
          self.query ="INSERT INTO `"+str(tabela) +"`"
          #colocando as colunas
          self.query +="(" + self.montador_valores(valores1,bet="`") +")" 
          #Colocando os valores
          self.query += " VALUES ("+ self.montador_valores(valores2,bet="\"") +");"
          return self.query
                   
      def update_dado(self, tabela, id_tabela, coluna, valor):
          #  declaração
          self.query =" UPDATE `"+str(tabela) +"` SET `"+ str(coluna) +"` = \""+ str(valor)+"\"" +" WHERE `id_corretor`="+str(id_tabela)+";"
          return self.query
         
      def deletando_um_dado(self, tabela, id_tabela):
          self.query = "DELETE FROM `"+ str(tabela) +"` WHERE "+str(id_tabela[0])+"="+str(id_tabela[1])+";"
          return self.query
         
      def deletando_todos_dados(self, tabela):
          #Primeira declaração
          self.query =" Delete from `"+ str(tabela) +"`;" 
          return self.query
###############################################################################################################################


######################testes##################
           # Todos estão ok
'''           
#criando a instância
consulta = Querys()

input("Testando o mantar valores \n")
print(consulta.montador_valores(["Carlos","Eduardo"]))

input("Testando o obter nome das colunas")
print(consulta.Obter_nome_colunas("corretor"))

input("Testando o select todos os dados ")
print(consulta.select_todos_dados("corretor"))

input("Testando o insert dados")
'''
#INSERT INTO `corretor` (`id_corretor`, `nome_corretor`, `Endereço_imovel`, `situação_imovel`, `morador`, `situação_morador`) VALUES (2, "nilce", "Morumbi", "Vago", "Ted", "Zoio");

'''
print(consulta.inserir_dados("corretor", ["id_corretor","nome_corretor", "Endereço_imovel","situação_imovel","morador","situação_morador"],[2,"nilce","Morumbi","Vago","Ted","Zoio"]))



input("testando o update dado")
print(consulta.update_dado("corretor","1" , "nome_corretor", "leon"))

input("Deletando um dado")
print(consulta.deletando_um_dado("corretor",["id_corretor",1]))

input("Deletando todos os dados")
print(consulta.deletando_todos_dados("corretor"))
'''
