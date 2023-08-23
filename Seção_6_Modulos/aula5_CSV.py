# CSV (Comma Separated Values - Valores separados por vírgulas)
# É um formato de arquivo que armazena dados em forma de tabela, onde cada
# linha representa uma linha da tabela e as colunas são separadas por vírgulas.
# Ele é amplamente utilizado para transferir dados entre sistemas de diferentes
# plataformas, como por exemplo, para importar ou exportar dados para uma
# planilha (Google Sheets, Excel, LibreOffice Calc) ou para uma base de dados.
# Um arquivo CSV geralmente tem a extensão ".csv" e pode ser aberto em um
# editor de texto ou em uma planilha eletrônica.
# Um exemplo de um arquivo CSV pode ser:
# Nome,Idade,Endereço
# Felipe Bravo,40 ,"Av Brasil, 21, Centro"
# João bravo,45,"Rua 22, 44, Nova Era"
# A primeira linha do arquivo define os nomes das colunas, enquanto as
# linhas seguintes contêm os valores das linhas, separados por vírgulas.
# Regras simples do CSV
# 1 - Separe os valores das colunas com um delimitador único (,)
# 2 - Cada registro deve estar em uma linha
# 3 - Não deixar linhas ou espaços sobrando
# 4 - Use o caractere de escape (") quando o delimitador aparecer no valor.
import csv
from pathlib import Path

CAMINHYO_CSV = Path(__file__).parent / 'aula5_CSV.csv'
print(CAMINHYO_CSV) # c:\Python_intermediario\Seção_6_Modulos\aula5_CSV.csv

# Para leitura CSV:

# formato de ler com reader() retorna uma lista - usa FOR e next
with open(CAMINHYO_CSV, 'r', encoding='utf8') as arquivo:
    leitor = csv.reader(arquivo)

    for linha in leitor:
        print(linha)

# ['Nome', 'Idade', 'Endereço']
# ['Felipe Bravo', '40 ', 'Av Brasil, 21, Centro']
# ['João bravo', '45', 'Rua 22, 44, Nova Era']


print( '----------')
# Para pegar valro por valor é melhor DictReader() retorna um dict
with open(CAMINHYO_CSV, 'r', encoding='utf8') as arquivo:
    leitor = csv.DictReader(arquivo)
    
    for linha in leitor:
        print(linha)
        # print(linha['Nome'], linha['Idade'])

# {'Nome': 'Felipe Bravo', 'Idade': '40 ', 'Endereço': 'Av Brasil, 21, Centro'}
# {'Nome': 'João bravo', 'Idade': '45', 'Endereço': 'Rua 22, 44, Nova Era'}

print('----------\n')

# Para escrever CSV:
# Usei o mesmo arquivo. Vai escrever por cima do csv anterior.

CAMINHYO_CSV2 = Path(__file__).parent / 'aula5_CSV.csv'

lista_clientes = [
    {'Nome': 'Luiz Felipe', 'Endereço': 'Av BR, 233'},
    {'Nome': 'João Bravo', 'Endereço': 'Rua. 27, "3"'},
    {'Nome': 'Miriam Leila', 'Endereço': 'Av Ame, 55'},
]

with open(CAMINHYO_CSV2, 'w', encoding='utf8') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    # nova_colunas = ['Nome','Endereco'] igual a linha de cima
    escrita = csv.writer(arquivo)
    escrita.writerow(nome_colunas)

    for cliente in lista_clientes:
        escrita.writerow(cliente.values())

# Uma lista de lista:
# Escreve linha por linha. A linha é separada por vírgula
# lista_clientes = [
#     ['Luiz Felipe', 'Av BR, 233'],
#     ['João Bravo', 'Rua. 27, "3"'],
#     ['Miriam Leila', 'Av Ame, 55'],
# ]
with open(CAMINHYO_CSV2, 'w', encoding='utf8') as arquivo:
    nome_colunas = ['Nome','Endereco'] # igual a linha de cima
    escrita = csv.writer(arquivo)
    escrita.writerow(nome_colunas)

    for cliente in lista_clientes:
        escrita.writerow(cliente)

# Se for um dicionário:
# Escreve o arquivo com os fields_names (nome, endereco)
# Escreve o cabeçalho com writeheader e jgoa o dicionário dentro do csv.
"""
with open(CAMINHYO_CSV2, 'w', encoding='utf8') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escrita = csv.DictReader(
        arquivo,
        fieldnames=nome_colunas     
    )
    escrita.writeheader(nome_colunas) # para o cabeçalho

    for cliente in lista_clientes:
        escrita.writerow(cliente)
"""
