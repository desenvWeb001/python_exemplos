from datetime import datetime, timedelta

class DatasBr:

    def __init__(self):
        self.data_cadastro = datetime.today()

    def __str__(self):
        return self.data_formatada()

    def meses_do_ano(self):
        meses = [
            "janeiro", "fevereiro", "março", "abril",
            "maio", "junho", "julho", "agosto",
            "setembro", "outubro", "novembro", "dezemrbo"
        ]
        mes_cadastro = self.data_cadastro.month -1
        return meses[mes_cadastro]
        
    def dias_da_semana(self):
        dias = [
            "segunda", "terça", "quarta",
            "quinta", "sexta", "sábado",
            "domingo"
        ]
        dia_cadastro = self.data_cadastro.weekday()
        return dias[dia_cadastro]
    
    def data_formatada(self):
        data_formatada = self.data_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada
    
    def tempo_cadastro(self):
        tempo_cadastrado = (datetime.today() + timedelta(days=30))- self.data_cadastro
        return tempo_cadastrado
    
