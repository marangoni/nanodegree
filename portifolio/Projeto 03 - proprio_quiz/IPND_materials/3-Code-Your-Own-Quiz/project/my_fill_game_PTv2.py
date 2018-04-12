# -*- coding: utf-8 -*-
###############################################################################
# Jogo Fill the blanks
# IPND Stage 2 Final Project
# Luiz C M de Oliveira
# abril de 2018
# Versao: Atualizada usando a estrutura dict
############################################################################

#definicoes do jogo
data = {
    'facil': {
        'frase':  """'Hello __1__!' Em __2__ isto é particularmente facil; tudo o que voce deve fazer e digitar: __3__ 'Hello __1__ !'. Os diferentes blocos de programa sao separados atraves de __4__""",
        'respostas': ["world", "Python", "print", "indentacao"],
        'tentativas': 5
    },
    'medio': {
        'frase': """Construcoes de Python incluem: estrutura de __1__ (if, else, elif); estrutura de __2__ (for, while), que itera por um container, capturando cada elemento em uma variavel local dada; construcao de __3__ (class), construcao de __4__ (def).""",
        'respostas': ["selecao", "repeticao", "classes", "sub-rotinas"],
        'tentativas': 3
    },
    'dificil': {
        'frase': """Uma __1__ eh definida com class nome:, e o codigo seguinte eh a composicao dos __2__. Os metodos sao chamados objeto.metodo(argumento1, argumento2, ...) e sao definidos iguais a uma funcao, como __3__(self, argumento1, argumento2, ...). Veja que o __4__ self contera uma referencia para a instancia da classe definida em objeto quando for efetuada esta chamada. Os __2__ da __1__ podem ser acessados em qualquer lugar da __1__, e os __3__ de instancia devem ser declarados dentro dos __3__ utilizando a referencia a instancia atual (self).""",
        'respostas': ["classe", "atributos", "metodo", "parametro"],
        'tentativas': 2
    }
}

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
        print
        return user_input

# Funcao que retorna true se o jogador preencheu corretamente a lacuna
# e false se errou
# parametros: lacuna a ser preenchida
#             limite_tentativas - limite de tentativas conforme Nivel
#             frase - frase conforme o Nivel
#             respostas - resposta conforme o Nivel
#
def preenche_lacuna(lacuna,limite_tentativas,frase,respostas):
    global nova_frase
    index=0
    while index < limite_tentativas:
        user_input = raw_input("_" + str(lacuna) + "_ = ")
        if user_input in respostas:
            print "Correto!"
            print
            nova_frase = frase.replace("_" + str(lacuna) + "_", user_input.upper())
            print nova_frase
            return True
        else:
            print "Resposta incorreta! Tente novamente..."
            index = index + 1
            if index<> limite_tentativas:
                print "Voce tem mais " + str(limite_tentativas-index) + " tentativas"
                print
                nova_frase = frase
    return False

# Funcao que formata e apresenta a tela de abertura do jogo
def abertura():
    print "*****************************************"
    print "Jogo das lacunas! Voce eh fera em Python?"
    print "*****************************************"
    print
    print "*****************************************"
    print "REGRAS:"
    print "Voce deve preencher as lacunas com a palavra correta."
    print "O numero de tentativas varia conforme o nivel escolhido: "
    print "facil - 5 tentativas, medio - 3 tentativas, dificil - 2 tentativas "
    print "Boa sorte!"
    print "*****************************************"
    print
    return

# Funcao que formata e apresenta a frase do jogo
def print_frase(frase):
    print
    print "Preencha as lacunas desta frase:"
    print frase
    print
    return

# Funcao que formata e apresenta a mensagem perdeu
def mensagem_perdeu():
    print
    print "Voce perdeu o jogo! Tente outra vez!"
    return

# Funcao que formata e apresenta a mensagem perdeu
def mensagem_ganhou():
    print
    print "Parabens! Voce eh mesmo fera em Python!!!!"
    print
    return

# Função principal - game()
# Solicita a escolha do Nivel
# Apresenta a frase
# Aguarda o preenchimento pelo jogador
def game():
    #definicoes do jogo
    numero_max_tentativas = 5
    abertura()
    nivel = escolha_nivel()
    frase = data[nivel]['frase']
    resposta = data[nivel]['respostas']
    tentativas = data[nivel]['tentativas']
    print_frase(frase)

    # Loop principal do jogo
    # se o jogador preencher corretamente resultado igual a True e o jogo continua
    # se o jogador preencher incorretamente resultado igual a False e o jogo acaba
    for tentativa in range(1,numero_max_tentativas):
        resultado = preenche_lacuna(tentativa, tentativas, frase, resposta)
        # atualiza frase
        # variavel global nova_frase atualizada na rotina preenche_lacuna
        frase = nova_frase
        if resultado == False: # Se o jogador errou todas as tentativas
            mensagem_perdeu()
            break
            return
    if resultado == True: # Se o jogador acertou as 4 lacunas
        mensagem_ganhou()
    return

# Funcao principal do programa
game()
