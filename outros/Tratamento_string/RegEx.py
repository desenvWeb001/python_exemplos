import re

endereco = "Rua: Monsenhor Pires Ferreira 373A, Tibiri, Santa Rita, PB, 58303-360, 58305-360"

#criando expressão padrão, cada colchete representa um caracter que pode ser de 1 a 9

#padrao = re.compile('[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]')
# utilizando quantificadores na reg expres
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")

busca = padrao.search(endereco) #retorna um objeto Match caso não identifique a expressão retorna None

if busca:
    #group() retorna a string encontratada
    cep = busca.group()
    print(cep)