from conta import Conta

# teste classe OO

def cria_conta(numero, titular, saldo, limite):
    #conjunto de dados
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def deposita(conta, valor):
    conta["saldo"] += valor     

def saca(conta, valor):
    conta["saldo"] -= valor 

def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))

cria_conta(1,"Felipe", 100, 10000)

# variavel de objeto da classe contém a referencia da classe 
#conta = Conta(123,'felipe',1000, 1000)
#conta2 = Conta(123,'Joyce',55.0, 1000)

#print(Conta.codigo_banco())

a = 3
a = 33
print(a==a)
