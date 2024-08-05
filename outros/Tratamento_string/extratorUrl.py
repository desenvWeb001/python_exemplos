import re

class ExtratorUrl:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if self.url == '':
            raise ValueError('A url está vazia')

        # o caracter ? indica que a expressão pode estar ou não na string () busca o texto exato [] busca os caracteres dentro as colchetes
        padrao = re.compile('(http(s)?://)?(www.)?bytebank.com(br)?/cambio')
        # match função que verifica se a url está no padrã da que foi passada em parametro
        matchh = padrao.match(self.url)

        if not matchh:
            raise ValueError('Url é inválida')

    def get_url_base(self):
        indice_terrogacao = self.url.find('?')
        url_base = self.url[0:indice_terrogacao]
        return url_base

    def get_url_parametro(self):
        indice_terrogacao = self.url.find('?')
        url_parametros = self.url[indice_terrogacao +1:]
        return url_parametros

    def get_valor_parametros(self, parametro_busca):
        # find retorna a indice de uma string
        indice_parametro = self.get_url_parametro().find(parametro_busca)

        indice_valor = indice_parametro + len(parametro_busca) + 1
        # find quando não acha o valor retorna -1, segundo parametro posição de busca
        indice_e_comercial = self.get_url_parametro().find('&', indice_valor)

        if indice_e_comercial == -1:
            valor = self.get_url_parametro()[indice_valor:]
        else:
            valor = self.get_url_parametro()[indice_valor: indice_e_comercial]

        return valor

    def __len__(self):
        return len(self.url)
        
extrator = ExtratorUrl("bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real")

print('O tamanho da URL é: {} caracters'.format(len(extrator)))

valor = extrator.get_valor_parametros('quantidade')

print(valor)