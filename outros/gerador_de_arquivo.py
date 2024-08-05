import os

log = open("log.txt", "a")

path = os.listdir('C:\Projetos\python_exemplos\outros')

cont = 0
linha = 1

for arquivo in path:
    open(str(arquivo), "r")
    for nome in arquivo:
        if "LISTBOX" in nome:
            cont = cont + 1
            log.write("Expressao na linha :" + str(linha) + "\n")
        linha = linha + 1
    #log.write(str(arquivo) + "\n")
    #print(nome)
log.write("Total de expressoes encontradas :" + str(cont) + "\n")
log.write("Quantidade de linhas do arquivo :" + str(linha) + "\n")

log.close()
