#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 17:51:04 2019

@author: beatrizcf
"""

nota=10
import random 
def andar0_opcaobiblio():
    print ('Voce esta na biblioteca. Parece que a unica coisa que voce pode fazer aqui é pegar um livro, ou voce pode voltar para o saguao.')
    print ('A-voltar para o saguao')
    print ('B-pegar um livro')
    opcao=input('O que voce deseja fazer? Digite a letra desejada: ')
    if opcao in respostaB:
        inventario.append('livro')
        print('Boa, acho que este livro pode ser util! ')
        print('A-voltar para o saguao')
        opcao=input('O que voce deseja fazer agora? Digite a letra desejada: ')
    if opcao in respostaA:
        local='saguao'
    return local
        
def andar0_opcaocasa():
    print('Putz.... Acho que fugir das obrigacoes nao é a melhor opcao hein...Mas voce quem manda' )
    opcao=input('Voce deseja mesmo ir embora? ')
    if opcao in sim:
        print('Fim de jogo')
        print('Que pena... Voce nao conseguiu terminar o EP a tempo e sua nota foi 0')
        local='casa'
    elif opcao in nao:
        print('Boa escolha guerreiro! Bora continuar tentando...')
        local='saguao'
    return local
        
def opcaoelevador():
    local='elevador'
    print('Voce esta no elevador. Aqui voce tem acesso a todos os andares ou pode voltar para o saguao.')
    print('A-ir para o andar 0')
    print('B-ir para o 1 andar')
    print('C-ir para o 2 andar')
    print('D-ir para o 3 andar')
    print('E-ir para o 4 andar')
    print('F-ir para o 5 andar')
    print('G-ir para a sala dos professores')
    opcao=input('O que voce deseja fazer? Digite a letra desejada: ')
    #respostasvalidas=[respostaA,respostaB,respostaC,respostaD,respostaE,respostaF]
    #while opcao not in respostasvalidas:
        #opcao=input('Digite uma resposta valida: ')
    if opcao in respostaA:
        andar='Andar Térreo'
        local=andar0()
    elif opcao in respostaB:
        andar='Andar 1'
        local=andar1()
    elif opcao in respostaC:
        andar='Andar 2'
        local=andar2()
    elif opcao in respostaD:
        andar='Andar 3'
        #local=andar3()
    elif opcao in respostaE:
        andar='Andar 4'
        local=andar4()
    elif opcao in respostaF:
        andar='Andar 5'
        #local=andar5()
    elif opcao in respostaG:
        andar='sala dos professores'
        #local=andarprof()
    
    return local, andar 



#DEFS ANDARES

def andar0():
    print('Voce esta no saguao do Insper. A partir daqui voce pode ir para:')
    print('A-biblioteca')
    print('B-Elevador')
    print('C-Desistir de tudo e ir para casa')
    opcao=input('O que voce deseja fazer? Digite a letra desejada: ')
    #respostasvalidas=[respostaA,respostaB]
    #while opcao not in respostasvalidas:
            #opcao=input('Digite uma resposta valida: ')
    if opcao in respostaA:
        local=andar0_opcaobiblio()
        #local=biblio
    elif opcao in respostaB:
        local,andar=opcaoelevador()
    elif opcao in respostaC:
        local=andar0_opcaocasa()#local=saguao
          
    return local
        
def andar1():
    profsurpresa=random.choice(professores)
    print('Parece que hoje não é seu dia de sorte!O professor {0} apareceu!!!'.format(profsurpresa))
    print('Para escapar dele voce devera responder a pergunta que ele fizer corretamente')
    pergunta=random.choice(perguntas)
    print(asperguntas())
    
def andar2():
    print('Voce esta no 2 andar. A partir daqui voce pode:')
    print('A-ir para o elevador')
    print('B-dar um pulo na reprografia')
    opcao=input('O que vc deseja fazer? Digite a letra desejada: ')
    if opcao in respostaA:
        local,andar=opcaoelevador()
    elif opcao in respostaB:
        local='Reprografia'
        opcao=input('Aqui vc pode imprimir alguma leitura obrigatoria. Deseja imprimir? ')
        if opcao in sim:
            print('Boaaaaa, agora vc tem uma leitura obrigatoria no seu inventario')
            inventario.append('Leitura obrigatoria')
        if opcao in nao:
            print('Okay, a decisao é sua... ')
        print('vc esta de volta ao elevador')
        local='elevador'
    return local

#def andar3():
    #encontrar veterano para dica
    #encontrar prof 
    
def andar4():
    nota=media
    print('Voce esta no 4 andar. A partir daqui vc pode:')
    print('A-Voltar para o elevador')
    print('B-Jogar videogame')
    opcao=input('O que vc deseja fazer? Digite a letra desejada: ')
    if opcao in respostaA:
        local,andar=opcaoelevador()
    elif opcao in respostaB:
        local='sala de jogos'
        print('Voce esta na sala de jogos')
        print('...2 hours later...')
        print('putzzz... essa sala de jogos é um perigo. vc perdeu a nocao da hora e as suas chances de conseguir o adiamento diminuiram')
        nota=nota-1
        print('Sua media agr é de {} pontos'.format(nota))
    return local,nota

    
    
#DEF PERGUNTAS

def asperguntas():
    if pergunta==perguntas[0]:
        ponto=0.25
        resposta=int(input('Quanto é um mais um? Digite um numero: '))
        if resposta==2:
            resposta=True
        else:
            resposta=False
    if pergunta==perguntas[1]:
        ponto=1
        resposta=int(input('Quanto é 2+2? Digite um numero: '))
        if resposta==4:
            resposta=True
        else:
            resposta=False
            
    if resposta==True:
        print('parabens!!! vc acertou e ganhou {} de media'.format(ponto))
        media+=ponto
    if resposta==False:
        print('Voce erroooooou e perdeu {} ponto na media'.format(ponto))
        media-=ponto
    return media
        
        
#VARIAVEIS      
media=10        
inventario=[]
respostaA=['A','a']
respostaB=['B','b']
respostaC=['C','c']
respostaD=['D','d']
respostaE=['E','e']
respostaF=['F','f']
respostaG=['G','g']
andaresvisitados=[0]

professores=['Fernando Ribeiro','Carlinhos','Pelicano','Vitor','nenhum']
perguntas=[0,1]
pedidos=[0,1]

sim=['Sim','sim','s','S','SIM']
nao=['Nao','nao','n','N','NAO','Não','não','NÃO']


#INTRO

print('Tudo parecia tranquilo, sem provas nem nada pra entregar, a única coisa pra fazer era aproveitar o tempo livre… Ate que vc recebe um aviso, na segunda de manha, no balckboard: ENTREGA EP HOJE.  ') 
print('É dia de entregar EP, e você ainda nem começou o projeto….  Você esta na entrada do Insper, e sua missão é tentar adiar a entrega do EP. Boa sorte ;D .')

nome=input('Qual é o seu nome? ')
print('Olá {0}, o negócio é o seguinte: Voce tem ate as 18 horas para conseguir adiar a entrega do EP. Além disso, voce inicia o dia com 10 de média, e ao longo do jogo vc devera manter essa media maior do que 7.5, para ter alguma chance de conseguir o adiamento do EP com o Raul'.format(nome))
local='saguao'
andar='Andar Térreo'

    
while local=='saguao':
    local=andar0()
while local=='elevador':
    local,elevador=opcaoelevador()