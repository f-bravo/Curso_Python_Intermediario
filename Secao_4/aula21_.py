# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - São úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120

def recursiva(inicio=0, fim=4):

    print(inicio, fim)

    # Caso base
    if inicio >= fim:
        return fim

    # Caso recursivo
    # contar até chegar ao final
    inicio += 1
    return recursiva(inicio, fim)


print(recursiva(0, 10)) # com 1mil:  996 1000
print()
# Toda vez que usa função recursiva o escopo inteiro é salvo na call stack.
# Por isso só conseguiu chegar até 996. O limite de recursão do Python é 1000. 

# Número fatorial:
print('Fatorial:\n')
def fatorial(n):
    if n <= 1:
        return 1
    
    return n * fatorial(n -1)

print(fatorial(5))
print(fatorial(10)) # 3628800


# -------------------------------------------------------------------


# Ambientes virtuais - é como uma pasta com toda a instalação e bibliotecas
# de terceiros. 
# Caso não use ambiente virtual tudo será instalado no Python global

# O mais importante de usar ambiente virtual é que forma uma bolha, uma espécie 
# de proteção com tds as versões usadas. 
# Suponha que um cliente que vc fez um app para ele. Agora vc precisa da 
# manutenção. Vc vai precisar das versões exatas de quando o app foi feito.
# COm o ambiente virtual isso é feito de maneira muito simples.
# Cada projeto ficará em um ambiente virtual

# Ambientes virtuais em Python (venv)
# Um ambiente virtual carrega toda a sua instalação
# do Python para uma pasta no caminho escolhido.
# Ao ativar um ambiente virtual, a instalação do
# ambiente virtual será usada.
# venv é o módulo que vamos usar para
# criar ambientes virtuais.
# Você pode dar o nome que preferir para um
# ambiente virtual, mas os mais comuns são:
# venv env .venv .env

# No windows: primeiro precisa modificar no power shell a politica e execução
# para irrestrito. 

# para criar o ambiente virtual:
# -> python -m venv nome_do_ambiente(venv)

# O nome do ambiente geralmente é venv

# Para ativar o ambiente virtual:
# -> . venv/Scripts/Activate

# Para desativar:
# -> deactivate


# -------------------------------------------------------------------


# PIP - instalando pacotes e bibliotecas:


# PIP é um instalador de pacotes que não vem junto com o Python.

# Geralmente no Windows para instalar use o comando:
# -> python -m pip install nome_da_biblioteca

# Para atualizar coloque o --upgrade no final
# pip install nome_da_biblioteca --upgrade

# Para desinstalar:
# -> pip uninstall nome_da_bilbioteca 

# Para visualizar versões das bibliotecas:
# -> pip index versions nome_da_biblioteca

#Para instalar versões específicas coloque ==número_da_versão:
# -> pip install nome_da_biblioteca==2.0.3

# REQUIREMENTS.txt - são requerimentos para determinado ambiente virtual funcionar
# é um arquivo que contém todos os pacotes e suas versões para reinstalar em
# outro ambiente virtual.
# Digite o comando abaixo para gerar o arquivo requirements.txt 
# -> pip freeze > requirements.txt
# Esse arquivo contém o que vem do pip freeze

# Recriando ambiente virtual com o requirements.txt:
# Com o ambiente virtual ativo digite:
# pip install -r .\requiremets.txt

# Agora dê um pip freeze para ver todos os pacotes instalados.

# A cada novo pacote instalado precisa rodar o comando para atualizar o arquivo
# requerimets.txt 
# # -> pip freeze > requiremets.txt 

# OBS tuda biblioteca que estiver instalada na versão global do Python será a
# versão final. Caso tenha uma instalada na global e precise de uma versão 
# específica não irá conseguir atualizar enquanto a versão global estiver instalada
 