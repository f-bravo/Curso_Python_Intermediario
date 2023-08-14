# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime, timedelta

data_str_data = '2023/08/14 13:30:00'
data_str_data2 = '14/08/2023'
data_str_fmt = '%Y/%m/%d %H:%M:%S'


data1 = datetime(2023, 8, 13, 13, 35, 00)

# strptime(Data e formato) 
data2 = datetime.strptime(data_str_data, data_str_fmt)
print(data1)
print(data2)
print('-----\n')

data3 = datetime.now()
print(data3)

from pytz import timezone
# Para colocar time zone diferentes: instalar pytz
# pip install pytz types-pytz
data4 = datetime.now(timezone('Asia/Shanghai'))
print(data4)
print('-----\n')

# Unix timestamp - contagem de 01/01/1970 até hoje
data_hoje = datetime.now()
print(data_hoje.timestamp())
print('-----\n')

# from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('05/11/1982 05:30:00', fmt)
data_fim = datetime.strptime('14/08/2023 14:20:00', fmt)
print(data_fim - data_inicio)

delta = data_fim - data_inicio
print(delta.days)
print(delta.total_seconds())

# Time delta é a diferença entre duas datas 
delta2 = timedelta(days=300) 
print(data_fim + delta2) # 2024-06-09 14:20:00
print('-----\n')

# pip install python-dateutil types-python-dateutil
from dateutil.relativedelta import relativedelta
print(data_fim + relativedelta(months=10)) # 2024-06-14 14:20:00
# 10 meses para o meio do ano que vem

delta3 = relativedelta(data_fim, data_inicio)
print(delta3)
# relativedelta(years=+40, months=+9, days=+9, hours=+8, minutes=+50)
print('-----\n')

# Formatar datas é a mesma coisa que criar datas. Só muda uma letra

# Para criar datas usa o strptime
# Para formatar datas

data_new = datetime.strptime('2023-08-15 08:30:00', '%Y-%m-%d %H:%M:%S')
print(data_new)
formato = '%d/%m/%Y'
print(data_new.strftime(formato))
print(data_new.strftime('%d/%m/%Y %H:%M:%S'))
print(data_new.strftime('%d/%m/%Y %H:%M'))
print(data_new.strftime('%Y'))
# Formato é sempre string - para pegar valor int use .year, .day:
print(data_new.strftime('%Y'), data_new.year)
print(data_new.strftime('%Y'), data_new.day)


# Exercício: calcul as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela


valor_total = 1_000_000
data_emprestimo = datetime(2023, 8, 10)
delta_anos = relativedelta(years=5)
data_final = data_emprestimo + delta_anos

data_parcelas = []
data_parcela = data_emprestimo
while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)

numero_parcelas = len(data_parcelas)
valor_parcela = valor_total / numero_parcelas

for data in data_parcelas:
    print(data.strftime('%d/%m/%Y'), f'R$ {valor_parcela:,.2f}')

print()
print(
    f'Você pegou R$ {valor_total:,.2f} para pagar '
    f'em {delta_anos.years} anos '
    f'({numero_parcelas} meses) em parcelas de '
    f'R$ {valor_parcela:,.2f}.'
)
