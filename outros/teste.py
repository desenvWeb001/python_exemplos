import os, webbrowser

#os.system('cd C:\Projetos\python_exemplos\outros')


print(os.getcwd())

path = os.listdir('C:\Projetos\python_exemplos\outros')

lista = []

for arquivo in path:
    lista.append(arquivo)
    open(str(lista), "r")
print(lista)

#webbrowser.open_new(os.path.realpath(diretorio))

