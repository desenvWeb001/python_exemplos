from abc import ABCMeta, abstractmethod
from operator import attrgetter

# [] lista 
# () tuplas
# {} conjuntos

idades = [20,35]

# idades.append("Jose")
# idades.remove(20)
# posição, valor
#dades.insert(2, "Guanabara")

idades_ano_seguinte = []

def proximo_ano(idade):
    return idade + 1

# list comprehesion aplicando filtros e transformações na lista
# [proximo_ano(idade) for idade in idades if idade > 20]

for idade in idades:
    idades_ano_seguinte.append(idade + 1)

#print(idades)
#print(idades_ano_seguinte)

#transformando classe em abstrata 
class Conta(metaclass=ABCMeta):
   
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    #força todas as classes filhas de conta a implmentar esse metodo
    @abstractmethod
    def extrato(self):
        return self.saldo

    #quando precisar comparar um objeto com o outro se é do mesmo tupo
    def __eq__(self, outro):
        if type(outro) != ContaCorrente:
            return False
        return self.codigo == outro.codigo and self.saldo == outro.saldo

    # retorna uma representação da classe em forma de string
    def __str__(self):
        return ">> Código: {} Saldo: {} <<".format(self.codigo, self.saldo)

    # nome personalizado verificando se uma conta é menor que outro com base no saldo
    def __lt__ (self, outro):
        if self.saldo != outro.saldo:
            return self.saldo < outro.saldo
        
        return self.codigo < outro.codigo

class ContaCorrente(Conta):
    def extrato(self):
        return self.saldo and self.codigo

#implmenta operações de ordenação baseada em criteiros de igualdade 
from functools import total_ordering
@total_ordering
class ContaPoupanca(Conta):
    def extrato(self):
        return self.saldo

conta1 = ContaCorrente(1050)
conta1.deposita(500)

conta2 = ContaPoupanca(10)
conta2.deposita(500)

#verifica se um objeto é de uma intancia do tipo tal, verifica se é do mesmo tipo da classe m]ae
if isinstance(ContaCorrente(1050), Conta):
    print("Instancia correta")
else:
    print("Instancia incorreta")

#comparação de objetos iteraveis é feita pelo metodo __eq__ que pode ser implementado
#print(conta1 > conta2)

contas =[conta1, conta2]

#iordenando lista com base num atributo sem precisar criar um função na classe
for conta in sorted(contas, key=attrgetter("saldo", "codigo")):
    print(conta)

# imprimindo posição e valor da lista
idade = [10,11,12,13,45,12]

for i in range(len(idade)):
    print("Posição: {} Idade: {}".format(i, idade[i]))

#transformando numa lista as posições da lista idade
print(list(range(len(idade))))

#retorna duplas de dados
for i in enumerate(idade):
    print(i)

#desenpacotando valores de uma lista

usuarios = [
    ("Felipe", 27, 1995),
    ("Joyce", 26, 1996),
    ("Ana", 8, 2014)
]

#desenpacotando lista
for nome, idade, nascimento in usuarios:
    #print(nome)
    pass


nomes = []
#desaconsiderando posições da lista
for nome, _, _ in usuarios:
    nomes.append(nome)
print(nomes[2])

# imprimindo em ordem decrescente

idade = [10,11,12,13,45,12]

print(sorted(idade, reverse=True))

##print(contas[1])
        


