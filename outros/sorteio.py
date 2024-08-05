

qtd_participantes = 3

participantes = {}

for i in range(qtd_participantes):
    numero = int(input("Digite um número: "))
    nome = input("Digite um nome: ").upper()

    participantes[numero] = nome


print(participantes.get(44,"Não encontrado"))