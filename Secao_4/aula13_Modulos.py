# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html

# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo (sys)-> é o nome do módulo
# Desvantagens: nomes grandes
import sys

print(sys.platform)



# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo - cuidado p não sobrescrever os nomes
from sys import exit, platform

print(platform) # não precisa do name_space sys.

# alias 1 - import nome_modulo as apelido
# Use a comunidade Python tem o costume de renomear ok. Se não, não faça.
import sys as s

# sys = 'alguma coisa'
print(s.platform)
# print(sys)


# alias 2 - from nome_modulo import objeto as apelido
# from sys import exit as ex
from sys import platform as pf
print(pf)

# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# Má prática - 
from sys import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo com seus nomes
# from sys import exit, platform

print(platform)
# exit()
print()

print('\n# Modularização\n')
# Modularização - Entendendo os seus próprios módulos Python.

# A separação da aulas da seção 4 está organizada em módulos, aulas por temas.
# A seção 4 é um package. Um pacote para separa a seção 4.
# O primeiro módulo executado chama-se __main__
print('Nome desse módulo:', __name__)
# Você pode importar outro módulo inteiro ou parte do módulo.

# Importando o módulo inteiro - aula01_Funcao.py
import aula01_Funcao

# O python conhece a pasta onde o __main__ está e as pastas abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por padrão
# O python conhece todos os módulos e pacotes presentes nos caminhos de sys.path

print(*sys.path, sep='\n')
# Primeiro busca no arquivo onde o main está que é a pasta raiz onde está o curso.
# depois busca nas bibliotecas
# Depois busca no ambiente virtual 

# O padrão é:
"""
O main é o ponto de entrada do programa.
Você sabe qual é o arquivo de entrada quando cria uma aplicação. 
Você cria o sistema envolta do main.
Cria os pacotes onde está o main e cria arquivos p frente do main
"""
print()


print('\n# \n')
# import aula01_Funcao
# Ao importar o módulo aula01_Funcao, importa tudo que tem dentro dele.

# Se quiser importar apenas uma função do módulo
print('\n# Importanto apenas a função soma:\n')
from aula01_Funcao import soma2
soma2(10,10,10)

# para importar pacotes ou módulos para trás, fora da hierarquia, precisa
# manupular o sys.path.

# Todo módulo é um singleton - import único
# O import é salvo na memória - toda vez que precisar usar o módulo não precisa
# importar novamente. Nos códigos acima existe import repetidos apenas para fins 
# didático. E os imports sempre ficam na parte superior do arquivo.
