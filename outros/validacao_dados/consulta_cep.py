import requests

class ConsultaCep:
    def __init__(self, cep):
        if self.validacep(cep):
            self.cep = cep
        else:
            raise ValueError("CEP Inválido!!!")
    def __str__(self):
        return self.formata_cep()

    def validacep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False
    
    def formata_cep(self):
        return "{}-{}".format(self.cep[0:5], self.cep[5:])
    
    def acessa_via_cep(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        #r.json retorna um dicionario de dados que pode ser acesso pela chave
        dados = r.json()
        return (
            dados['bairro'],
            dados['localidade'],
            dados['uf']
        )
