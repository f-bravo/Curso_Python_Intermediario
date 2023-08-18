# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo
import calendar

# print(calendar.calendar(2022))
print(calendar.month(2023, 8))

# monthrange: retorna o primeiro e o último dia do mês
numero_primeiro_dia, ultimo_dia = calendar.monthrange(2023,8)
print(list(enumerate(calendar.day_name)))

print(calendar.day_name[numero_primeiro_dia])
print(calendar.day_name[calendar.weekday(2023, 8, ultimo_dia)])

print(calendar.monthcalendar(2023, 8))

for week in calendar.monthcalendar(2023, 8):
    for day in week:
        if day == 0:
            continue
        print(day)

print('-----\n')

# -----------------------------------------------------------------------------


# Locale - internacionalização (tradução)

# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps
import calendar
import locale

# Mudar a localidade do programa:
# Para isso o sistema tem que da suporte.
# Usando a localização padrão do sistema operacional
# LC_ALL - muda tudo de uma vez. 
locale.setlocale(locale.LC_ALL, '')

print(calendar.calendar(2023))

print(locale.getlocale())  # ('pt_BR', 'cp1252')

# No terminal:
# -> Get-WinSystemLocale
# LCID             Name             DisplayName
# 1046             pt-BR            Português (Brasil)

print('-----\n')


# -----------------------------------------------------------------------------


# OS - módulo para interação com o sistema


# O módulo os para interação com o sistema
# Doc: https://docs.python.org/3/library/os.html
# O módulo `os` fornece funções para interagir com o sistema operacional.
# Por exemplo, o módulo os.path contém funções para trabalhar com caminhos de
# arquivos e a função os.listdir() pode ser usada para listar os arquivos em um
# diretório. O método os.system() permite executar comandos do sistema
# operacional a partir do seu código Python.
# Windows 11 (PowerShell), Linux, Mac = clear
# Windows (antigo, cmd) = cls
import os

# Para limpar o terminal:
os.system('cls')
os.system('echo "Hello world"')

print('a' * 80)
print('-----\n')


# -----------------------------------------------------------------------------


# os.path --> apenas manipula o caminho.
# os.path trabalha com caminhos em Windows, Linux e Mac
# Doc: https://docs.python.org/3/library/os.path.html#module-os.path
# os.path é um módulo que fornece funções para trabalhar com caminhos de
# arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças
# entre esses sistemas.

# Exemplos do os.path:
# os.path.join: junta strings em um único caminho. Desse modo,
# os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
# 'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e
# 'pasta1\pasta2\arquivo.txt' no Windows.

# os.path.split: divide um caminho uma tupla (diretório, arquivo).
# Por exemplo, os.path.split('/home/user/arquivo.txt')
# retornaria ('/home/user', 'arquivo.txt').

# os.path.exists: verifica se um caminho especificado existe.
# os.path só trabalha com caminhos de arquivos e não faz nenhuma
# operação de entrada/saída (I/O) com arquivos em si.
import os

caminho = os.path.join('Desktop', 'curso', 'arquivo.txt')
print(caminho) # Desktop\curso\arquivo.txt
print('-----')
diretorio, arquivo = os.path.split(caminho)
nome_arquivo, extensao_arquivo = os.path.splitext(caminho)
print(nome_arquivo, extensao_arquivo) # Desktop\curso\arquivo .txt

# digite: pwd - no terminal. Caminho da pasta atual do vscode
# Path
# C:\Python_intermediario

# Esse caminho existe? 
print(os.path.exists('C:\Python_intermediario'))  # True
print(os.path.exists('C:\Python_intermediario\Seção_6_Modulos')) # True

# Caminho absoluto
print(os.path.abspath('.'))  # C:\Python_intermediario
print('-----')
print(caminho)  # Desktop\curso\arquivo.txt
print(os.path.basename(caminho)) # arquivo.txt
print(os.path.basename(diretorio)) # curso - retorna apenas a parte final
print(os.path.dirname(caminho)) # Desktop\curso - nome do diretório
print('-----\n')


# ---------------------------------------------------------------------------


# os.listdir --> para listar e navegar em caminhos


# caminho_livros = 'C:\\Livros\Ti'
# print(caminho_livros)
import os
# C:\Livros\Ti
caminho_livros = os.path.join('C:\\Livros', 'Ti') # C:\Livros\Ti
print(caminho_livros)

for item in os.listdir(caminho_livros):
    print(item)

print('-----')
# não faz recursão em pastas internas. Só busca um nível.
# Se tiver muitas pastas internas a serem buscadas, use o walk
# Sò está mostrando o nome do arquivo e não os caminhos 

for pasta in os.listdir(caminho_livros):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)

    if not os.path.isdir(caminho_completo_pasta): # chega se a pasta é diretório
        continue

    for imagem in os.listdir(caminho_completo_pasta):
        print('  ', imagem)

caminho_interno = os.path.join('C:\Livros', 'Livros_ficticios', 'Pasta1_interna')
print(caminho_interno) # C:\Livros\Livros_ficticios\Pasta1_interna

for pasta in os.listdir(caminho_interno):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)

    if not os.path.isdir(caminho_completo_pasta): # chega se a pasta é diretório
        continue

    for imagem in os.listdir(caminho_completo_pasta):
        print('  ', imagem)


