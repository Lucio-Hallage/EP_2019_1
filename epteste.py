# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 14:10:14 2019

@author: insper
"""
import time

def t(t):
    return time.sleep(t)

A=['A','a']
B=['B','b']

def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguão do perigo",
            "descricao": "Você esta no saguão de entrada do Insper",
            "opcoes": {
                "biblioteca": "Ir para a biblioteca",
                'elevador':'Acesso a todos os andares',
                'predionovo':'Vá para o prédio novo',
                'auditorio':'Veja se tem alguma palestra interessante'
            }
        },
        "andarprofessor": {
            "titulo": "Andar do desespero",
            "descricao": "Você chegou ao andar da sala do seu professor de dessoft",
            "opcoes": {
                "elevador": "Acesso a todos os andares",
                "professor": "Falar com o professor",
                'restaurante':'Vá comer no restaurante'
            }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce entrou na sala de Raul Ikeda",
            "opcoes": {'fim':'FIM DE JOGO'}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Você está na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguão de entrada",
                'livro':'Pegar um livro'
            }
        },"andar1": {
            "titulo": "Andar da Verdade",
            "descricao": "Você chegou no primeiro andar ",
            "opcoes": {
                "professor1": "Falar com o professor",
                'elevador':'Acesso a todos os andares'}}
    ,"professor1": {
            "titulo": "Aula de GDE",
            "descricao": "Você chegou na sala do seu professor",
            "opcoes": {
                'elevador':'Acesso a todos os andares'}}
    ,"andar2": {
            "titulo": "Andar da Ganância",
            "descricao": "Você chegou no segundo andar",
            "opcoes": {
                'professor2':'Entra na sala de aula',
                'elevador':'Acesso a todos os andares',
                'imprimir':'Vai até a reprografia'}}
    ,"professor2": {
            "titulo": "Aula de ModSim",
            "descricao": "Você entrou na aula de Modsim",
            "opcoes": {'elevador':'Acesso a todos os andares'}}
    ,"imprimir": {
            "titulo": "Reprografia",
            "descricao": "Você chegou na reprografia",
            "opcoes": {
                    'elevador':'Acesso a todos os andares'}}
    ,"andar3": {
            "titulo": "Andar da Luxúria",
            "descricao": "Você chegou no terceiro andar",
            "opcoes": {
                'professor3':'Entre na sala de aula',
                'elevador':'Acesso a todos os andares'}}
    ,"professor3": {
            "titulo": "Aula de InstruMed",
            "descricao": "Você chegou na aula de Instrumed",
            "opcoes": {
                    'elevador':'Acesso a todos os andares'}}
    ,"elevador": {
            "titulo": "Elevador da queda",
            "descricao": "Você entrou no elevador",
            "opcoes": {
                "inicio": "Pegar o elevador para o saguão de entrada",
                'andar1':'Primeiro andar',
                'andar2':'Segundo andar',
                'andar3':'Terceiro andar',
                'andar4':'Quarto andar',
                "andarprofessor": "Andar dos professores e do lanche",
                'subsolo':'Vá para o subsolo'}}
    ,"andar4": {
            "titulo": "Andar de experimentos",
            "descricao": "Você chegou no quarto andar",
            "opcoes": {
                "jogar": "Jogar um mario kart com o Fuka",
                'elevador':'Acesso a todos os andares',
                'professor4':'Entre na sala de aula'}}
    ,"professor4": {
            "titulo": "Aula de NatDes",
            "descricao": "Você chegou na sala de aula",
            "opcoes": {
                    'elevador':'Acesso a todos os andares'}}
    ,"livro": {
            "titulo": "Escolha um livro",
            "descricao": "Você chegou na estante em um instante oooooaaaaauuuuu!!!",
            "opcoes": {
                    "inicio": "Voltar para o saguão de entrada"}}
    ,"predionovo": {
            "titulo": "Você estava atravessando a rua e...",
            "descricao": "MORREU!!!!!!!!!!!!!!!!!!!!!!",
            "opcoes": {}}
    ,"jogar": {
            "titulo": "FUKA Rei do mario kart",
            "descricao": "Você até tentou, mas não teve jeito... Você perdeu );",
            "opcoes": {'elevador':'Acesso a todos os andares'}}
    ,"subsolo": {
            "titulo": "Subsolo da Escuridão",
            "descricao": "Tome cuidado com o escuro",
            "opcoes": {'elevador':'Acesso a todos os andares',
                       'techlab':'Vá para o techlab'}}
    ,"techlab": {
            "titulo": "Techlab da Gula",
            "descricao": "Você está no Techlab...Aqui é cheio de invenções... Nossa mas o que será aquilo??? Que estranho...",
            "opcoes": {'subsolo':'Vá para o subsolo'}}
    ,"auditorio": {
            "titulo": "Auditório",
            "descricao": "Você está no auditório",
            "opcoes": {'inicio':'Volta para o saguão'}}
    ,"restaurante": {
            "titulo": "Restaurante da restauração",
            "descricao": "Comer,comer...comer,comer ...é o melhor para poder crescer",
            "opcoes": {'elevador':'Acesso a todos os andares'}}
    ,"veterano": {
            "titulo": "Veterano",
            "descricao": "Voce achou um veterano",
            "opcoes": {'elevador':'Acesso a todos os andares'}}
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
            "def":5}
    ,'Raul Alienigena':{
            'hp':200,
            'atk':40,
            'def':20}
    ,'Zumbi0':{
            'hp':34,
            'atk':20,
            'def':3}
    ,'Zumbi1':{
            'hp':45,
            'atk':10,
            'def':4}
    ,'Zumbi2':{
            'hp':55,
            'atk':5,
            'def':10}
    ,'Zumbi3':{
            'hp':65,
            'atk':15,
            'def':5}
    ,'Zumbi4':{
            'hp':40,
            'atk':20,
            'def':5}
    ,'Zumbi5':{
            'hp':50,
            'atk':15,
            'def':10}
            }
    vilao_atual=competidores['Zumbi0']
    
        
    return competidores,vilao_atual

def main():
    nota=10
    r=0
    c=0
    d=0
    Inventario=[]
    print("Na hora do sufoco!")
    print("------------------")
    t(1)
    print()
    print('Tudo parecia tranquilo, sem provas nem nada pra entregar, a única coisa pra fazer era aproveitar o tempo livre… '
        'Até que você recebe um aviso, na segunda de manhã, no blackboard: ENTREGA DO EP HOJE...')
    t(3)
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor Raul para pedir um "
        "adiamento do EP (boa sorte...)")
    print()
    t(4)

    cenarios, nome_cenario_atual = carregar_cenarios()
    competidores,vilao_atual=combate()
    eu=competidores['avatar']
    game_over = False
    while not game_over:
    
        if c%6==0 and c!=0:
            competidores,vilao_atual=combate()
            if c==6:
                vilao_atual=competidores['Zumbi1']
            elif c==12:
                vilao_atual=competidores['Zumbi2']
            elif c==18:
                vilao_atual=competidores['Zumbi3']
            elif c==24:
                vilao_atual=competidores['Zumbi4']
            elif c>30:
                vilao_atual=competidores['Zumbi5']
            inimigo=vilao_atual
            print()
            print('Voce achou um zumbi veterano pela a escola')
            t(1)
            print()
            print('Seus status de combate')
            print(eu)
            t(1)
            print()
            print('Status de combate de seu oponente')
            print(inimigo)
            t(1)
            print()
            
            decida=input('Correr ou lutar?')
            while decida!='lutar' and decida!='correr':
                print('Opção Inválida')
                decida=input('Correr ou lutar?')
                print()
            while eu['hp']>0 and inimigo['hp']>0 and decida=='lutar':
                print('>>>Sua vez de atacar')
                t(1)
                print('Você tirou {0} de hp do seu oponente'.format(eu['atk']-inimigo['def']))
                inimigo['hp']-=eu['atk']-inimigo['def']
                if inimigo['hp']>0:
                    t(1)
                    print('>>>Vez do seu inimigo')
                    t(1)
                    print('Você perdeu {0} de hp para seu oponente'.format(inimigo['atk']-eu['def']))
                    eu['hp']-=inimigo['atk']-eu['def']
                    print()
                    t(1)
                    print('>>>Seu status de combate')
                    print(eu)
                    t(1)
                    print()
                    print('>>>Status de combate de seu oponente')
                    print(inimigo)
                    t(1)
                    print()
                    decida=input('Quer continuar? Digite correr para parar ou lutar para continuar')
                    while decida!='lutar' and decida!='correr':
                        print('Opção Inválida')
                        decida=input('Quer continuar? Digite correr para parar ou lutar para continuar')
            if eu['hp']<=0:
                game_over=True
            else:
                if decida=='lutar': 
                    t(2)
                    print('Parabéns!!! Você derrotou o zumbi veterano e ganhou mais 3 pontos de ataque')
                    eu['atk']+=3
                    t(1)
                    print(eu)
                    c+=1
                if decida=='correr':
                    t(2)
                    print()
                    print('Vish... Parece que temos um arregão por aqui...Você perdeu 2 pontos de defesa')
                    eu['def']-=2
                    t(1)
                    print('Seu status de combate:{0}'.format(eu))
                    c+=1
                t(3)

        cenario_atual = cenarios[nome_cenario_atual]
        print()
        t(2)
        print(cenario_atual['titulo'])
        print('-'*len(cenario_atual['titulo']))
        t(1)
        print(cenario_atual['descricao'])
        print()
        t(2)

        
        if nome_cenario_atual== 'professor1':
            print('Parece que hoje não é o seu dia de sorte!O professor de GDE apareceu!!!')
            t(2)
            print('A:NatDES')
            t(0.2)
            print('B:Modsim')
            t(0.2)
            print('C:InstruMed')
            t(0.2)
            print('D:DesSoft')
            t(0.2)
            resposta=input('Fernando Ribeiro: Qual matéria resume o método científico?')
            while resposta!='A' and resposta!='B' and resposta!='C' and resposta!='D':
                print('Opção Inválida')
                resposta=input('Fernando Ribeiro: Qual matéria resume o método científico?')
            if resposta=='B' or resposta=='Modsim':
                print('Parabéns,você passou em GDE e ganhou 0.25 de média')
                nota+=0.25
                print('Sua média agora é de {}'.format(nota))
            else:
                nota-=1.5
                print('Voce erroooooou e perdeu 1.5 ponto na média. Sua média agora é {}'.format(nota))
            if 'Leitura GDE' in Inventario:
                print('Fernando: O que é isso na sua mão?')
                t(1)
                print('Eu: Nada não, só a leitura obrigatória da aula')
                t(1)
                print('Fernando: Estou muito orgulhoso de você...Toma aqui mais alguns décimos para te ajudar...')
                nota+=0.7
                t(1)
                print('Boa, você ganhou mais 0.7 de nota.... Sua nota agora é de {}'.format(nota))
                t(1)
            Inventario.append('GDE')
        elif nome_cenario_atual== 'veterano':
            print()
            t(1)
            print('Você encontrou um veterano gente boa e ele te deu uma dica valiosa...')
            print()
            t(1)
            print('DICA: Mantenha sua nota sempre acima de 7.5...')
            print()
            t(1)
        elif nome_cenario_atual== 'professor2': 
            print('A wild Pelicano has appeared!!!')
            t(2)
            print()
            print('A:Taxa de variação')
            t(0.2)
            print('B:Número de euler')
            t(0.2)
            print('C:Equação a diferenças')
            t(0.2)
            print('D:Taxa de variação instantânea')
            t(0.2)
            resposta=input('Pelicano:O que é uma derivada?')
            while resposta!='A' and resposta!='B' and resposta!='C' and resposta!='D':
                print('Opção Inválida')
                resposta=input('Pelicano:O que é uma derivada?')
            if resposta=='D':
                print('Eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeexato, você ganhou 0.3 pontos')
                nota+=0.3
            else:
                print('Eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeerrado,perdeu 1.5 ponto na média!')
                nota=nota-1.5
            print('Sua média agora é de {}'.format(nota))
            print()
            Inventario.append('ModSim')
        elif nome_cenario_atual== 'professor3': 
            print('OH NO')
            print()
            t(0.5)
            print('O professor de Instrumed está pedindo o seu relatório')
            t(2)
            if 'relatório Instrumed' in Inventario:
                print('Boa.... Como você entregou o relatório antes da data, toma aqui uns pontinhos de bônus...')
                nota+=0.5
                t(1)
                print('Você ganhou 0.5 de bônus... Sua nota agora é de {}'.format(nota))
            else:
                print('Como você não tinha o relatório em mãos, Carlinhos te fez uma pergunta...')
                print()
                t(1)
                print('A:Potenciômetro')
                t(0.2)
                print('B:Protoboard')
                t(0.2)
                print('C:Multímetro')
                t(0.2)
                print('D:Trimpot')
                t(0.2)
                resposta=input('Carlos Ribeiro: Qual é o aparelho de medição usado nos laboratórios?')
                while resposta!='A' and resposta!='B' and resposta!='C' and resposta!='D':
                    print('Opção Inválida')
                    resposta=input('Carlos Ribeiro: Qual é o aparelho de medição usado nos laboratórios?')
                if resposta=='C':
                    print('Carlos Ribeiro: Boa, você acertou e ganhou 0.2 de média')
                    nota+=0.2
                else:
                    print('Que pena, você errou e perdeu 1 ponto na sua média!')
                    nota=nota-1
                print('Sua média agora é de {}'.format(nota))
                print()
            Inventario.append('instrumed')
        elif nome_cenario_atual== 'professor4':      
            print('PROTÓTIPOS PRA QUARTA')
            print()
            t(1)
            print('Deu a louca em Victor e Gabriel')
            print()
            t(2)
            print('Essa não!É segunda e você só tem 2 dias pra fazer 2 protótipos, você pede o adiamento, mas ele te faz uma pergunta em troca') 
            print()
            t(2)
            if 'DYM' in Inventario:
                print('Eu: Calma, eu tenho um livro que vocês vão gostar')
                t(2)
                print('Profs: Uau!!! Você tem o livro do dym, dessa vez você escapou..')
                #del 'DYM'do inventario
            else:
                print('A:É um protótipo pronto para a entrega')
                t(0.2)
                print('B:É um protótipo que ainda está em skecth ')
                t(0.2)
                print('C:É um protótipo feito para entender melhor o problema')
                t(0.2)
                print('D:É um protótipo quase em seu estado final')
                t(0.2)
                resposta=input('Victor Macul: O que é um protótipo sujo?')
                while resposta!='A' and resposta!='B' and resposta!='C' and resposta!='D':
                    print('Opção Inválida')
                    resposta=input('Victor Macul: O que é um protótipo sujo?')
                if resposta=='C':
                    print('Victor Macul: Boa! Você acertou e ganhou 0.5 de média')
                    nota+=0.5
                else:
                    print('Acho melhor você comecar a ler o DYM, peeeeelo amoooor de deus!!! Você perdeu 1 ponto na média!')
                    nota=nota-1
                    print('Sua nota agora é {}'.format(nota))
                print()
            Inventario.append('Natdes')
            print()
        elif nome_cenario_atual== 'livro':
            print()
            print('A:Livro sobre Python')
            t(0.2)
            print('B:DYM')
            t(0.2)
            resposta=input('Qual livro você quer?')
            while resposta not in A and resposta not in B:
                    print('Opção Inválida')
                    resposta=input('Qual livro você quer?')
            if resposta in A:
                print('Boa escolha guerreiro(a)...Acho que este livro pode ser útil')
                Inventario.append('Livro Python')
            elif resposta in B:
                print('Boa escolha...Victor Macul ficará orgulhoso')
                Inventario.append('DYM')
            print()
        elif nome_cenario_atual== 'imprimir':
            print()
            print('Aqui você pode imprimir:')
            t(1)
            print('A-Leitura obrigatória de GDE')
            t(0.2)
            print('B-Relatório de Instrumed')
            t(0.2)
            resposta=input('O que você quer? ')
            while resposta not in A and resposta not in B:
                    print('Opção Inválida')
                    resposta=input('Qual livro você quer?')
            if resposta in A:
                print('Boaaaaa... Fernando vai ficar orgulhoso')
                Inventario.append('Leitura GDE')
            else:
                print('O Carlinhos vai amar que você adiantou a entrega do seu relatório')
                Inventario.append('Relatório de Instrumed')
            print()
        
        elif nome_cenario_atual== 'restaurante':
            if r==0:
                print('Você deve estar com fome')
                t(1)
                print('Coma uma comida e ganhe 20 de hp')
                t(2)
                print('Delicious!!!')
                eu['hp']+=20
                print('hp atual:{0}'.format(eu['hp']))
                r=1
                print()
            else:
                print('Você acabou com toda a nossa comida!')
                print()
                t(2)
                print('Parece que você comeu muuuito da última vez')
                print()
        
        elif nome_cenario_atual== 'techlab':
            if 'Arma de portais' not in Inventario:
                
                inimigo=competidores['Monstro do techlab']
                print('OOOOOOOOOH')
                print()
                t(1)
                print('Você achou um Monstro pelo Techlab')
                print()
                t(2)
                print('Seu status de combate')
                print(eu)
                t(2)
                print()
                print('Status de combate de seu oponente')
                print(inimigo)
                t(2)
                print() 
                decida=input('Correr ou lutar?')
                while decida!='lutar' and decida!='correr':
                    print('Opção Inválida')
                    decida=input('Correr ou lutar?')
                while eu['hp']>0 and inimigo['hp']>0 and decida=='lutar':
                    print('>>>Sua vez de atacar:')
                    t(1)
                    print('Voce tirou {0} de hp do seu oponente'.format(eu['atk']-inimigo['def']))
                    inimigo['hp']-=eu['atk']-inimigo['def']
                    t(1)
                    if inimigo['hp']>0:
                        print('>>>Vez do seu inimigo:')
                        t(1)
                        print('Você perdeu {0} de hp para seu oponente'.format(inimigo['atk']-eu['def']))
                        eu['hp']-=inimigo['atk']-eu['def']
                        print()
                        t(1)
                        print('>>>Seu status de combate')
                        print(eu)
                        t(2)
                        print()
                        print('>>>Status de combate de seu oponente')
                        print(inimigo)
                        t(2)
                        decida=input('Correr ou lutar?')
                        while decida!='lutar' and decida!='correr':
                            print('Opção Inválida')
                            decida=input('Correr ou lutar?')
                if inimigo['hp']<=0:
                    print()
                    print('Seu status de combate: {0}'.format(eu))
                    print()
                    t(1)
                    print('Parabéns, você derrotou o monstro do Techlab')
                    t(2)
                    print('Você achou uma invenção bem esquisita no TechLab...')
                    t(2)
                    print('Nusssssss! Você encontrou um portal de teletransporte..')
                    t(2)
                    print('Parece que valeu a pena você ter derrotado esse monstro')
                    t(2)
                    Inventario.append('Arma de portais')
                elif decida=='correr':
                    print('Vish... Parece que temos um arregão por aqui...Você perdeu 2 pontos de defesa')
                    eu['def']-=2
                    print('Seu status de combate:{0}'.format(eu))
                else:
                    game_over=True
            else:
                print('Não tem nada de interessante para fazer aqui...')
                print()
                
        elif nome_cenario_atual== 'auditorio':
            if 'Excalibur' not in Inventario:
                print('Excalibur')
                print('-'*len('excalibur'))
                t(1)
                print('Você achou a Espada Lendária para derrotar monstros disfarçados de pessoas')
                print('Ganhou 40 de atk')
                eu['atk']+=40
                print('Seu status de combate:{0}'.format(eu))
                Inventario.append('Excalibur')
            else:
                print('Parece que não tem nada de interessante para fazer aqui...')
                print()
        elif nome_cenario_atual== 'professor':
            if nota<7.5:
                print('Raul ikeda: Você não tem nota suficiente e nem merecimento, volte pra casa')
                game_over=True
            else:
                print('Raul ikeda: Tudo bem,vou adiar o EP para o outro mês')
                t(2)
                print('Não....Pera...Tem algo de errado...')
                t(1)
                print('Quando você estava saindo, um monstro te atacou e você percebe que na verdade o monstro era o Raul disfarçado')
                t(3)
                if 'Excalibur' not in Inventario:
                    print('Monstro do Python(Raul):Comigo sua chance vai a 0% HA HA HA HA HA')
                else:
                    print('Monstro do Python: Mas o que é isso na sua mão?')
                    t(1)
                    print('Eu: É a lendaria Excalibur... To pronto pro FIGHT')
                t(2)
                vilao_atual='Raul Alienigena'
                inimigo=competidores[vilao_atual]
                print('Batalhe e Derrote o Monstro do Python')
                t(1)
                print()
                print('Seus status de combate')
                print(eu)
                print()
                t(2)
                print('Status de combate de seu oponente')
                print(inimigo)
                print()
                t(2)
                
                decida=input('Correr ou lutar?')
                while decida!='lutar' and decida!='correr':
                    print('Opção Inválida')
                    decida=input('Correr ou lutar?')
                while eu['hp']>0 and inimigo['hp']>0 :
                    if decida=='correr' and d==0:
                        print('O monstro te alcançou e você terá que lutar de qualquer jeito')
                        d=1
                    print()
                    t(2)
                    print('>>>Sua vez de atacar')
                    t(1)
                    print('Você tirou {0} de hp do seu oponente'.format(eu['atk']-inimigo['def']))
                    inimigo['hp']-=eu['atk']-inimigo['def']
                    if inimigo['hp']>0:
                        print()
                        t(2)
                        print('>>>Vez do seu inimigo')
                        t(1)
                        print('Você perdeu {0} de hp para seu oponente'.format(inimigo['atk']-eu['def']))
                        eu['hp']-=inimigo['atk']-eu['def']
                        print()
                        t(1)
                        print('>>>Seu status de combate')
                        t(2)
                        print(eu)
                        print()
                        t(1)
                        print('>>>Status de combate de seu oponente')
                        t(2)
                        print(inimigo)
                if eu['hp']<=0:
                    print('Você nunca irá ganhar de mim')
                    t(1)
                    print('Morra verme!')
                else:
                    print('Mas como você me derrotou????Isso é impo..ssi..v...Nãaaaaaaaa...')
        elif nome_cenario_atual== 'predionovo':
            nota=0
        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            nota=0
            game_over = True
        elif'fim' in opcoes:
            game_over = True
            
        else:
            print()
            for escolhas,acoes in opcoes.items():
                print(escolhas+': '+acoes)
                t(0.2)
            if 'Arma de portais' in Inventario:
                print('Arma de portais: Te teleporta para QUALQUER lugar do jogo que já foi desbloqueado')
                
            escolha=input("Qual opção você quer?")
            escolha=escolha.lower()
            escolha=''.join(escolha.split())
            while escolha not in opcoes and escolha!='armadeportais':
                print('Opção Inválida')
                escolha=input("Qual opção você quer")
                escolha=escolha.lower()
                escolha=''.join(escolha.split())
            if escolha in opcoes:
                if 'instrumed' and 'Modsim' and 'Natdes' and 'GDE'  not in Inventario:
                    while escolha=='professor':
                        print('Sala bloqueada!!! ')
                        print('Para desbloquear você tem que falar com todos os professores antes de ir para a sala do Raul')
                        print()
                        print('Você está de volta no elevador')
                        print()
                        escolha=input("Qual opção você quer?")
                        escolha=escolha.lower()
                        escolha=''.join(escolha.split())
                        while escolha not in opcoes:
                            print('Opção Inválida')
                            escolha=input("Qual opção você quer?")
                            escolha=escolha.lower()
                            escolha=''.join(escolha.split())
                nome_cenario_atual= escolha
            elif escolha=='armadeportais' and 'Arma de portais' in Inventario:
                for k in cenarios.keys():
                    print(k)
                    t(0.1)
                escolha=input("Qual opção você quer?")
                escolha=escolha.lower()
                escolha=''.join(escolha.split())
                if 'instrumed' and 'Modsim' and 'Natdes' and 'GDE' and 'GDE' not in Inventario:
                    while escolha=='professor':
                        print('Sala bloqueada!!! ')
                        t(1)
                        print('Para desbloquear você tem que falar com todos os professores antes de ir para a sala do Raul')
                        print()
                        escolha=input("qual opção vc quer?")
                        escolha=escolha.lower()
                        escolha=''.join(escolha.split())
                        while escolha not in cenarios:
                            print('Opção Inválida')
                            escolha=input("Qual opção você quer?")
                            escolha=escolha.lower()
                            escolha=''.join(escolha.split())
                else:
                    while escolha not in cenarios:
                        print('Opção Inválida')
                        escolha=input("Qual opção você quer?")
                        escolha=escolha.lower()
                        escolha=''.join(escolha.split())
            nome_cenario_atual= escolha
    if nota>=7.5 and eu['hp']>0:
        print('You WIN')
        t(1)
        print('Mas não perca tempo comemorando')
        t(1)
        print('Você ainda tem que fazer o seu EP ate amanhã, boa Sorte')
    else:
        print("Você perdeu e não conseguiu o adiamento do EP! Mais sorte da próxima vez... ")


# Programa principal.
if __name__ == "__main__":
    main()