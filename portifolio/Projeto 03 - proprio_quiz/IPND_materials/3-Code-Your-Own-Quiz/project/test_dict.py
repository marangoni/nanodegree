# Programa test dict
# Teste da estrutura dict do python


data = {
    'facil': {
        'frase':  "'Hello __1__!' Em __2__ isto e particularmente facil; tudo o que voce deve fazer e digitar: __3__ 'Hello __1__ !'. Os diferentes blocos de programa sao separados atraves de __4__",
        'respostas': ["world", "Python", "print", "indentacao"],
        'falhas': 5
    },
    'medio': {
        'frase': "Construcoes de Python incluem: estrutura de __1__ (if, else, elif); estrutura de __2__ (for, while), que itera por um container, capturando cada elemento em uma variavel local dada; construcao de __3__ (class), construcao de __4__ (def).",
        'respostas': ["selecao", "repeticao", "classes", "sub-rotinas"],
        'falhas': 3
    },
    'dificil': {
        'frase': "Uma __1__ eha definida com class nome:, e o codigo seguinte eh a composição dos __2__. Os metodos sao chamados objeto.metodo(argumento1, argumento2, ...) e sao definidos iguais a uma funcao, como __3__(self, argumento1, argumento2, ...). Veja que o __4__ self contera uma referencia para a instancia da classe definida em objeto quando for efetuada esta chamada. Os __2__ da __1__ podem ser acessados em qualquer lugar da __1__, e os __3__ de instancia devem ser declarados dentro dos __3__ utilizando a referencia a instancia atual (self).",
        'respostas': ["classe", "atributos", "metodo", "parametro"],
        'falhas': 2
    }
}

nivel = raw_input('Escolha o nivel: (facil / medio / dificil)').lower() # facil
# imprimindo
print data[nivel]['frase'] #  Facil __1__  .  __2__ .  __3__  .   __4__ .
print data[nivel]['respostas'][3] #  quatro_facil
print 'nivel: {0}, falhas: {1}'.format(nivel, data[nivel]['falhas']) # nivel: facil, falhas: 5
