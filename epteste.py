# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 14:10:14 2019

@author: insper
"""
import time

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
            "opcoes": {'VITÓRIA':'Ganhou o JOGO'}
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
                'professor2':'Entra na sala de um professor',
                'elevador':'Acesso a todos os andares',
                'imprimir':'Vai até a reprografia'}}
    ,"professor2": {
            "titulo": "Aula de ModSim",
            "descricao": "Você entrou na sala do seu professor",
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
                'professor3':'Entre na sala do professor',
                'elevador':'Acesso a todos os andares'}}
    ,"professor3": {
            "titulo": "Aula de InstruMed",
            "descricao": "Você chegou ao andar da sala do seu professor",
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
                "andarprofessor": "Pegar o elevador para o andar dos professores",
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
            "descricao": "Você chegou na sala do seu professor",
            "opcoes": {
                    'elevador':'Acesso a todos os andares'}}
    ,"livro": {
            "titulo": "Escolha um livro",
            "descricao": "Você chegou na estante em um instante oooooaaaaauuuuu!!!",
            "opcoes": {
                    "inicio": "Voltar para o saguão de entrada"}}
    ,"predionovo": {
            "titulo": "vc esta atravessando a rua e...",
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
            "titulo": "Auditorio",
            "descricao": "Voce está no auditório",
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
            "def":0}
    ,'Raul Alienigena':{
            'hp':200,
            'atk':40,
            'def':20}
    ,'Zumbi0':{
            'hp':35,
            'atk':20,
            'def':3}
    ,'Zumbi1':{
            'hp':30,
            'atk':10,
            'def':4}
    ,'Zumbi2':{
            'hp':40,
            'atk':5,
            'def':2}
    ,'Zumbi3':{
            'hp':30,
            'atk':15,
            'def':5}
    ,'Zumbi4':{
            'hp':20,
            'atk':20,
            'def':5}
    ,'Zumbi5':{
            'hp':50,
            'atk':15,
            'def':3}
            }
    vilao_atual=competidores['Zumbi0']
    
        
    return competidores,vilao_atual

def main():
    nota=10
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
            competidores,vilao_atual=combate()
            if c==8:
                vilao_atual=competidores['Zumbi1']
            elif c==12:
                vilao_atual=competidores['Zumbi2']
            elif c==16:
                vilao_atual=competidores['Zumbi3']
            elif c==20:
                vilao_atual=competidores['Zumbi4']
            elif c>24:
                vilao_atual=competidores['Zumbi5']
            inimigo=vilao_atual
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
                print()
            while eu['hp']>0 and inimigo['hp']>0 and decida=='lutar':
                print('>>>Sua vez de atacar')
                print('Voce tirou {0} de hp do seu oponente'.format(eu['atk']-inimigo['def']))
                inimigo['hp']-=eu['atk']-inimigo['def']
                if inimigo['hp']>0:
                    print('>>>Vez do seu inimigo')
                    print('Voce perdeu {0} de hp para seu oponente'.format(inimigo['atk']-eu['def']))
                    eu['hp']-=inimigo['atk']-eu['def']
                    print()
                    print('>>>Seus status de combate')
                    print(eu)
                    print()
                    print('>>>Status de combate de seu oponente')
                    print(inimigo)
                    print()
                    decida=input('Quer continuar:correr ou lutar?')
                    while decida!='lutar' and decida!='correr':
                        print('Opção Inválida')
                        decida=input('Quer continuar:correr ou lutar?')
            if eu['hp']<=0:
                game_over=True
            else:
                if decida=='lutar': 
                    print('Parabéns vc derrotou o zumbi veterano e ganhou mais 3 pontos de ataque')
                    eu['atk']+=3
                    print(eu)
                    c+=1
                if decida=='correr':
                    print('Vish... Parece que temos um arregao por aqui...Voce perdeu 2 pontos de defesa')
                    eu['def']-=2
                    print(eu)
        else:       
            c+=1
        cenario_atual = cenarios[nome_cenario_atual]
        print()
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
            resposta=input('Fernando Ribeiro:Qual matéria resume o método científico?')
            while resposta!='A' and resposta!='B' and resposta!='C' and resposta!='D':
                print('Opção Inválida')
                resposta=input('Fernando Ribeiro:Qual materia resume o método científico?')
            if resposta=='B' or resposta=='Modsim':
                print('Parabéns,você passou em GDE e ganhou 0.25 de média')
                nota+=0.25
                print('Sua média agora é de {}'.format(nota))
            else:
                nota-=-1
                print('Voce erroooooou e perdeu 1 ponto na média. Sua média agora é {}'.format(nota))
            if 'Leitura GDE' in Inventario:
                print('Fernando: O que é isso na sua mao?')
                print('Eu: Nada nao, só a leitura obrigatória da aula')
                print('Fernando: Estou muito orgulhoso de voce...Toma aqui mais alguns décimos pra te ajudar...')
                nota+=0.7
                print('Boa, você ganhou mais 0.7 de nota.... Sua nota agora é de {}'.format(nota))
                
            Inventario.append('GDE')
        elif nome_cenario_atual== 'veterano':
            print()
            print('Voce encontrou um veterano gente boa e ele te deu uma dica valiosa...')
            print()
            print('DICA: Mantenha sua nota sempre acima de 7.5...')
            print()
        elif nome_cenario_atual== 'professor2': 
            print('A wild Pelicano has appeared!!!')
            time.sleep(2)
            print()
            print('A:Taxa de variação')
            print('B:Número de euler')
            print('C:Equação a diferenças')
            print('D:Taxa de variação instantânea')
            resposta=input('Pelicano:O que é uma derivada?')
            while resposta!='A' and resposta!='B' and resposta!='C' and resposta!='D':
                print('Opção Inválida')
                resposta=input('Pelicano:O que é uma derivada?')
            if resposta=='D':
                print('Eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeexato, vc ganhou 0.3 pontos')
                nota+=0.3
            else:
                print('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeerrado,perdeu 1 ponto na media!')
                nota=nota-1
            print('Sua média agora é de {}'.format(nota))
            print()
            Inventario.append('ModSim')
        elif nome_cenario_atual== 'professor3': 
            print('OH NO')
            print()
            print('O professor de Instrumed está pedindo o seu relatório')
            if 'relatório Instrumed' in Inventario:
                print('Boa.... Como voce entregou o relatorio antes da data, toma aqui uns pontinhos de bonus...')
                nota+=0.5
                print('Voce ganhou 0.5 de bonus... Sua nota agora é de {}'.format(nota))
            else:
                print('Como voce não tinha o relatório em mãos, Carlinhos te fez uma pergunta...')
                print()
                print('A:Potenciômetro')
                print('B:Protoboard')
                print('C:Multimetro')
                print('D:Trimpot')
                resposta=input('Carlos Ribeiro:Qual è o aparelho de medição usado nos laboratórios?')
                while resposta!='A' and resposta!='B' and resposta!='C' and resposta!='D':
                    print('Opção Inválida')
                    resposta=input('Carlos Ribeiro:Qual é o aparelho de medicão usado nos laboratorios?')
                if resposta=='C':
                    print('Carlos Ribeiro:Boa, você acertou e ganhou 0.2 de média')
                    nota+=0.2
                else:
                    print('Que pena, você errou e perdeu 1 ponto na sua média!')
                    nota=nota-1
                print('Sua média gora é de {}'.format(nota))
                print()
            Inventario.append('instrumed')
        elif nome_cenario_atual== 'professor4':      
            print('PROTÓTIPOS PRA QUARTA')
            print()
            print('Deu a louca em Victor e Gabriel')
            print()
            print('Essa não!É segunda e você só tem 2 dias pra fazer 2 protótipos, você pede o adiamento, mas ele te faz uma pergunta em troca?') 
            print()
            if 'DYM' in Inventario:
                print('Eu: Calma, eu tenho um livro que vocês vão gostar')
                print('Profs: Uau!!! você tem o livro do dym,dessa vez você escapou..')
                #del 'DYM'do inventario
            else:
                print('A:É um prototipo pronto para a entrega')
                print('B:É um prototipo que ainda está em skecth ')
                print('C:É um prototipo feito para entender melhor o problema')
                print('D:É um prototipo quase em seu estado final')
                resposta=input('Victor Macul:O que é um prototipo sujo?')
                while resposta!='A' and resposta!='B' and resposta!='C' and resposta!='D':
                    print('Opção Inválida')
                    resposta=input('Victor Macul:O que é um protótipo sujo?')
                if resposta=='C':
                    print('Victor Macul:Boa! Você acertou e ganhou 0.5 de média')
                    nota+=0.5
                else:
                    print('Acho melhor voce comecar a ler o DYM, pelo amor de deus!!! Voce perdeu 1 ponto na media!')
                    nota=nota-1
                    print('Sua nota agora é {}'.format(nota))
                print()
            Inventario.append('Natdes')
            print()
        elif nome_cenario_atual== 'livro':
            print()
            print('A:Livro sobre Python')
            print('B:DYM')
            resposta=input('Qual livro vc quer?')
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
            print('Aqui voce pode imprimir:')
            print('A-Leitura obrigatória de GDE')
            print('B-Relatório de Instrumed')
            resposta=input('O que você quer? ')
            if resposta in A:
                print('Boaaaaa... Fernando vai ficar orgulhoso')
                Inventario.append('Leitura GDE')
            if resposta in B:
                print('O Carlinhos vai amar que você adiantou a entrega do seu relatório')
                Inventario.append('Relatório de Instrumed')
            print()
        
        elif nome_cenario_atual== 'restaurante':
            if r==0:
                print('Voce deve estar com fome')
                print('Coma uma comida e ganhe 20 de hp')
                print('Delicious!!!')
                eu['hp']+=20
                print('hp atual:{0}'.format(eu['hp']))
                r=1
                print()
            else:
                print('Voce acabou com toda a nossa comida!')
                print()
                print('Parece que vc comeu muuuito da última vez')
                print()
        
        elif nome_cenario_atual== 'techlab':
            if 'Arma de portais' not in Inventario:
                
                inimigo=competidores['Monstro do techlab']
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
                    print('>>>Sua vez de atacar:')
                    print('Voce tirou {0} de hp do seu oponente'.format(eu['atk']-inimigo['def']))
                    inimigo['hp']-=eu['atk']-inimigo['def']
                    if inimigo['hp']>0:
                        print('>>>Vez do seu inimigo:')
                        print('Voce perdeu {0} de hp para seu oponente'.format(inimigo['atk']-eu['def']))
                        eu['hp']-=inimigo['atk']-eu['def']
                        print()
                        print('>>>Seus status de combate')
                        print(eu)
                        print()
                        print('>>>Status de combate de seu oponente')
                        print(inimigo)
                        decida=input('correr ou lutar?')
                        while decida!='lutar' and decida!='correr':
                            print('Opção Inválida')
                            decida=input('correr ou lutar?')
                if inimigo['hp']<=0:
                    print()
                    print('Vc encontrou uma invenção bem esquisita no TechLab...')
                    print('Nusssssss! vc encontrou um portal de teletransporte..')
                    print('Parece que valeu a pena vc ter Derrotado esse monstro')
                    Inventario.append('Arma de portais')
                elif decida=='correr':
                    print('Vish... Parece que temos um arregao por aqui...Voce perdeu 2 pontos de defesa')
                    eu['def']-=2
                    print(eu)
                else:
                    game_over=True
            else:
                print('Não tem nada de interessante para fazer aqui...')
                print()
                
        elif nome_cenario_atual== 'auditorio':
            if 'Excalibur' not in Inventario:
                print('Excalibur')
                print('-'*len('excalibur'))
                print('Você achou a Espada Lendária para derrotar monstros disfarçados de pessoas')
                print('Ganhou 40 de atk')
                eu['atk']+=40
                Inventario.append('Excalibur')
            else:
                print('Parece que não tem nada de interessante para fazer aqui...')
                print()
        elif nome_cenario_atual== 'professor':
            if nota<7.5:
                print('Raul ikeda:Você não tem nota suficiente e nem merecimento, volte pra casa')
                game_over=True
            else:
                print('Raul ikeda:Tudo bem,vou adiar o EP para o outro mês')
                print('Não....Pera...Tem algo de errado...')
                print('Quando vc estava saindo, um monstro te atacou e vc percebe que na verdade o monstro era o Raul disfarçado')
                if 'Excalibur' not in Inventario:
                    print('Monstro do Python(Raul):Comigo sua chance vai a 0% HA HA HA HA HA')
                else:
                    print('Monstro do Python: Mas o que é isso na sua mão?')
                    print('Eu: É a lendaria Excalibur,então vc ja derrotou o meu irmão,outro motivo para eu te matar')
                vilao_atual='Raul Alienigena'
                inimigo=vilao_atual
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
                        print('O monstro te alcançou e você terá que lutar de qualquer jeito')
                    print()
                    print('>>>Sua vez de atacar')
                    print('Voce tirou {0} de hp do seu oponente'.format(eu['atk']-inimigo['def']))
                    inimigo['hp']-=eu['atk']-inimigo['def']
                    if inimigo['hp']>0:
                        print()
                        print('>>>Vez do seu inimigo')
                        print('Voce perdeu {0} de hp para seu oponente'.format(inimigo['atk']-eu['def']))
                        eu['hp']-=inimigo['atk']-eu['def']
                        print()
                        print('>>>Seu status de combate')
                        print(eu)
                        print()
                        print('>>>Status de combate de seu oponente')
                        print(inimigo)
                if eu['hp']<=0:
                    print('Vc nunca ira ganhar de mim')
                    print('Morra verme')
                else:
                    print('Mas como vc me derrotou????Isso é impo..ssi..v...Nãaaaaaaaa...')
        
        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            nota=0
            game_over = True
        elif'VITORIA' in opcoes:
            game_over = True
            
        else:
            print()
            for escolhas,acoes in opcoes.items():
                print(escolhas+': '+acoes)
            if 'Arma de portais' in Inventario:
                print('Arma de portais: Te teleporta para QUALQUER lugar do jogo que já foi desbloqueado')
                
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
                        print('Você está de volta no elevador')
                        print()
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
    if nota>=7.5 and eu['hp']>0:
        print('You WIN')
        print('Mas nao perca tempo comemorando')
        print('vc ainda tem que fazer o seu EP ate amanha, Boa Sorte')
    else:
        print("Você Perdeu e nao conseguiu o adiamento do EP! Mais sorte da próxima vez... ")


# Programa principal.
if __name__ == "__main__":
    main()