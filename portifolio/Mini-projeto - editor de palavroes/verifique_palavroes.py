import urllib

def leia_texto():
    quotes = open("texto.txt")
    conteudo = quotes.read()
    #print conteudo
    quotes.close()
    check_paralavroes(conteudo)

def check_paralavroes(text_to_check):
    connection = urllib.urlopen("http://www.purgomalum.com/service/containsprofanity?text="+text_to_check)
    output = connection.read()
    #print output
    connection.close()

    if "true" in output:
        print "Alerta de palavroes!!!! Verifique seu texto"
    elif "false" in output:
        print "Texto verificado. Sem palavroes."
    else:
        print "Seu texto não pode ser verificado."



leia_texto()
