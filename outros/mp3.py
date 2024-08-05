from pytube import YouTube
import moviepy.editor as mp
import re
import os

link = input("Digite uma do vídeo para fazer download em mp3: ")
#path = input("Digite o diretório que será salvo: ")
path = "c:\projetos"

yt = YouTube(link)

print("Baixando...")
ys = yt.streams.filter(only_audio=True).first().download(path)
print("Download concluido!!")


print("convertendo arquivo...")
for file in os.listdir(path):
    if re.search('mp4', file):
        mp4_path = os.path.join(path, file)
        mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)
print("terminado!!!") 

        




