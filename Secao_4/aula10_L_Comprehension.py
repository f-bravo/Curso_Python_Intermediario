# List comprehension em Python
# List comprehension é uma forma rápida para criar lista a partir de iteráveis.
# print(list(range(10)))

import pprint

# Função para o print bonito - não vou usar
def pt(produtos):
    pprint.pprint(produtos, sort_dicts=False, width=50)

lista = []
for numero in range(10):
    lista.append(numero)
# print(lista)

lista = [
    numero * 2
    for numero in range(10)
]
print(lista)


print('\n# Mapeamento de dados em list comprehension\n')
# Mapeamento: pega o dado transforma ou não e joga em outra lista
# Um dicionário na list Comprehension precisa ter as chaves dentro da lista[]
produtos = [
    {'nome': 'p1', 'preco': 50, },
    {'nome': 'p2', 'preco': 20, },
    {'nome': 'p3', 'preco': 70, },
]

novos_produtos1 = [
    {'nome': produto['nome'], 'preco':produto['preco']}
    for produto in produtos
]
print(*novos_produtos1, sep='\n')
print('-----+-----')

# Caso queira mostrar o dicionário inteiro: Desempacote o dicionário na própria lista  
novos_produtos2 = [
    {**produto} for produto in produtos]

print(*novos_produtos2, sep='\n')
print('-----+-----')

# Alterando o preço em 20:
# Os mapeamentos fica na esquerda do FOR
# O IF a esquerda sempre precisará ter um ELSE.
novos_produtos2 = [
    {**produto, 'preco': produto['preco'] * 1.20}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]
print(*novos_produtos2, sep='\n')
print()


print('\n# FILTER: Filtro de dados em List Comprehension\n')
# O objetivo do filter é não querer incluir algo na lista na condição True
# O filter fica a direita do FOR e o IF  é sem ELSE

lista2 = [n for n in range(10) if n < 5]
print(lista2)


novos_produtos3 = [
    {**produto, 'preco': produto['preco'] * 1.20}
    if produto['preco'] > 20 else {**produto}
    for produto in produtos 
    if produto['preco'] > 30
]
print(*novos_produtos3, sep='\n')


print('\n# List Comprehension com mais de um FOR:\n')
# Não é possível colocar dois valores em um índice da lista. Precisa ter um 
# tipo de dado no índice da lista que aceita mais de um valor. 
# Um tupla por exemplo.

lista3 = []
for x in range(3):
    for y in range(3):
        lista3.append((x,y))
print(lista3)

lista4 = [
    (x,y) 
    for x in range(3)
    for y in range(3)
]
print(lista4)


print('\n# Dictionário Comprehension\n')
# É a mesma coisa. Só troca os colchetes por chaves

produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}

# Com FOR:
for chave, valor in produto.items():
    print(chave, valor)

dict1 = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()
    if chave != 'categoria'
}
print(dict1)
