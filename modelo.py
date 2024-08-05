
class Programa:
    
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes +=1

    def likes(self):
        return self._likes


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    #representação textal de uma classe
    def __str__(self):
        return f'{self.nome} - {self.ano} - {self._likes}'

    
#herdando atributos e metodos da classe generica programa
class Filme (Programa):
    
    def __init__(self, nome, ano, duracao):
        #chmando o inicializador da classe mãe
        super().__init__(nome, ano)
        self.duracao = duracao
    
    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.duracao} - {self._likes}'
    
    def retorna_artistas(self):
        lista = ("Felipe", "Joyce", "Ana Clara")
        return lista

class Serie (Programa):
    
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.temporadas} - {self._likes}'

#herdando da classe list,a classe herda as caracteristicas e comportamentos de uma lista
#a classe tera caracteristicas da própria classe como nome e caracteristicas de lista para o objeto programa
class Playlist ():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    # torna uma classe iteravel recebe um item e repassa para lista interna
    def __getitem__(self, item):
        return self._programas[item]

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)

    #para poder usar o len fora da classe para o iteravel
    #def __len__(self):
        #return len(self._programas)

##########################################################################################


vingadores = Filme("vingadores", 2019, 150)
atlanta = Serie("atlanta", 2020, 10)
sobrenatural = Serie("sobrenatura", 2005, 15)
arqueiro = Serie("sobrenatura", 2012, 8)

sobrenatural.dar_like()
vingadores.dar_like()
atlanta.dar_like()
arqueiro.dar_like()

#print(filme.nome)
#print(filme.retorna_artistas())

filmes_e_series = [vingadores, atlanta, arqueiro, sobrenatural]

playlist = Playlist('final de semana', filmes_e_series)

print('Nome Playlist:', playlist.nome,'Tamanho:', playlist.tamanho)

for programa in playlist:
    print(programa)
    #detalhe = programa.duracao if hasattr(programa, 'duracao') else programa.temporadas
    #print(" Nome: {} Ducaração/Temporada: {} Likes: {}".format(programa.nome, detalhe, programa.likes()))
