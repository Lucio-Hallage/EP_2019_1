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
                "biblioteca": "Ir para a biblioteca",
                'elevador':'acesso a todos os andares',
                'Predio Novo':'vá para o predio novo'
            }
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "elevador": "Acesso a todos os andares",
                "professor": "Falar com o professor",
                'restaurante':'Vá comer no restaurante'
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
                "inicio": "Voltar para o saguao de entrada",
                'livro':'pegar um livro'
            }
        },"andar 1": {
            "titulo": "Andar da Verdade",
            "descricao": "Voce chegou ao andar da sala de um professor",
            "opcoes": {
                "professor1": "Falar com o professor",
                'elevador':'acesso a todos os andares'}}
    ,"professor1": {
            "titulo": "Aula de GDE",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                'elevador':'acesso a todos os andares'}}
    ,"andar 2": {
            "titulo": "Andar da Ganancia",
            "descricao": "Voce chegou ao andar da sala de um professor",
            "opcoes": {
                'professor2':'Entra na sala de um professor',
                'elevador':'acesso a todos os andares',
                'imprimir':'vai ate a impressora'}}
    ,"professor2": {
            "titulo": "Aula de ModSim",
            "descricao": "Voce entrou na sala do seu professor",
            "opcoes": {'elevador':'acesso a todos os andares'}}
    ,"imprimir": {
            "titulo": "vc esta na impressora",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                    'elevador':'acesso a todos os andares'}}
    ,"andar 3": {
            "titulo": "Andar da Luxuria",
            "descricao": "Voce chegou ao andar da sala de um professor",
            "opcoes": {
                'professor3':'Entre na sala de um professor',
                'elevador':'acesso a todos os andares'}}
    ,"professor3": {
            "titulo": "Aula de InstruMed",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                    'elevador':'acesso a todos os andares'}}
    ,"elevador": {
            "titulo": "Elevador da queda",
            "descricao": "Voce entrou no elevador",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                'andar 1':'primeiro andar',
                'andar 2':'segundo andar',
                'andar 3':'terceiro andar',
                'andar 4':'quarto andar',
                "andar professor": "Tomar o elevador para o andar do professor",
                'subsolo':'va para o subsolo'}}
    ,"andar 4": {
            "titulo": "Andar de experimentos",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "jogar": "Jogar um mario kart com o Fuka",
                'elevador':'acesso a todos os andares',
                'professor4':'Entre na sala de um professor'}}
    ,"professor4": {
            "titulo": "Aula de NatDes",
            "descricao": "Voce chegou na sala do seu professor",
            "opcoes": {
                    'elevador':'acesso a todos os andares'}}
    ,"livro": {
            "titulo": "Escolha um livro",
            "descricao": "Voce chegou na estante em um instante oooooaaaaauuuuu!!!",
            "opcoes": {
                    "inicio": "Voltar para o saguao de entrada"}}
    ,"Predio Novo": {
            "titulo": "vc esta atravessando a rua e",
            "descricao": "MORREU!!!!!!!!!!!!!!!!!!!!!!",
            "opcoes": {}}
    ,"jogar": {
            "titulo": "vish,logo contra o Fukada,o melhor jogador de Mario kart do insper",
            "descricao": "Não teve jeito vc perdeu );",
            "opcoes": {'elevador':'acesso a todos os andares'}}
    ,"subsolo": {
            "titulo": "Subsolo da Escuridão",
            "descricao": "Tome cuidado com o escuro",
            "opcoes": {'elevador':'acesso a todos os andares',
                       'techlab':'Va para o techlab'}}
    ,"techlab": {
            "titulo": "Voce esta no Techlab...",
            "descricao": "Aqui é cheio de invencoes... Nossa mas o q sera aquilo??? Q estranho...",
            "opcoes": {'subsolo':'va para o subsolo'}}
    ,"auditorio": {
            "titulo": "Auditorio",
            "descricao": "INTEGRAÇÃO COM FDA",
            "opcoes": {'inicio':'acesso a todos os andares'}}
    ,"restaurante": {
            "titulo": "Restaurante da restauração",
            "descricao": "comer,comer,comer,comer e o melhor para poder crescer",
            "opcoes": {'elevador':'acesso a todos os andares'}}
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual

def combate():
    competidores={'avatar':{
            'hp':100,
            'atk':20,
            'def':10}
    ,'zumbi veterano':{
            'hp':40,
            'atk':12,
            "def":0}
    ,'Raul Alienigena':{
            'hp':200,
            'atk':40,
            'def':20}}
    vilao_atual='zumbi veterano'
    return competidores,vilao_atual

