from datetime import date, timedelta

def date_sys():
    data_atual = date.today()
    data_sys = data_atual.strftime('%d/%m/%y')
    return data_sys

def data_fim():
    vigencia = timedelta(365)
    soma_atual_vigencia = date.today() + vigencia
    dtfim = soma_atual_vigencia.strftime('%d/%m/%y')
    return dtfim

print(date_sys())