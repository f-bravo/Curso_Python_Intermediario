# Count é um iterador sem fim
# O count está no módulo itertools

from itertools import count

c1 = count(0, 5)  # tem apenas start e step
r1 = range(0, 50, 5)

for i in c1:
    if i > 55:
        break
    print(i)

print('--------')

for i in r1:
    print(i)

print('\n-----------------------\n')


print('Análise Combinatória:')

# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import combinations, permutations, product

# Para substituir o print abaixo eu fiz uma função:
# print(*list(combinations(pessoas, 2)), sep='\n')

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]

print_iter(combinations(pessoas, 2))
print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))

print('\n--------------------------\n')


print('groupby')

from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

# Ordenação: é uma lista de dicionários

alunos_agrupados = sorted(alunos, key=lambda a: a['nota'])

for aluno in alunos_agrupados:
    print(aluno)


grupos = groupby(alunos_agrupados, key=lambda a: a['nota'])

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)


print('\n--------------\n')
# observe - existem dois pontos de alteração. Se a chave mudar tem 2 lugares para 
# alterar. Para isso substitua a função lambda por uma função nomeada - ordena()

def ordena(aluno):
    return aluno['nota']


alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)