def main():
    arma_de_portais=0
    d=0
    p=0
    hp=100
    r=0
    g=0
    m=0
    i=0
    n=0
    c=0
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
    competidores,vilao_atual=combate()
    game_over = False
    while not game_over:
    
        if c%4==0 and c!=0:
            eu=competidores['avatar']
            inimigo={'hp':40,'atk':12,"def":0}
            print()
            print('Voce achou um zumbi veterano pela a escola')
            print()
            print('Seus status de combate')
            print(eu)
            print()
            print('Status de combate de seu oponente')
            print(inimigo)
            print()
            
            decida=input('correr ou lutar?')
            while eu['hp']>0 and inimigo['hp']>0 and decida=='lutar':
                print('Sua vez de atacar')
                print('Voce tirou {0} de hp do seu oponente'.format(eu['atk']-inimigo['def']))
                inimigo['hp']-=eu['atk']-inimigo['def']
                if inimigo['hp']>0:
                    print('Vez do seu inimigo')
                    print('Voce perdeu {0} de hp para seu oponente'.format(inimigo['atk']-eu['def']))
                    eu['hp']-=inimigo['atk']-eu['def']
                    decida=input('correr ou lutar?')
                else:
                    print('Parabens vc derrotou o Zumbi')
            c+=1
                    
        else:
            c+=1
        cenario_atual = cenarios[nome_cenario_atual]
        print(nome_cenario_atual)
        print('-'*len(nome_cenario_atual))
        for nomes,des in cenario_atual.items():
            if nomes != 'opcoes':
                print(des)
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
                hp-=10
            g=1
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
            m=1
        elif nome_cenario_atual== 'professor3': 
            print('OH NO')
            print()
            print('O professor de Instrumed esta pedindo o seu relatorio,vc pede o adiamento, mas ele te faz uma pergunta em troca?  ')
            print()
            print('A:Potenciometro')
            print('B:Protoboard')
            print('C:Multimetro')
            print('D:Tripot')
            resposta=input('Carlos Ribeiro:Qual è o aparelho de medicão usado nos laboratorios?')
            if resposta=='C':
                print('Carlos Ribeiro:Boa')
            else:
                print('Que pena,perdeu 1 ponto na media!')
                hp-=10
            i=1
        elif nome_cenario_atual== 'professor4':      
            print('PROTOTIPOS PRA QUARTA')
            print()
            print('Deu a louca em Victor e Gabriel')
            print()
            print('Essa não!É segunda e voce so tem 2 dias pra fazer 2 prototipos,vc pede o adiamento, mas ele te faz uma pergunta em troca?') 
            print()
            if d==1:
                print('Uau!!! vc tem o livro do dym,dessa vez vou te ajudar')
            print('A:É um prototipo pronto para a entrega')
            print('B:É um prototipo que ainda está em skecth ')
            print('C:É um prototipo feito para entender melhor o problema')
            print('D:É um prototipo quase em seu estado final')
            resposta=input('Victor Macul:O que é um prototipo sujo?')
            if resposta=='C':
                print('Carlos Ribeiro:Boa')
            else:
                print('Leia o DYM pelo amor de deus,perdeu 1 ponto na media!')
                hp-=10
            n=1
        elif nome_cenario_atual== 'livro':
            print()
            print('A:Livro Python')
            print('B:DYM')
            escolha=input('Qual livro vc quer?')
            if escolha=='A':
                print('Ótima escolha,agora vc podera imprimi-lo, e isso pode te ajudar a adiar o ep')
                p=1
            elif escolha=='B':
                print('Victor Macul ficará orgulhoso')
                d=1
        elif nome_cenario_atual== 'imprimir':
            if p==1:
                print('Uau!!!vc Tem um livro de python,o professor raul ira adorar')
                print()
                print('vc ganhou 0,5 pontos na media')
                hp+=5
            else:
                print()
                print('Estou impressionado')
        elif nome_cenario_atual== 'restaurante':
            if r==0:
                print('Voce deve estar com fome')
                print('Coma uma comida e ganhe 20 de hp')
                print('Delicious!!!')
                eu['hp']+=20
                print('hp atual{0}'.format(eu['hp']))
                r=1
            else:
                print('Voce acabou com toda a nossa comida!')
                print()
                print('Parece que vc comeu muuuito da ultima vez')
        
        elif nome_cenario_atual== 'techlab':
            print('Vc encontrou uma invencao bem esquisita no TechLab... Deseja verificar o que é? ')
            print('Nusssssss! Parece que vc encontrou um portal de teletransporte..')
            arma_de_portais=1
        elif nome_cenario_atual== 'auditorio':
            print('FDA')
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            for escolhas,acoes in opcoes.items():
                print(escolhas+': '+acoes)
            if arma_de_portais==1:
                print()
                print('arma de portais: Te teleporta para QUALQUER lugar do jogo')
                print('menos para salas bloqueadas(mesmo desbloqueadas)')
                
            escolha=input("qual opção vc quer?")
            while escolha=='professor' and i==0 and m==0 and n==0 and g==0 and nome_cenario_atual=='andar professor':
                print('Sala bloqueada!!! ')
                print('Para desbloquear vc tem que falar com todos os professores antes de ir para a sala do Raul')
                print()
                print('Volte para o elevador')
                escolha=input("qual opção vc quer?")
           
                    
            if escolha in opcoes:
                nome_cenario_atual= escolha
            elif escolha=='arma de portais' and arma_de_portais==1:
                print("inicio: Tomar o elevador para o saguao de entrada")
                print('andar 1:primeiro andar')
                print('andar 2:segundo andar')
                print('andar 3:terceiro andar')
                print('andar 4:quarto andar')
                print("andar professor: Tomar o elevador para o andar do professor")
                print('subsolo')
                print('restaurante')
                print()
                print()
                print()
                escolha=input("qual opção vc quer?")
                nome_cenario_atual= escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")
#adicionar o auditorio,restaurante,estacionamento

# Programa principal.
if __name__ == "__main__":
    main()