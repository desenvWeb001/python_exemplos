
class Conta:

    # paradigma orientado a objeto
        
    #contrutor da classe
    def __init__(self,numero, titular, saldo, limite):
        print('contruindo objeto... {}'.format(self))
        #__ dois andescor deixa o atributo privado - modificador de acesso
        self.__numero = numero
        self.__titula = titular
        self.__saldo = saldo
        self.__limite = limite


    def extrato(self):
        print('Saldo de {} do titular {}'.format(self.__saldo, self.__titula))

    def deposita(self, valor):
        self.__saldo += valor
    
    # deixando metodo privado
    def __verifica_saque(self,valor):
        disponivel_saque = self.__saldo + self.__limite
        return valor <= disponivel_saque

    def saca(self, valor):
        if(self.__verifica_saque(valor)):
            self.__saldo -= valor
            print ("sacou {}".format(valor))
        else:
            print ("Saldo indisponivel")
    
    def transferir(self, valor, origem,destino):
        origem.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    #metodo com acesso as propriedades nesses casos na passagem de valores não precisa usar as ()
    #automaticamente o python identificara se a operação e um get ou set
    @property
    def limite(self):
        print("Chamando o @property limite()")
        return self.__limite
   
    @limite.setter
    def limite(self, novolimite):
        print("Chamando o setter limite()")
        self.__limite = novolimite

    #metodo estatico
    @staticmethod
    def codigo_banco():
        return "001" #{"BB": "001", "CAIXA":"002"}

    def get_limite(self):
        return self.__limite
        
    def set_limite(self, novo_limite):
        self.__limite = novo_limite

