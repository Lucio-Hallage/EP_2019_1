#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 11:50:08 2019

@author: beatrizcf
"""

def subsolo():
    andar='subsolo'
    A='A-Voltar para o elevador'
    B='B-Ir para o TechLab'
    print('SUBSOLO')
    print('-'*len(andar))
    print()
    print('Vc esta no subsolo... Aqui voce pode:')
    print(A)
    print(B)
    opcao=input('O que vc deseja fazer? ')
    if opcao==respostaA:
        local=opcaoelevador()
        #volta para o elevador
    elif opcao==respostaB:
        local='techlab'
        print('TECHLAB')
        print('-'*len(local))
        print()
        print('Voce esta no Techlab... Aqui é cheio de invencoes... Nossa mas o q sera aquilo??? Q estranho...')
        opcao=input('Vc encontrou uma invencao bem esquisita no TechLab... Deseja verificar o que é? ')
        if opcao in sim:
            print('Nusssssss! Parece que vc encontrou um portal de teletransporte..')
            A='A-voltar para o elevador'
            B='B-testar o teletransporte'
            if opcao in respostaA:
                #voltar para o elevador
            if opcao in respostaB:
                print('Ahhhhhhhhhhhhhhhh naooooooooooo... Vc foi teletransportado para algum lugar...')
                #fazer random lugar 
                print('vish, vc foi parar no {0}, no andar {1}...Agora vc tem uma arma de teletransporte no seu inventario '.format(lugar,andar))
                inventario.append('Arma de teletransporte')
                #voltar funcao do andar que ele for parar
        if opcao in nao:
            print('Boa, as vezes é melhor nao arriscar...')
            print()
            local='elevador'
            print('ELEVADOR')
            print('-'*len(local))
            print('vc esta de volta no elevador')
            #voltar funcao elevador
    