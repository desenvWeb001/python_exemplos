from Cpf_cnpj import Documento
from telefonesBr import TelefonesBr
from datas_br import DatasBr
from consulta_cep import ConsultaCep
from datetime import datetime, timedelta
import re
import requests
#from validate_docbr import CPF, CNPJ

cpf = "11782914480"
cnpj = "44444582000170"

cpf_valido = Documento.cria_documento(cnpj)

#cpf_valido2 = CPF()
#cnpj_valido = CNPJ()

#print(cpf_valido)
#print(cpf_valido2.validate(cpf_valido.formata_cpf()))

#print(cnpj_valido.validate(cnpj,))

padrao = "\w{0,50}.{0,1}\w{0,50}@\w{3,10}.\w{2,3}.\w{2,3}"
texto = "1wwwwwwwwwwwwwww felipe.gm001@gmail.com.br eeeeeeeeeeeeeeeeeeeeeeeee"
resposta = re.search(padrao, texto)
#print(resposta.group())

padrao2 = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
texto2 = "meu numero é 83986937673"
resposta2 = re.search(padrao2, texto2)
#print(resposta2.group())

telefone = "55083986937673"

telefone_obj = TelefonesBr(telefone)
#print(telefone_obj)

datasbr = DatasBr()

#print(datasbr.tempo_cadastro())
cep = "58303360"

objeto_cep = ConsultaCep(cep)

#desempacotando de tupla
bairro, localidade, uf = objeto_cep.acessa_via_cep()

print(bairro, localidade, uf)

