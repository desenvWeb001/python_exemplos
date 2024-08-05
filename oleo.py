from datetime import date, timedelta, datetime
import sqlite3

class TrocaOleo:
        
    def __init__(self, data, km):
        self.data = data
        self.km = km

    def proxima_troca(self):
        previsao_prox_troca = 28
        data = datetime.strptime(self.data, "%d/%m/%Y") + timedelta(previsao_prox_troca)
        return data.strftime('%d/%m/%Y')

    def __str__(self):
        return 'Informações - Data da Troca: {} - KM da Troca: {} - Próxima Troca: {}'.format(self.data, self.km, self.proxima_troca())

data = input("Digite a data da troca de oleo: ")
km = input("Digite o KM data da troca de oleo: ")

trocaoleo = TrocaOleo(data,km)

con = sqlite3.connect("troca_oleo.db")
cur = con.cursor()

def sequencial_tabela():
    res = cur.execute("SELECT MAX(ID) FROM troca_oleo")
    for num in res:
        new = num
        return new[0] + 1
    

#cur.execute("CREATE TABLE troca_oleo(ID integer primary key AUTOINCREMENT, DATA_TROCA VARCHAR(30), KM_TROCA VARCHAR(30), PROXIMA_TROCA VARCHAR(30))")

cur.execute("""
    INSERT INTO troca_oleo VALUES
        ('{}','{}', '{}', '{}')
""".format(sequencial_tabela(),data,km,trocaoleo.proxima_troca()))

con.commit()
con.close()

print(trocaoleo)
