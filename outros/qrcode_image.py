import qrcode
import os
import string
import random

link = input('Digite o link do QRCODE: ')

imagem = qrcode.make(link)

#gera string aleatória
def gerador_nome_imagem(size=6, chars=string.ascii_lowercase):
    return ''.join(random.choice(chars) for _ in range(size))

id_img = gerador_nome_imagem()

imagem.save("{}{}.jpg".format('image-',id_img))

#retorna repositório atual
print('Imagem salva no firetório: ',os.getcwd())
