#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
##################################################################################d
# Encoding para utilizacao de caracteres acentuados
# IPND Stage 2 Final Project
# Luiz C M de Oliveira
# janeiro de 2018
# ################################################################################


# Funcao - escolha_nivel - retorna o valor do nivel escolhido pelo usuario
def escolha_nivel():
    niveis = ["easy", "medium", "hard"]
    user_input = raw_input("Please, choose the game level - easy, medium or hard: ")

    while user_input not in niveis:
        print "Not an option!"
        user_input = raw_input("Please, choose the game level - easy, medium or hard: ")
    else:
        print
        print "Game level: " + user_input + "."
        return user_input

# Funcao frase_nivel - retorna a frase a ser preenchida, conforme o nivel escolhido pelo jogador.
def frase_nivel(game_level):
    frase_easy = "'Hello __1__!'  In __2__ this is particularly easy; all you have to do is type in:__3__ 'Hello __1__!'"

    frase_medium = "'A __1__ is created with the def keyword.  You specify the inputs a __1__ takes by adding __2__ separated by commas between the parentheses. __1__s by default returns __3__ if you don't specify the value to return.'"

    frase_hard ="You can also create binary operators, like __6__ and __7__, which allow + and - to be used by __4__s of the __1__."

    if game_level == "easy":
        return frase_easy
    elif game_level == "medium":
        return frase_medium
    elif game_level =="hard":
        return frase_hard

# retorna respostas corretas, conforme nivel
def answer_level(game_level):
    answer_easy = ["world", "Python", "print"]
    answer_medium = ["function", "parameters", "low"]
    answer_hard = ["+", "-", "function", "Python"]

    if game_level == "easy":
        return answer_easy
    elif game_level == "medium":
        return answer_medium
    elif game_level =="hard":
        return answer_hard

# Função principal - game()
def game():

    print "Fill-the-blanks game! Are you keen in Python?"
    print
    nivel = escolha_nivel()
    print "Fill the blanks!"
    print "Good luck!"
    print
    frase = frase_nivel(nivel)
    sample_answer = answer_level(nivel)
    print frase
    i = 0
    while i<3:
        user_input = raw_input("_1_ = ")
        if user_input in sample_answer:
            print "Correto!"
            frase = frase.replace("__1__", user_input)
            print frase
            i=3
        else:
            print "Resposta incorreta!"
            i = i+1
    i=0
    while i < 3:
        user_input = raw_input("_2_ = ")
        if user_input in sample_answer:
            print "Correto!"
            frase = frase.replace("__2__", user_input)
            print frase
            i=3
        else:
            print "Resposta incorreta!"
            i = i+1
    i=0
    while i < 3:
        user_input = raw_input("_3_ = ")
        if user_input in sample_answer:
            print "Correto!"
            frase = frase.replace("__3__", user_input)
            print frase
            i=3
        else:
            print "Resposta incorreta!"
            i = i+1

    print "You win! End of game!"
    return

game()
