import re

class TelefonesBr:
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numeto = telefone
        else:
            raise ValueError("Numero inválido")
        
    def __str__(self):
        return self.formata_numero()

    def valida_telefone(self, telefone):
        padrao2 = "([0-9]{3})?([0-9]{4,5})([0-9]{4})"
        resposta2 = re.search(padrao2, telefone)
        if resposta2:
            return True
        else:
            return False
        
    def formata_numero(self):
        padrao2 = "([0-9]{2})?([0-9]{3})([0-9]{4,5})([0-9]{4})"
        resposta2 = re.search(padrao2, self.numeto)
        return "+{} {} {}-{}".format(resposta2.group(1), resposta2.group(2), resposta2.group(3), resposta2.group(4))


        
    