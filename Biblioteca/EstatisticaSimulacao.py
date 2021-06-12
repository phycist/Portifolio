#bibliotecas
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import sys, os
#----------------------------------------------------------------------------------------
#       Esse módulo possui a funcionalidade  que adcionamos 
#       Simula os dados futuros 
#       classe terminada em 31/05
#----------------------------------------------------------------------------------------

class EstatisticaSimulacao(object):
    def __init__(self,**kwargs):
        pass
    ####################Estatistica###################
        #realiza as medidas do desvios  
    def Medida_Desvio_padrao_show(self,dados):
        media = sum(dados)/(len(dados))
        desvio_medio_2=[]
        for i in range(0,len(dados)):
            desvio_medio_2.append(np.power(media - dados[i],2))
        
        desvio_medio_2s=sum(desvio_medio_2)        
        desvio_p=np.math.sqrt(desvio_medio_2s/(len(dados) - 1))
        variancia=desvio_medio_2s/(len(dados)-1)
        erro=variancia/desvio_p
        print(" Nossa mediada : %.2f +/- %.2f" %(desvio_p,variancia))
        print("O erro obtido %.2f" %(erro))
    
    
        #levanta as prabailidades entre os usuarios
    def Medida_Desvio_padrao(self,dados):
        media = sum(dados)/(len(dados))
        desvio_medio_2=[]
        desvio_p=[]
        for i in range(0,len(dados)):
            desvio_medio_2.append(np.power(media - dados[i],2))
        desvio_medio_2s=sum(desvio_medio_2)        
        desvio_p=np.math.sqrt(desvio_medio_2s/(len(dados) - 1))
        variancia=desvio_medio_2s/(len(dados)-1)
        erro=variancia/desvio_p
        resultado = {'media':media,'desvio_padrao':desvio_p,'variancia':variancia,'erro':erro}
        return resultado
    
    
    
   
    def Propabilades_Usuarios(self,usuarios,novos_usuarios):
        n_usuarios=usuarios
        n_usuarios_total=sum(usuarios)
        n_novos_usuarios=novos_usuarios
        n_novos_usarios_total=sum(novos_usuarios)
        #porcentagem dos usuários
        porcent_usuarios = sum(n_usuarios)/(n_usuarios_total + n_novos_usarios_total)
        porcent__novos_usuarios = sum(n_novos_usuarios)/(n_usuarios_total + n_novos_usarios_total)
                 # probabilidades
        prop = [porcent_usuarios,porcent__novos_usuarios]
        usu=['usuários','novos_usuários']
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,2])
        ax.bar(usu[0],prop[0],color='r',width=0.25)
        ax.bar(usu[1],prop[1],color='b',width=0.25)
        ax.set_title('Distribuição dos usuários')
        ax.legend(labels=usu)
        plt.text(x=usu[0],y=prop[0],s=str(prop[0]*100)+'%',size=11,ha='center')
        plt.text(x=usu[1],y=prop[1],s=str(prop[1]*100)+'%',size=11,ha='center')
        plt.show()
        # retorna os dados para a simulacao
        return prop
        
    #########################Simulação######################################## 
    def sim(self,p_usuario,n_sim=10,espacamento=0.025,lim_p=10):
        #inicializa dos dado da simulacao
        sim=[]
        #realiza a sumulacao
        if p_usuario > 1 :
           print("O primeiro termo tem que estar entre a e 1")
           exit(0)
        else:
            pass
        
        if type(n_sim) == type(1):
            prob_usuario = []
            prob_novo_usuario = []
            p = list(np.random.binomial(n_sim,p_usuario,n_sim)/100)
            
            for i in range(0,n_sim):
                q = 1 - p[i]
                prob_novo_usuario.append(q)
            prob_usuario=list(p)
            # resultados
            p_media=self.Medida_Desvio_padrao(prob_usuario)['media']
            p_desvio=self.Medida_Desvio_padrao(prob_usuario)['desvio_padrao']
            p_erro=self.Medida_Desvio_padrao(prob_usuario)['erro']

            q_media=self.Medida_Desvio_padrao(prob_novo_usuario)['media']
            q_desvio=self.Medida_Desvio_padrao(prob_novo_usuario)['desvio_padrao']
            q_erro=self.Medida_Desvio_padrao(prob_novo_usuario)['erro']


        #######################################################################
        #gera oa grafico simulacao
                #usuarios
            # configuacoes 
        # O eixo X --> probabilidades
        x=''
        x=list(np.unique(prob_usuario))
        # O eixo Y --> frequecias 
                 # frequencia dos  y
        freqs = {i:prob_usuario.count(i) for i in prob_usuario}
        #print("A frequencia")
        #print(freqs)
        # valores de y
        y=''
        y=list(freqs.values())
        
        # plotagem dos graficos
        bar=plt.subplot()
        bar.set(title="Distribuição usuários",
                xlabel="probabilidades possiveis",
                ylabel="Frequências de ocorrência")
        bar.bar(x,y,width=espacamento)
        
        
        
        # salvar grafico
        
        plt.show(True)
        ########fim usuarios################
        #novos_usuarios
            # configuacoes 
        # O eixo X --> probabilidades
        x=''
        x=list(np.unique(prob_novo_usuario))
        # O eixo Y --> frequecias 
                 # frequencia dos  y
        freqs = {i:prob_novo_usuario.count(i) for i in prob_novo_usuario}
        y=''
        y=list(freqs.values())
        
        # plotagem dos graficos
        bar=plt.subplot()
        bar.set(title="Distribuição novos_usuários",
                xlabel="probabilidades possiveis",
                ylabel="Frequências de ocorrência")
        bar.bar(x,y,width=espacamento)
        # salvar grafico
        
        plt.show(True)
        ##################fim de novos usuarios##########
        #################valores previstos
        print("Os valores previstos para usuários  :")
        print("valor medio %.2f +/- %.2f erro percentual: %.2f " %(p_media,p_desvio,p_erro))
        
        print("Os valores previstos para novos usuários  :")
        print("valor medio %.2f +/- %.2f erro percentual: %.2f  " %(q_media,q_desvio,q_erro))
        return {'usuarios':{'media':p_media,'desvio':p_desvio,'erro_per':p_erro},
                 'novos_usuarios':{'media':q_media,'desvio':q_desvio,'erro_per':q_erro}}

         
        
























        


