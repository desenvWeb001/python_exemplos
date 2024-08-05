from collections import Counter

usuaios_data_science = {15,16,17,18}
usuario_machine_learn = {20,16,22,23}

assistiram = usuario_machine_learn.copy()
#extend copia elementos de uma lista obs não trata repetidos
#assistiram.extend(usuaios_data_science)

#criando conjunto
# o set transforma uma lista em um conjunto de dados
conj = set(assistiram)

print(type(conj))

#operador de ou para conjunto de dados é o |
print(usuaios_data_science | usuario_machine_learn)

#retornar os valor que estão presentoes nos dois conjuntos
print(usuaios_data_science & usuario_machine_learn)

#removendo que está no primeiro conjunto e não está no segundo conjuntos
print(usuaios_data_science - usuario_machine_learn)

#ou está em um ou está no outro
print(usuaios_data_science ^ usuario_machine_learn)


usuário = {1,2,3,4,5,6}

#adiciona
usuário.add(789)

#congela o conjunto para não permitir alterações
usuário = frozenset(usuário)

#dicionairio
conj_chv = {"Felipe": 10, "joyce":50}

#criando pelo contrutor
conj_chv2 = dict(Joao = 10, Mario = 100)


print(conj_chv["Felipe"])

#segundo parametro é adotado na função get quando não retorna nada
print(conj_chv.get("0","Não encontrado"))

conj_chv = {"Felipe": 10, "joyce":50}

#contador
x = Counter("conj_chv".split())

print("Contagem é :", x)

for elemento in conj_chv:
    print(elemento)

#lista dos valores
for elemento in conj_chv.values():
    print(elemento)

#lista dos valores retornoando por item
for elemento in conj_chv.items():
    print(elemento)

for elemento in conj_chv.keys():
    valor = conj_chv[elemento]
    print(elemento, valor)

#desenpacotar conjunto
for chave, valor in conj_chv.items():
    print(chave,"=", valor)

#busca pela chaves dados do conjunto 
print("Felipe" in conj_chv)

#deleta dados de um conjunto pela chave
del conj_chv["Felipe"]

print(conj_chv)




