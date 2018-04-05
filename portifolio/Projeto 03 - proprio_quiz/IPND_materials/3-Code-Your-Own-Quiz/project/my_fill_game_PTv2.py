
##################################################################################
# Jogo Fill the blanks
# IPND Stage 2 Final Project
# Luiz C M de Oliveira
# abril de 2018
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
#       parametro: game_level - nivel do jogo escolhido pelo jogador

def frase_nivel(game_level):
    frase_easy = "'Hello __1__!' Em __2__ isto e particularmente facil; tudo o que voce deve fazer e digitar: __3__ 'Hello __1__ !'. Os diferentes blocos de programa sao separados atraves de __4__"

    frase_medium = "Construcoes de Python incluem: estrutura de __1__ (if, else, elif); estrutura de __2__ (for, while), que itera por um container, capturando cada elemento em uma variavel local dada; construcao de __3__ (class), construcao de __4__ (def)."

    frase_hard = "Uma __1__ eha definida com class nome:, e o codigo seguinte eh a composição dos __2__. Os metodos sao chamados objeto.metodo(argumento1, argumento2, ...) e sao definidos iguais a uma funcao, como __3__(self, argumento1, argumento2, ...). Veja que o __4__ self contera uma referencia para a instancia da classe definida em objeto quando for efetuada esta chamada. Os __2__ da __1__ podem ser acessados em qualquer lugar da __1__, e os __3__ de instancia devem ser declarados dentro dos __3__ utilizando a referencia a instancia atual (self)."

    if game_level == "facil":
        return frase_easy
    elif game_level == "medio":
        return frase_medium
    elif game_level =="dificil":
        return frase_hard

# retorna respostas corretas, conforme nivel selecionado pelo jogador
#       parametro: game_level - nivel do jogo escolhido pelo jogador
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

# define o numero de tentativas em funcao do nivel do jogo
#       parametro: game_level - nivel do jogo escolhido pelo jogador
def tentativa_nivel(game_level):

    if game_level == "facil":
        return 5
    elif game_level == "medio":
        return 3
    elif game_level =="dificil":
        return 2

# Funcao que retorna true se o jogador preencheu corretamente a lacuna
# e false se errou
# parametros: lacuna a ser preenchida
#             limite_tentativas - limite de tentativas conforme Nivel
#             frase - frase conforme o Nivel
#             respostas - resposta conforme o Nivel
#
def preenche_lacuna(lacuna, limite_tentativas,frase, respostas):
    global nova_frase
    i=0
    while i < limite_tentativas:
        user_input = raw_input("_" + str(lacuna) + "_ = ")
        if user_input in respostas:
            print "Correto!"
            print
            nova_frase = frase.replace("_" + str(lacuna) + "_", user_input.upper())
            print nova_frase
            return True
        else:
            print "Resposta incorreta! Tente novamente..."
            i = i+1
            if i<> limite_tentativas:
                print "Voce tem mais " + str(limite_tentativas-i) + " tentativas"
                print

    return False



# Função principal - game()
# Apresenta as regras
# Solicita a escolha do Nivel
# Apresenta a frase
# Aguarda o preenchimento pelo jogador
def game():
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
    nivel = escolha_nivel()
    print
    frase = frase_nivel(nivel)
    resposta = answer_level(nivel)
    tentativas = tentativa_nivel(nivel)
    print
    print "Preencha as lacunas desta frase:"
    print frase
    print

    # Loop para preenchimento das lacunas
    # se o jogador preencher corretamente resultado igual a True e o jogo continua
    # se o jogador preencher incorretamente resultado igual a False e o jogo acaba
    for n in range(1,5):
        resultado = preenche_lacuna(n, tentativas, frase, resposta)
        # atualiza frase
        frase = nova_frase
        if resultado == False:
            print
            print "Voce perdeu o jogo! Tente outra vez!"
            break
            return

    # Se o jogador acertou todas as lacunas parabeniza jogador
    if resultado == True:
        print
        print "Parabens! Voce eh mesmo fera em Python!!!!"
        print
    return

game()
