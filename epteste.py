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
                'predionovo':'vá para o predio novo',
                'auditorio':'vá para o predio novo'
            }
        },
        "andarprofessor": {
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
            "descricao": "Voce entrou na sala de Raul Ikeda",
            "opcoes": {'VITORIA':'Ganhou o JOGO'}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada",
                'livro':'pegar um livro'
            }
        },"andar1": {
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
    ,"andar2": {
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
            "titulo": "Impressora",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                    'elevador':'acesso a todos os andares'}}
    ,"andar3": {
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
                'andar1':'primeiro andar',
                'andar2':'segundo andar',
                'andar3':'terceiro andar',
                'andar4':'quarto andar',
                "andarprofessor": "Tomar o elevador para o andar do professor",
                'subsolo':'va para o subsolo'}}
    ,"andar4": {
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
    ,"predionovo": {
            "titulo": "vc esta atravessando a rua e",
            "descricao": "MORREU!!!!!!!!!!!!!!!!!!!!!!",
            "opcoes": {}}
    ,"jogar": {
            "titulo": "FUKA Rei do mario kart",
            "descricao": "Não teve jeito vc perdeu );",
            "opcoes": {'elevador':'acesso a todos os andares'}}
    ,"subsolo": {
            "titulo": "Subsolo da Escuridão",
            "descricao": "Tome cuidado com o escuro",
            "opcoes": {'elevador':'acesso a todos os andares',
                       'techlab':'Va para o techlab'}}
    ,"techlab": {
            "titulo": "Techlab da Gula",
            "descricao": "Voce esta no Techlab...Aqui é cheio de invencoes... Nossa mas o q sera aquilo??? Q estranho...",
            "opcoes": {'subsolo':'va para o subsolo'}}
    ,"auditorio": {
            "titulo": "Auditorio",
            "descricao": "Voce esta no auditorio",
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
    ,'Monstro do techlab':{
            'hp':120,
            'atk':15,
            "def":0}
    ,'Raul Alienigena':{
            'hp':200,
            'atk':40,
            'def':20}}
    vilao_atual='Monstro do techlab'
    return competidores,vilao_atual

def main():
    nota=100
    r=0
    c=0
    Inventario=[]
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
    eu=competidores['avatar']
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
            while decida!='lutar' and decida!='correr':
                print('Opção Inválida')
                decida=input('correr ou lutar?')
            while eu['hp']>0 and inimigo['hp']>0 and decida=='lutar':
                print('Sua vez de atacar')
                print('Voce tirou {0} de hp do seu oponente'.format(eu['atk']-inimigo['def']))
                inimigo['hp']-=eu['atk']-inimigo['def']
                if inimigo['hp']>0:
                    print('Vez do seu inimigo')
                    print('Voce perdeu {0} de hp para seu oponente'.format(inimigo['atk']-eu['def']))
                    eu['hp']-=inimigo['atk']-eu['def']
                    print('Seus status de combate')
                    print(eu)
                    print('Status de combate de seu oponente')
                    print(inimigo)
                    decida=input('Quer continuar:correr ou lutar?')
                    while decida!='lutar' and decida!='correr':
                        print('Opção Inválida')
                        decida=input('Quer continuar:correr ou lutar?')
            if eu['hp']<=0:
                game_over=True
            else:
                print('Parabens vc derrotou o zumbi')
                c+=1
        else:       
            c+=1
        cenario_atual = cenarios[nome_cenario_atual]
        print(cenario_atual['titulo'])
        print('-'*len(cenario_atual['titulo']))
        print(cenario_atual['descricao'])
        print()

        
        if nome_cenario_atual== 'professor1':
            print('Parece que hoje não é seu dia de sorte!O professor de GDE apareceu!!!')
            print('A:NatDES')
            print('B:Modsim')
            print('C:InstruMed')
            print('D:DesSoft')
            resposta=input('Fernando Ribeiro:Qual materia resume o método científico?')
            while resposta!='A' and resposta!='B' and resposta!='C' and resposta!='D':
                print('Opção Inválida')
                resposta=input('Fernando Ribeiro:Qual materia resume o método científico?')
            if resposta=='B' or resposta=='Modsim':
                print('Parabens,Voce passou em GDE')
            else:
                print('Voce erroooooou e perdeu 1 ponto na media')
                nota-=10
            Inventario.append('GDE')
        elif nome_cenario_atual== 'professor2': 
            print('A wild Pelicano has appeared!!!')
            time.sleep(2)
            print()
            print('A:Tx de variacao')
            print('B:Numero  de euler')
            print('C:Equacao a diferencas')
            print('D:Tx de variacao instantanea')
            resposta=input('Pelicano:O que é uma derivada?')
            while resposta!='A' and resposta!='B' and resposta!='C' and resposta!='D':
                print('Opção Inválida')
                resposta=input('Pelicano:O que é uma derivada?')
            if resposta=='D':
                print('Eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeexato')
            else:
                print('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeerrado,perdeu 1 ponto na media!')
                nota-=10
            Inventario.append('ModSim')
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
            while resposta!='A' and resposta!='B' and resposta!='C' and resposta!='D':
                print('Opção Inválida')
                resposta=input('Carlos Ribeiro:Qual è o aparelho de medicão usado nos laboratorios?')
            if resposta=='C':
                print('Carlos Ribeiro:Boa')
            else:
                print('Que pena,perdeu 1 ponto na media!')
                nota-=10
            Inventario.append('instrumed')
        elif nome_cenario_atual== 'professor4':      
            print('PROTOTIPOS PRA QUARTA')
            print()
            print('Deu a louca em Victor e Gabriel')
            print()
            print('Essa não!É segunda e voce so tem 2 dias pra fazer 2 prototipos,vc pede o adiamento, mas ele te faz uma pergunta em troca?') 
            print()
            if 'DYM' in Inventario:
                print('Uau!!! vc tem o livro do dym,dessa vez vou te ajudar')
            else:
                print('A:É um prototipo pronto para a entrega')
                print('B:É um prototipo que ainda está em skecth ')
                print('C:É um prototipo feito para entender melhor o problema')
                print('D:É um prototipo quase em seu estado final')
                resposta=input('Victor Macul:O que é um prototipo sujo?')
                while resposta!='A' and resposta!='B' and resposta!='C' and resposta!='D':
                    print('Opção Inválida')
                    resposta=input('Victor Macul:O que é um prototipo sujo?')
                if resposta=='C':
                    print('Victor Macul:Boa')
                else:
                    print('Leia o DYM pelo amor de deus,perdeu 1 ponto na media!')
                    nota-=10
            Inventario.append('Natdes')
        elif nome_cenario_atual== 'livro':
            print()
            print('A:Livro Python')
            print('B:DYM')
            resposta=input('Qual livro vc quer?')
            while resposta!='A' and resposta!='B':
                    print('Opção Inválida')
                    resposta=input('Qual livro vc quer?')
            if resposta=='A':
                print('Ótima escolha,agora vc podera imprimi-lo, e isso pode te ajudar a adiar o ep')
                Inventario.append('Livro Python')
            elif resposta=='B':
                print('Victor Macul ficará orgulhoso')
                Inventario.append('DYM')
        elif nome_cenario_atual== 'imprimir':
            if 'Livro Python' in Inventario:
                print('Uau!!!vc Tem um livro de python,o professor raul ira adorar')
                print()
                print('vc ganhou 0,5 pontos na media')
                nota+=5
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
            if 'Arma de portais' not in Inventario:
                eu=competidores['avatar']
                inimigo=competidores[vilao_atual]
                print('OOOOOOOOOH')
                print()
                print('Voce achou um Monstro pela no Techlab')
                print()
                print('Seus status de combate')
                print(eu)
                print()
                print('Status de combate de seu oponente')
                print(inimigo)
                print() 
                decida=input('correr ou lutar?')
                while decida!='lutar' and decida!='correr':
                    print('Opção Inválida')
                    decida=input('correr ou lutar?')
                while eu['hp']>0 and inimigo['hp']>0 and decida=='lutar':
                    print('Sua vez de atacar')
                    print('Voce tirou {0} de hp do seu oponente'.format(eu['atk']-inimigo['def']))
                    inimigo['hp']-=eu['atk']-inimigo['def']
                    if inimigo['hp']>0:
                        print('Vez do seu inimigo')
                        print('Voce perdeu {0} de hp para seu oponente'.format(inimigo['atk']-eu['def']))
                        eu['hp']-=inimigo['atk']-eu['def']
                        print('Seus status de combate')
                        print(eu)
                        print('Status de combate de seu oponente')
                        print(inimigo)
                        decida=input('correr ou lutar?')
                        while decida!='lutar' and decida!='correr':
                            print('Opção Inválida')
                            decida=input('correr ou lutar?')
                if inimigo['hp']<=0:
                    print('Vc encontrou uma invencao bem esquisita no TechLab... Deseja verificar o que é? ')
                    print('Nusssssss! Parece que vc encontrou um portal de teletransporte..')
                    print('Parece que valeu a pena vc ter Derrotado esse monstro')
                    Inventario.append('Arma de portais')
                else:
                    game_over=True
                
        elif nome_cenario_atual== 'auditorio':
            if 'Excalibur' not in Inventario:
                print('Excalibur')
                print('Voce achou a Espada Lendaria para derrotar monstros disfarçados de pessoas')
                print('Ganhou 80 de atk')
                eu['atk']+=80
                Inventario.append('Excalibur')
        elif nome_cenario_atual== 'professor':
            if nota<75:
                print('Raul ikeda:Voce nao tem nota suficiente e nem merecimento,volte pra casa')
                game_over=True
            else:
                print('Raul ikeda:Tudo bem,vou adiar o EP para o outro més')
                print('Tem algo de errado')
                print('Quando vc vai sair um monstro te ataca e vc percebe que o esse monstro era o Raul disfarçado')
                if 'Excalibur' not in Inventario:
                    print('Monstro do Python:Comigo sua chance vai a 0%')
                else:
                    print('Monstro do Python:O que é isso na sua mão')
                    print('É a lendaria Excalibur,então vc ja derrotou o meu irmão,outro motivo para eu te matar')
                vilao_atual='Raul Alienigena'
                eu=competidores['avatar']
                inimigo=competidores[vilao_atual]
                print('Batalhe e Derrote o Monstro do Python')
                print()
                print('Seus status de combate')
                print(eu)
                print()
                print('Status de combate de seu oponente')
                print(inimigo)
                print()
                
                decida=input('correr ou lutar?')
                while decida!='lutar' and decida!='correr':
                    print('Opção Inválida')
                    decida=input('correr ou lutar?')
                while eu['hp']>0 and inimigo['hp']>0 :
                    if decida=='correr':
                        print('O monstro quebrou a porta, se prepare pra lutar')
                    print('Sua vez de atacar')
                    print('Voce tirou {0} de hp do seu oponente'.format(eu['atk']-inimigo['def']))
                    inimigo['hp']-=eu['atk']-inimigo['def']
                    if inimigo['hp']>0:
                        print('Vez do seu inimigo')
                        print('Voce perdeu {0} de hp para seu oponente'.format(inimigo['atk']-eu['def']))
                        eu['hp']-=inimigo['atk']-eu['def']
                        print('Seus status de combate')
                        print(eu)
                        print('Status de combate de seu oponente')
                        print(inimigo)
                if eu['hp']<=0:
                    print('Vc nunca ira ganhar de mim')
                    print('Morra verme')
                else:
                    print('Mas como vc me derrotou')
        
        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        elif'VITORIA' in opcoes:
            game_over = True
            
        else:
            for escolhas,acoes in opcoes.items():
                print(escolhas+': '+acoes)
            if 'Arma de portais' in Inventario:
                print()
                print('Arma de portais: Te teleporta para QUALQUER lugar do jogo')
                print('menos para salas bloqueadas')
                
            escolha=input("qual opção vc quer?")
            escolha=escolha.lower()
            escolha=''.join(escolha.split())
            while escolha not in opcoes and escolha!='armadeportais':
                print('Opção Inválida')
                escolha=input("qual opção vc quer?")
                escolha=escolha.lower()
                escolha=''.join(escolha.split())
            if escolha in opcoes:
                if 'instrumed' and 'Modsim' and 'Natdes' and 'GDE'  not in Inventario:
                    while escolha=='professor':
                        print('Sala bloqueada!!! ')
                        print('Para desbloquear vc tem que falar com todos os professores antes de ir para a sala do Raul')
                        print()
                        print('Volte para o elevador')
                        escolha=input("qual opção vc quer?")
                        escolha=escolha.lower()
                        escolha=''.join(escolha.split())
                nome_cenario_atual= escolha
            elif escolha=='armadeportais' and 'Arma de portais' in Inventario:
                for k in cenarios.keys():
                    print(k)
                escolha=input("qual opção vc quer?")
                escolha=escolha.lower()
                escolha=''.join(escolha.split())
                if 'instrumed' and 'Modsim' and 'Natdes' and 'GDE'  not in Inventario:
                    while escolha=='professor':
                        print('Sala bloqueada!!! ')
                        print('Para desbloquear vc tem que falar com todos os professores antes de ir para a sala do Raul')
                        print()                  
                        escolha=input("qual opção vc quer?")
                        escolha=escolha.lower()
                        escolha=''.join(escolha.split())
                        while escolha not in cenarios:
                            print('Opção Inválida')
                            escolha=input("qual opção vc quer?")
                            escolha=escolha.lower()
                            escolha=''.join(escolha.split())
                else:
                    while escolha not in cenarios:
                        print('Opção Inválida')
                        escolha=input("qual opção vc quer?")
                        escolha=escolha.lower()
                        escolha=''.join(escolha.split())
            nome_cenario_atual= escolha
    if nota>=75 and eu['hp']>0:
        print('You WIN')
        print('Mas nao perca tempo comemorando')
        print('vc ainda tem que fazer o seu EP ate amanha, Boa Sorte')
    else:
        print("Você Perdeu!")


# Programa principal.
if __name__ == "__main__":
    main()