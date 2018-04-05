#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
##################################################################################
# Encoding para utilizacao de caracteres acentuados
# IPND Stage 2 Final Project
# Luiz C M de Oliveira
# janeiro de 2018
# ################################################################################


# Funcao - escolha_nivel - retorna o valor do nivel escolhido pelo usuario
def escolha_nivel():
    niveis = ["facil", "medio", "dificil"]
    user_input = raw_input("Escolha o nivel do jogo - facil, medio ou dificil: ")

    while user_input not in niveis:
        print "Esta opcao nao existe!"
        user_input = raw_input("Escolha o nivel do jogo - facil, medio ou dificil: ")
    else:
        print
        print "Nivel selecionado " + user_input + "."
        return user_input

# Funcao frase_nivel - retorna a frase a ser preenchida, conforme o nivel escolhido pelo jogador.
def frase_nivel(game_level):
    frase_easy = "'Hello __1__!' Em __2__ isto e particularmente facil; tudo o que voce deve fazer e digitar: __3__ 'Hello __1__ !'. Os diferentes blocos de programa são separados por __4__"

    frase_medium = "Construções de Python incluem: estrutura de __1__ (if, else, elif); estrutura de __2__ (for, while), que itera por um container, capturando cada elemento em uma variável local dada; construção de __3__ (class), construção de __4__ (def)."

    frase_hard = "Uma __1__ é definida com class nome:, e o código seguinte é a composição dos __2__. Os métodos são chamados objeto.método(argumento1, argumento2, ...) e são definidos iguais a uma função, como __3__(self, argumento1, argumento2, ...). Veja que o __4__ self conterá uma referência para a instância da classe definida em objeto quando for efetuada esta chamada. Os __2__ da __1__ podem ser acessados em qualquer lugar da __1__, e os __3__ de instância devem ser declarados dentro dos __3__ utilizando a referência à instacia atual (self)."

    if game_level == "facil":
        return frase_easy
    elif game_level == "medio":
        return frase_medium
    elif game_level =="dificil":
        return frase_hard

# retorna respostas corretas, conforme nivel selecionado pelo jogador
def answer_level(game_level):
    answer_easy = ["world", "Python", "print", "indentacao"]
    answer_medium = ["selecao", "repeticao", "classes", "sub-rotinas"]
    answer_hard = ["classe", "atributos", "metodo", "parametro"]

    if game_level == "facil":
        return answer_easy
    elif game_level == "medio":
        return answer_medium
    elif game_level =="dificil":
        return answer_hard



# Função principal - game()
def game():


    no_tentativas = 3

    print "Jogo das lacunas! Voce eh fera em Python?"
    print
    nivel = escolha_nivel()
    print "Preencha as lacunas"
    print "Boa sorte!"
    print "-------------------------------------------------------------------"
    print
    frase = frase_nivel(nivel)
    sample_answer = answer_level(nivel)
    print frase
    i = 0
    t = 0



    while i < no_tentativas:
        user_input = raw_input("_1_ = ")
        if user_input in sample_answer:
            print "Correto!"
            frase = frase.replace("__1__", user_input)
            print frase
            i=no_tentativas
        else:
            print "Resposta incorreta! Tente novamente..."
            i = i+1

    i=0
    while i < no_tentativas:
        user_input = raw_input("_2_ = ")
        if user_input in sample_answer:
            print "Correto!"
            frase = frase.replace("__2__", user_input)
            print frase
            i=no_tentativas
        else:
            print "Resposta incorreta! Tente novamente..."
            i = i+1

    i=0
    while i < no_tentativas:
        user_input = raw_input("_3_ = ")
        if user_input in sample_answer:
            print "Correto!"
            frase = frase.replace("__3__", user_input)
            print frase
            i=no_tentativas
        else:
            print "Resposta incorreta! Tente novamente..."
            i = i+1

    while i < no_tentativas:
        user_input = raw_input("_4_ = ")
        if user_input in sample_answer:
            print "Correto!"
            frase = frase.replace("__4__", user_input)
            print frase
            i=no_tentativas
        else:
            print "Resposta incorreta! Tente novamente..."
            i = i+1

    if i==4:
        print "You win! End of game!"
    else:
        print "Sorry, voce perdeu o jogo..."
    return

game()
