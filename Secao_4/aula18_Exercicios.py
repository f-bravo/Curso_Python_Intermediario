# Exercício - Unir listas na ordem


def zipper(l1, l2):
    intervalo = min(len(l1), len(l2))
    return [(l1[i], l2[i]) for i in range(intervalo)]

from itertools import zip_longest

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']

# ZIP(usa valor da lista menor) para juntar listas 
# zip_longest(usa valor da lista maior) para juntar listas

print(list(zip(l1, l2)))
print(list(zip_longest(l1, l2, fillvalue='SEM CIDADE')))


# ----------------------------------------------------------


lista_a = [10, 2, 3, 40, 5, 6, 7]
lista_b = [1, 2, 3, 4]

# Maneira mais Pythonica
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)

lista_soma = []
for i in range(len(lista_b)):
    lista_soma.append(lista_a[i] + lista_b[i])
print(lista_soma)

lista_soma = []
for i, _ in enumerate(lista_b):
    lista_soma.append(lista_a[i] + lista_b[i])
print(lista_soma)
