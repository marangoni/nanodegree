#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

# Encoding para utilizacao de caracteres acentuados
# IPND Stage 2 Final Project
# Luiz C M de Oliveira
# janeiro de 2018
# ################################################################################


# Funcao - escolha_nivel - retorna o valor do nivel escolhido pelo usuario
def escolha_nivel():
    niveis = ["facil", "medio", "dificil"]
    user_input = raw_input("Escolha o nível de dificuldade do jogo - facil, medio ou dificil: ")
    while user_input not in niveis:
        print "Nivel invalido!"
        user_input = raw_input("Escolha o nível de dificuldade do jogo - facil, medio ou dificil: ")
    else:
        print
        print "Você escolheu o nível " + user_input +"."
        return user_input

# Função principal - game()

def game():
    sample = '''Uma ___1___ é criada com a declaração def. Você especifica as entradas da
    ___1___ utilizando  ___2___ separados por virgulas entre parenteses. ___1___s por
    default retornam ___3___ se você não especificar um valor de retorno. ___2___ podem ser
    tipos de dados padrão tais como strings, números, dicionarios, tuple, e ___4___ ou
    podem ser mais complicados como objetos ou funções lambda.'''

    sample_answer = ["fun", "parâmetros", "None", "lista"]

    print "Bem-vindo ao jogo de preenchimento de lacunas! Teste seus conhecimentos em Python com este jogo."
    print
    nivel = escolha_nivel()
    print "Preencha as lacunas na frase abaixo. Você terá 03 chances para cada palavra."
    print "Boa sorte!"
    print
    print sample
    print
    for i in range(0,3):
        user_input = raw_input("_1_ = ")
        if user_input in sample_answer:
            print "Correto!"
            sample = sample.replace("___1___", user_input)
            print sample
        else:
            print "Resposta incorreta!"
    return

game()
