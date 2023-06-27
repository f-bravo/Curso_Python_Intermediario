# args - argumentos não nomeados
# * args(empacotamento e desempacotamento)

# Desempacotamento:
x, y, *resto = 1, 2, 3, 4, 5
print(x, y, resto) # 1 2 [3, 4, 5]

def soma_args(*args):
    print(args)  # (1, 2, 3, 4, 5)

soma_args(1,2,3,4,5)

def somatorio(*args):  # *args: empacota o que for enviar dentro de uma tupla
    total = 0 # Acumulador
    for num in args:
        total += num
    return total   

total = somatorio(1,2,3,4,5,6)
print(total) # 21

# Era só um exemplo. Existe uma função para somar no Python
numeros = 1,2,3,4,5,6
print(sum(numeros)) # 21


# ----------------------------------------------------------------------
# Exercícios

def multiplica(*args):
    total = 1
    for i in args:
        total = total * i
    return total

multi1 = multiplica(1,2,3,4,5)
print(multi1)


def par_impart(x):
    if x % 2 == 0:
        return f'{x} = par'
    return f'{x} = ímpar'

num = par_impart(2)
print(num)
num = par_impart(5)
print(num)
num = par_impart(1777)
print(num)


# Funções de primeira classe

def saudacao(msg, nome):
    return f'{msg}, {nome}'

def executa(funcao, *args):
    return funcao(*args)

variavel = executa(saudacao, 'Olá', 'Aluno')
print(variavel)

# Pode passar funções como argumento de outras funções e também
# retornar funções de dentro de uma função
# Academicamente:
"""
Higher Order Functions - Funções que podem receber e/ou retornar outras funções

First-Class Functions - Funções que são tratadas como outros tipos de dados 
comuns (strings, inteiros, etc...)
"""

