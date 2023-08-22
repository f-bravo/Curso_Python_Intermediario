# -----------------------------------------------------------------------------
# Usando calendar para calendários e datas
# -----------------------------------------------------------------------------


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
# -----------------------------------------------------------------------------


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
# -----------------------------------------------------------------------------


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
# -----------------------------------------------------------------------------


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
# ---------------------------------------------------------------------------


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
# Se tiver muitas pastas internas a serem buscadas, use o os.walk
# Só está mostrando o nome do arquivo e não os caminhos 

for pasta in os.listdir(caminho_livros):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)

    if not os.path.isdir(caminho_completo_pasta): # checa se a pasta é diretório
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

print('----------\n')


# -----------------------------------------------------------------------------
# os.walk --> para navegar em caminhos de forma recursiva
# -----------------------------------------------------------------------------


# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
import os
from itertools import count


caminho_walk = os.path.join("/C:", os.sep, "Teste_Python")

cont = count()

for root, dirs, files in os.walk(caminho_walk):
    print(files)

print('-----00I00-----')

for root, dirs, files in os.walk(caminho_walk):
    the_counter = next(cont)
    print(the_counter, root)

print('################################\n')
cont2 = count()

for root, dirs, files in os.walk(caminho_walk):
    the_counter = next(cont2)
    print(the_counter, "Pasta atual", root)

    for dir_ in dirs:
        print("  ", the_counter, "Dir", dir_)


print('=================#================\n')
cont3 = count()

for root, dirs, files in os.walk(caminho_walk):
    the_counter = next(cont3)
    print(the_counter, "Pasta atual", root)

    for dir_ in dirs:
        print("  ", the_counter, "Dir", dir_)

    for file_ in files:
        print("  ", the_counter, "FILE", file_)



# -----------------------------------------------------------------------------


# os.path.getsize e os.stat para dados dos arquivos (tamanho em bytes)

import math
import os
from itertools import count


# https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python

def formata_tamanho(tamanho_em_bytes: int, base: int = 1000) -> str:
    """Formata um tamanho, de bytes para o tamanho apropriado"""
    if tamanho_em_bytes <= 0:
        return "0B"

    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"
    # math.log vai retornar o logaritmo do tamanho_em_bytes
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))
    # Por quanto nosso tamanho deve ser dividido para gerar o tamanho correto.
    potencia = base ** indice_abreviacao_tamanhos
    # Nosso tamanho final
    tamanho_final = tamanho_em_bytes / potencia
    # A abreviação que queremos
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final:.2f} {abreviacao_tamanho}'

count4 = count()

for root, dirs, files in os.walk(caminho_walk):
    the_counter = next(count4)
    print(the_counter, 'Pasta atual', root)

    for dir_ in dirs:
        print('  ', the_counter, 'Dir:', dir_)

    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        # tamanho = os.path.getsize(caminho_completo_arquivo)
        stats = os.stat(caminho_completo_arquivo)
        tamanho = stats.st_size
        print('  ', the_counter, 'FILE:', file_, formata_tamanho(tamanho))

print('----------\n')        


# ------------------------------------------------------------------------------
# os + shutil - Copiando arquivos e criando pastas com Python
# ------------------------------------------------------------------------------


caminho_walk = os.path.join("/C:", os.sep, "Teste_Python")

# os + shutil - Mover copiar e apagar arquivos
# Mover/Renomear -> shutil.move
# Mover/Renomear -> os.rename
# Copiar -> shutil.copy
# Apagar os.unlink
# Apagar diretórios recursivamente -> shutil.rmtree

import shutil

HOME = os.path.expanduser("~")
print(HOME)  # C:\Users\bravo
DESKTOP = os.path.join(HOME, "Desktop")
print(DESKTOP)  # C:\Users\bravo\Desktop

# 1 - copiar arquivos de uma pasta para outra
PASTA_ORIGINAL = os.path.join(DESKTOP, "Python_teste")
print(PASTA_ORIGINAL)  # C:\Users\bravo\Desktop\pasta_teste

NOVA_PASTA = os.path.join(DESKTOP, "NOVA_PASTA")
print(NOVA_PASTA)  # C:\Users\bravo\Desktop\NOVA_PASTA

# Criando uma nova pasta - o Python n faz isso sozinho
os.makedirs(NOVA_PASTA, exist_ok=True)  # Se a pasta já exitir n dará erro
# replace substitui um valor por outro numa string

for root, dirs, files in os.walk(PASTA_ORIGINAL):
    for dir_ in dirs:
        caminho_novo_diretorio = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
        )
        os.makedirs(caminho_novo_diretorio, exist_ok=True)

    for file in files:
        caminho_arquivo = os.path.join(root, file)
        caminho_novo_arquivo = os.path.join(
            root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
        )
        shutil.copy(caminho_arquivo, caminho_novo_arquivo)

        print(caminho_novo_arquivo)  # C:\Users\bravo\Desktop\NOVA_PASTA


# -----------------------------------------------------------------------------
# Aula 287 - os + shutil - Apagando, copiando, movendo e renomeando pastas
# -----------------------------------------------------------------------------


# O código acima era mais uma lógica para entender como funciona
# Mas é muito mais dinâmico podendo fazer qualquer coisa quando estiver copiando
# Ex: poderia mudar a extenção, converter p outro formato, etc.
# Existe uma forma muito mais fácil de fazer... com o copytree

# Vamos copiar arquivos de uma pasta para outra
# Copiar -> shutil.copy
# copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move os os.rename - use o shutil.move da menos erros


# Copiando de uma pasta para outra:
# Só precisa da onde ta a pasta original e para onde a nova pasta vai ser criada
# Só precisa dos caminhos

shutil.rmtree(NOVA_PASTA, ignore_errors=True)
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)

# Ao executar o comando acima, a pasta já existe e gera um erro
# Para funcionar tem que apagar a pasta por recursão usando o comando:
# shutil.rmtree(NOVA_PASTA)
# Se existir algo dentro da pasta ou subpastas, tem que apagar por recursão
# Primeiro tem que apagar todos os arquivos dentro de cada pasta, apagar todas
# as subpastas e depois apagar a pasta original
# para n ter erro use ignore_errors=True

# Para mover/renomear
# shutil.move(NOVA_PASTA, NOVA_PASTA + 'novo_nome/caminho')



