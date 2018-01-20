# definir um procedimento para impressao de todos os elementos de uma lista

def print_all_elements(p):
    i = 0
    while i < len(p):
        print p[i]
        i = i + 1

a = ['paul', 'malcoln', 'william', 1900,[0,1]]

print_all_elements(a)
