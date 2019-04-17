# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 14:10:14 2019

@author: insper
"""
import time

def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca",
                'andar 1':'primeiro andar',
                'andar 2':'segundo andar',
                'andar 3':'terceiro andar'
            }
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor"
            }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada"
            }
        },"andar 1": {
            "titulo": "Andar da Verdade",
            "descricao": "Voce chegou ao andar da sala de um professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor1": "Falar com o professor"}}
    ,"professor1": {
            "titulo": "Aula de GDE",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada"}}
    ,"andar 2": {
            "titulo": "Andar da Ganancia",
            "descricao": "Voce chegou ao andar da sala de um professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                'professor2':'Entra na sala de um professor'}}
    ,"professor2": {
            "titulo": "Aula de ModSim",
            "descricao": "Voce entrou na sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada"}}
    ,"imprimir": {
            "titulo": "vc esta na impressora",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada"}}
    ,"andar 3": {
            "titulo": "Andar da Luxuria",
            "descricao": "Voce chegou ao andar da sala de um professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                'professor3':'Entre na sala de um professor'}}
    ,"professor3": {
            "titulo": "Aula de InstruMed",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada"}}}
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


def main():
    hp=10
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]

        print(nome_cenario_atual)
        print('-'*len(nome_cenario_atual))
        for nomes,c in cenario_atual.items():
            if nomes != 'opcoes':
                print(c)
                print()

        opcoes = cenario_atual['opcoes']
        if nome_cenario_atual== 'professor1':
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
                hp-=1
        elif nome_cenario_atual== 'professor2': 
            print('A wild Pelicano has appeared!!!')
            time.sleep(2)
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
        elif nome_cenario_atual== 'professor3': 
            print('OH NO')
            print()
            print('O professor de Instrumed esta pedindo o seu relatorio,vc pede o adiamento, mas ele te faz uma pergunta em troca?  ')
            print()
            print('A:Potenciometro')
            print('B:Protoboard')
            print('C:Multimetro')
            print('D:Tripot')
            resposta=input('Qual è o aparelho de medicão usado nos laboratorios?')
            if resposta=='C':
                print('Carlos Ribeiro:Boa')
            else:
                print('Que pena,perdeu 1 ponto na media!')
                hp-=10
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            for escolhas,acoes in opcoes.items():
                print(escolhas+': '+acoes)
                
            escolha=input("qual opção vc quer?")
            
            if escolha in opcoes:
                nome_cenario_atual= escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
