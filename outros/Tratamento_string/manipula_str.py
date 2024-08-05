url = "bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"

#url = ' '

# sanitização da urç

#remove espaçoes vazios de uma string
#texto.strip(), texto.lstrip(), texto.rstrip()
url = url.replace(' ', '')

# validação de url

if url == '':
    raise ValueError('A url está vazia')


indice_terrogacao = url.find('?')
# fatiamento de string
url_base = url[0:indice_terrogacao]

url_parametros = url[indice_terrogacao + 1:]

parametro_busca = 'quantidade'
# find retorna a indice de uma string
indice_parametro = url.find(parametro_busca)

indice_valor = indice_parametro + len(parametro_busca) + 1
# find quando não acha o valor retorna -1, segundo parametro posição de busca
indice_e_comercial = url.find('&', indice_valor)

if indice_e_comercial == -1:
    valor = url[indice_valor:]
else:
    valor = url[indice_valor: indice_e_comercial]

print(valor)



