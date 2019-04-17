# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 18:47:51 2019

@author: insper
"""

p=0
hp=100
while hp>75:
    print('ola calouro.Estamos aqui no saguao insper')
    i=0
    while hp>75:
        opcao=input('Qual lugar vc quer ir:elevador,biblioteca,casa?')
        if opcao=='casa':
            i=1
            hp=0
        if opcao=='biblioteca':
            opcao=input('vc quer um livro ou falar com o veterano?')
            if opcao=='livro':
                print('Parabens!!! Voce conseguiu um novo item no seu inventario:Livro Python')
                p=1
            elif opcao=='veterano':
                print('ola eu sou o veterano no insper,tenho uma dica para voce,o professor raul quer que visite todos os outros professores antes dele')
            else: 
                print('voce voltou para o saguao')
        elif opcao == 'elevador':
            andar=input('escolha o andar de 1 a 5:') 
            if andar=='1':
                print('vc encontrou um veterano,pior um ninja')
                opcao=input('lutar ou correr?')
                if opcao=='lutar':
                    print('pergunta surpresa')
                    reposta=input('Quanto é 1+1?')
                    if reposta=='2':
                        print('Parabens!!!Vc passou no teste')
                    else:
                        print('vc perdeu 0,5 pontos na media')
                        hp-=5
                else:
                    print('vc perdeu 0,25 pontos na media')
                    hp-=2.5
                print('Parece que hoje não é seu dia de sorte!O professor de GDE apareceu!!!')
                print('A:NatDES')
                print('B:Modsim')
                print('C:InstruMed')
                print('D:DesSoft')
                resposta=input('Fernando Ribeiro:Qual materia resume o método científico?')
                if resposta=='B' or resposta=='Modsim':
                    print('Parabens,Voce passou em GDE')
                else:
                    print('Voce erroooooou e perdeu 1 ponto na media')
                    hp-=10
            
                print('vc retornou para o saguão')
            elif andar=='2':
                print('vc esta no  segundo andar')
                print('')
                opcao=input('ir imprimir alguma coisa ou entra na sala de aula?')
                if opcao=='sala':
                    print('A wild Pelicano has appeared!!!')
                    print()
                    print('A:Tx de variacao')
                    print('B:Numero  de euler')
                    print('C:Equacao a diferencas')
                    print('D:Tx de variacao instantanea')
                    resposta=input('Pelicano:O que é uma derivada?')
                    if resposta=='D':
                        print('Eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeexato')
                    else:
                        print('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeerrado,perdeu 1 ponto na media!')
                        hp-=10
                elif opcao=='imprimir':
                    if p==1:
                        print('Uau!!!vc Tem um livro,o professor raul ira adorar')
                        print()
                        print('vc ganhou 0,5 pontos na media')
                    else:
                        print()
                        print('Estou impressionado')
                print('vc retornou para o saguão')
            elif andar=='3':
                print('vc esta no andar 3')
                opcao=input('')
print()
print('vc perdeu!!!')
                        
                        
                    
            
                    
                    