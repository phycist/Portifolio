#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-

#################Bibliotecas#######################
from  selenium import webdriver
####################Configuraçoes##################
driver = webdriver.Chrome('./drives/driveslinux/chromedriver') 

################Variaveis###########################
Link = "https://web.whatsapp.com/"
# Entrar no site 
browser = driver
browser.get(Link) 
    
'----------------------------------ok------------------------'

######## Antes de abrir o novegador################
######### o campo de escoler contato---------------
nome = raw_input("Escolha o contato")
menssagem = raw_input("Escreva a messagem ")


#########Esperar o scan##################
raw_input("Precione Qualquer tecla para continua")
##########################3Escolhendo o contato###########################
contato = driver.find_element_by_xpath('//span[@title = "{}"]'.format(nome))
contato.click()


'------------------------------------------------------------'
##############Ir para messagem###########################
msg_box = driver.find_element_by_class_name("_3u328")


for i in range(1,10,1):
    print(i)

    ################### Menssagem ao formulário #####################
    msg_box.send_keys(menssagem)

    #################### Mandar a messagem ##################################
    msg_button = driver.find_element_by_class_name("_3M-N-")
    msg_button.click()






raw_input("Precione qualquer tecla para sair")    
browser.close()
