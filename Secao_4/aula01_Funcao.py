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