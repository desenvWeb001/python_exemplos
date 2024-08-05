
otimista = int(input("Digita em Dias a estimativa otimista :"))

pessimista = int(input("Digita em Dias a estimativa pessimista :"))

mais_provavel = int(input("Digita em Dias a estimativa mais_provavel :"))

estimativa_dias = (otimista / (4 * mais_provavel) + pessimista) / 6

print("A estimativa em dias é :", estimativa_dias)