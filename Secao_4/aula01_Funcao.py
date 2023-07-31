# Cusro Python intermediário:
"""
Na seção 4 vamos ver os seguintes tópicos:
Funções, dicionários, módulos, programação funcional, etc.
"""

print('Seção 4 do curso Python intermediário')

"""
Parâmetro vs Argumento: é mais acadêmico.
Parâmetro: é o nome da variável usado na definição da função
Argumento: é o valor preenchido nos parâmetros ao chamar a função
"""

# Introdução a funções:
# Função por padrão retorna none
# após nomear um parâmetro todos que vierem depois vão precisar ser nomeados

def saudacao(nome='sem nome'):
    print(f'Olá, {nome}!')

saudacao('Bravo')
# Olá, Bravo!
saudacao()
# Olá, sem nome!

# Argumentos nomeados e posicional:
# Arguneto nomeado nome='sem nome'
# Argumento posicional: veja o exemplo abaixo
# x é o primeiro e y é o segundo - existe uma ordem

def soma(x, y):
    # print(x + y)
    print(f'{x=} {y=}. Total =',x + y) 

soma(1, 2) # x=1 y=2. Total = 3
# Usando argumentos nomeados: veja que o resultado é o mesmo.
soma(y=2, x=1)  # x=1 y=2. Total = 3


# Passando valor padrão no parâmetro
# Em função é comum passar um valor como um não valor
# Se por acaso precisar de introduzir mais um parâmetro no exemplo acima?
# O código quebra.

def soma2(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=}. Total =',x+y+z) 
    else:
        print(f'{x=} {y=} Total', x + y)    


soma2(5, 10) # x=5 y=10 Total 15
soma2(5, 10, 15) # x=5 y=10 z=15. Total = 30

# Repare: 
# Z sendo ou não enviado o código não quebra. Ao não enviar Z ele usa None

print('----------------------------------------------------------')
print('Importando a aula01 de funções para a aula13 como exemplo.')
print('Esse módulo se chama:', __name__)


# Toda vez que passa um parâmetro para a função e ele é mutável como uma lista
# o Python vai reutilizar a lista.
# Para ter uma lista nova toda vez?
# A mais simples é criar uma lista fora da função.

# Mas a melhor forma de resolver isso é não usar parâmetros mutáveis na função

# Coloque o parâmetro como None - faça um if para chegar se for None cria uma lista
# Toda vez que chamar a função sem passar o parâmetro lista=[] será criada uma nova lista


def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista= []
    lista.append(nome)
    return lista

# lista1 = [] -> não é mais necessário

cliente1 = adiciona_clientes('luiz')
adiciona_clientes('Juju', cliente1)
print(cliente1)

cliente2 = adiciona_clientes('Felipe')
adiciona_clientes('Eduarda', cliente2)
print(cliente2)

# Toda vez que for criar um parâmetro tem que checar se é mutável
# Se for mutável, não coloca valor padrão na função, coloque None.
# Se ninguém enviar, dentro da função cria o parâmetro
# Se colocar um parâmetro mutável ele será sempre o mesmo para toda
# as vezes que chamar a função


# ------------------------------------------------------------------


# Controlando a quantidade de argumentos posicionais e nomeados em funções
# *args (ilimitado de argumentos posicionais)
# **kwargs (ilimitado de argumentos nomeados)
# Positional-only Parameters (/) - Tudo antes da barra deve ser APENAS posicional.
# PEP 570 – Python Positional-Only Parameters
# https://peps.python.org/pep-0570/
# Keyword-Only Arguments (*) - * sozinho NÃO SUGA valores.
# PEP 3102 – Keyword-Only Arguments
# https://peps.python.org/pep-3102/

# Tudo que vem antes da barra só pode ser argumento posicional 
# Não é possível passar argumentos nomeados antes da /
# Depois da barra pode ser posicional ou nomeado

# * tudo que vier antes pode ser argumento posicional e nomeado
# * tudo que vier depois é argumento nomeado

def soma(a, b, /, *, c, **kwargs):
    print(kwargs)
    print(a + b + c)


soma(1, 2, c=3, nome='teste') 