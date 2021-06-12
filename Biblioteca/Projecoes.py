#Bibliotecas
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import sys, os
#----------------------------------------------------------------------------------------
#       Esse módulo possui a funcionalidade Principal de nossa aplicação
#       Gerações de gráficos das projeções
#       Classe terminada 30/05
#----------------------------------------------------------------------------------------
class Projecoes(object):
    def __init__(self,**kwargs):
        #pegar parametros
        if hasattr(self, 'path'):
            self.path=kwargs['path']
            
        else:
            self.path='.'
        
        if hasattr(self, 'origem'):
            self.origem=kwargs['origem']
            
        else:
            self.origem=''
            
        if hasattr(self,'dado'):
            self.path=kwargs['dado']
        else:
            self.dado='basededados.xlsx'
            
        #------verificação ----
        if self.path=='.':
            if self.origem=='': 
                self.origem=os.getcwd()
                self.path=self.origem+os.sep+'BaseDados'
               
                        
        else:
            pass
        #---------------------------
    
    def read_xls(self):
        df=pd.read_excel(self.path,index_col=1,header=None)
        self.dfa=df.drop(0,axis='columns').dropna()
        
    def data_frame_ajust(self):
        
        if self.dfa=='':
            self.read_xls()
        else:
            pass   
        #extração de dados
        #usuários old
        usuario_old=[]
        for i in range(1,len(self.dfa[2])):
            usuario_old.append(self.dfa[2][i])
        #numeros pontos
        self.N=len(usuario_old)
        #usuários novos
        usuario_novos=[]
        for i in range(1,len(self.dfa[3])):
            usuario_novos.append(self.dfa[3][i])
        #visualizasao
        visua=[]
        for i in range(1,len(self.dfa[4])):
            visua.append(self.dfa[4][i])
        sessoes=[]
        for i in range(1,len(self.dfa[5])):
            sessoes.append(self.dfa[5][i])
        #novo dataframe
        dado={'usuarios':usuario_old,'novos_usuarios':usuario_novos,'visualizacao':visua,'sessoes':sessoes}
        self.df_n=pd.DataFrame(data=dado)
    
    def gerar_projecao_usuario_visualizacao(self):

        px=np.array(self.df_n['usuarios'])
        py=np.array(self.df_n['visualizacao'])
        x__0=[]
        x__1=[]
        for i in range(0,len(px)):
            x__0.append((px[i]**0))
            x__1.append((px[i]**1))
        x00=np.dot(x__0,x__0)
        x01=np.dot(x__0,x__1)
        x10=np.dot(x__1,x__0)
        x11=np.dot(x__1,x__1)
        X=np.array([[x00,x01],[x10,x11]])
        y0=np.dot(py,x__0)
        y1=np.dot(py,x__1)
        Y=np.array([y0,y1])
        #solucao
        s = np.linalg.solve(X,Y)
        an=s[0]
        bn=s[1]
        a=str(s[0])
        b=str(s[1])
        x=np.linspace(1.0,32,num=29,endpoint=False)
        # no modelo temos que ter  linespace inferior a amostra
        y=bn*x+an
        titulo=str('usuários vs visualizacao\n'+r"$"+b+"x"+a+"$\n")
        plt.plot(px[1:32],py[1:32],'bo')
        plt.xlabel('usuários')
        plt.ylabel('visualizacao')
        plt.title(titulo)
        plt.plot(x,y)
        if self.path == './BaseDados/basededados.xlsx':
                os.chdir('..')
        plt.savefig('./graficos/usuarios_vs_visualizacao')
        #Cáculo de correlação
        # variação explicada / estatitica
        variacao_est_p=[]
        # variacao em relacao aos dados
        variacao_dados_p=[]
        #y médio
        y_medio=sum(py)/self.N
        print('Valor médio de y')
        print(y_medio) 
        for i in range(len(py)):
         variacao_dados_p.append((y_medio-py[i])**2)
        #variacao_dados_p
        # coreelacao ao quadrado
        r_2=sum(variacao_est_p)/sum(variacao_dados_p)
        # correlação
        r = round(np.sqrt(r_2)*100,2)
        print("O a correlação entre os dados é {0} % ".format(r))

    def gera_projecao_novos_usuarios_visualizacao(self):
        #test
        px=np.array(self.df_n['novos_usuarios'])
        py=np.array(self.df_n['visualizacao'])
        x__0=[]
        x__1=[]
        x__2=[]
        x__3=[]
        y__0=[]
        y__1=[]
        for i in range(0,len(px)):
            x__0.append((px[i]**0))
            x__1.append((px[i]**1))
            x__2.append((px[i]**2))
            x__3.append((px[i]**3))
        
        #linha 0
        x00=np.dot(x__0,x__0)
        x01=np.dot(x__0,x__1)
        x02=np.dot(x__0,x__2)
        x03=np.dot(x__0,x__3)
        #linha 1
        x10=np.dot(x__1,x__0)
        x11=np.dot(x__1,x__1)
        x12=np.dot(x__1,x__2)
        x13=np.dot(x__0,x__3)
        #linha 2
        x20=np.dot(x__2,x__0)
        x21=np.dot(x__2,x__1)
        x22=np.dot(x__2,x__2)
        x23=np.dot(x__2,x__3)
        #linha 3
        x30=np.dot(x__3,x__0)
        x31=np.dot(x__3,x__1)
        x32=np.dot(x__3,x__2)
        x33=np.dot(x__3,x__3)

        X=np.array([[x00,x01,x02,x03],[x10,x11,x12,x13],[x20,x21,x22,x23],[x30,x31,x32,x33]])
        y0=np.dot(py,x__0)
        y1=np.dot(py,x__1)
        y2=np.dot(py,x__2)
        y3=np.dot(py,x__3)
        Y=np.array([y0,y1,y2,y3])
        del x__0,x__1,y__0,y__1
        #solucao
        s = np.linalg.solve(X,Y)
        an=s[0]
        bn=s[1]
        cn=s[2]
        dn=s[3]
        a=str(s[0])
        b=str(s[1])
        c=str(s[2])
        d=str(s[3])
        x=np.linspace(1.0,32,num=32,endpoint=False)
        #x_2=np.linespace(1.0,)
        ## no modelo temos que ter  linespace inferior a amostra
        y=dn*x**3+cn*x**2+bn*x+an
        titulo=str('novos_usuários vs visualizacao\n')
        plt.plot(px[1:32],py[1:32],'bo')
        plt.xlabel('novos_usuários')
        plt.ylabel('acessos')
        plt.title(titulo)
        plt.plot(x,y) 

    def  gerar_projecao_usuarios_sessoes(self):
         px=np.array(df_n['usuarios'])
         py=np.array(df_n['sessoes'])
         x__0=[]
         x__1=[]
        
         for i in range(0,len(px)):
             x__0.append((px[i]**0))
             x__1.append((px[i]**1))
         x00=np.dot(x__0,x__0)
         x01=np.dot(x__0,x__1)
         x10=np.dot(x__1,x__0)
         x11=np.dot(x__1,x__1)
         X=np.array([[x00,x01],[x10,x11]])
         y0=np.dot(py,x__0)
         y1=np.dot(py,x__1)
         Y=np.array([y0,y1])
        
         #solucao
         s = np.linalg.solve(X,Y)
         an=s[0]
         bn=s[1]
         a=str(s[0])
         b=str(s[1])
         x=np.linspace(1.0,32,num=29,endpoint=False)
         # no modelo temos que ter  linespace inferior a amostra
         y=bn*x+an
         titulo=str('usuários vs sessões\n'+r"$"+b+"x"+a+"$\n")

         plt.plot(px[1:32],py[1:32],'bo')
         plt.xlabel('usuários')
         plt.ylabel('sessões')
         plt.title(titulo)
         plt.plot(x,y)
         plt.savefig('./graficos/usuarios_vs_sessoes')
         # Cáculo de correlação
         # variação explicada
         # variação em relação ao modelo
         variacao_est_p=[]
         #variaçao em relação aos dados
         variacao_dados_p=[]
         y_medio=sum(py)/N
         print("Valor médio")
         print(y_medio)
         for i in range(len(py)):
             variacao_dados_p.append((y_medio-py[i])**2)
         #variacao_dados_p
         #variaçao em relacao ao modelo
         for i in range(len(y)):
             variacao_est_p.append((y_medio-y[i])**2)

         #variacao_dados_p
         # coreelacao ao quadrado
         r_2=sum(variacao_est_p)/sum(variacao_dados_p)
         #r_2
         # correlacao
         r = round(np.sqrt(r_2)*100,2)
         print("O a correlação entre os dados é {0} % ".format(r))

    def  gerar_projecao_novos_usuarios_sessoes(self):
         px=np.array(self.df_n['novos_usuarios'])
         py=np.array(self.df_n['sessoes'])
         x__0=[]
         x__1=[]
         y__0=[]
         for i in range(0,len(px)):
             x__0.append((px[i]**0))
             x__1.append((px[i]**1))
         x00=np.dot(x__0,x__0)
         x01=np.dot(x__0,x__1)
         x10=np.dot(x__1,x__0)
         x11=np.dot(x__1,x__1)
         X=np.array([[x00,x01],[x10,x11]])
         y0=np.dot(py,x__0)
         y1=np.dot(py,x__1)
         Y=np.array([y0,y1])
         del x__0,x__1,y__0,
         #solucao
         s = np.linalg.solve(X,Y)
         an=s[0]
         bn=s[1]
         a=str(s[0])
         b=str(s[1])
         x=np.linspace(1.0,32,num=29,endpoint=False)
         # no modelo temos que ter  linespace inferior a amostra
         y=bn*x+an
         titulo=str('novos_usuários vs sessoes\n'+r"$"+b+"x+"+a+"$\n")
         plt.plot(px[1:32],py[1:32],'bo')
         plt.xlabel('novos_usuários')
         plt.ylabel('sessoes')
         plt.title(titulo)
         plt.plot(x,y)
         plt.savefig('./graficos/novos_usuarios_vs_sessoes')
         # Cáculo de correlação
         # variação explicada
         # variação em relação ao modelo
         variacao_est_p=[]
         #variaçao em relação aos dados
         variacao_dados_p=[]
         y_medio=sum(py)/N
         print("Valor médio")
         print(y_medio)
         for i in range(len(py)):
            variacao_dados_p.append((y_medio-py[i])**2)
         #variacao_dados_p
         #variaçao em relacao ao modelo
         for i in range(len(y)):
            variacao_est_p.append((y_medio-y[i])**2)
         
         #variacao_dados_p
         # coreelacao ao quadrado
         r_2=sum(variacao_est_p)/sum(variacao_dados_p)
         #r_2
         # correlacao
         r = round(np.sqrt(r_2)*100,2)
         print("O a correlação entre os dados é {0} % ".format(r))



    



    



     


        
           

    



     

        








