# Sets - Conjuntos em Python (tipo set)

# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}
# Set parece dicionário por usar {} mas só tem o valor.

s1 = set()  # vazio
s1 = {'Luiz', 1, 2, 3}  # com dados - set não garante ordem
print(s1)

# Sets são eficientes para remover valores duplicados de iteráveis.
# - Seus valores serão sempre únicos;

s2 = {1,2,3,3,3,4,2,1}  # {1, 2, 3, 4}
print(s2)

# Removendo valores duplicados de uma lista:
l1 = [1,2,3,3,3,3,4,5]
set1 = set(l1)
l2 = list(set1)
print(l2)  # [1, 2, 3, 4, 5]

# - Não aceitam valores mutáveis 
# set2 = {1,2,3, {12}}  # unhashable type - valor mutável e não é aceito no set

# Tupla aceita - mas n esqueça da vírgula sobrando no final
set2 = {1,2,3, (4,4,5,)}  # {1, 2, 3, (4, 4, 5)}
print(set2)

# - não tem índex;
# não da para encontrar um elemento. Ele sempre retorna uma sequência sem ordem garantida 
print('----')
# - são iteráveis (for, in, not in)
for i in set2:
    print(i)

# Métodos úteis:
# add, update, clear, discard
set3 = set()
set3.add('Um')  # add só aceita um valor
set3.add(2)
print(set3)  # {'Um', 2}

set3.update((1,2,3,4))
print(set3)
set3.update(('Bravo', 5,6)) 
print(set3)  # {1, 'Um', 3, 2, 4, 'Bravo', 5, 6}

# set.clear() limpa o set

set3.discard('Bravo')  # {1, 'Um', 3, 2, 4, 5, 6}
print(set3)


# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1.union(s2) # {1, 2, 3, 4}
# outra forma é usar o (|)
s3 = s1 | s2
print(s3)

s3 = s1 & s2
print(s3)  # {2, 3}

s3 = s1 - s2
print(s3)  # {1}

s3 = s1 ^ s2
print(s3) # {1, 4}


# Uso de Sets
conjunto = set()
while True:
    item = input('-> ')
    conjunto.add(item.lower())

    if 'f' in conjunto:
        print('FIM')
        break

    print(conjunto)


# -------------------------------------------------------------------


# Exercício - encontre a números repetidos na lista

lista_de_listas_de_inteiros = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
    [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
    [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
    [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
    [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
    [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
    [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
    [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
    [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
    [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]

def encontrar_duplicado(lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1

    for num in lista_de_inteiros:
        if num in numeros_checados:
            primeiro_duplicado = num
            break

        numeros_checados.add(num)

    print()
    return primeiro_duplicado

for lista in lista_de_listas_de_inteiros:
    print(lista, f'({encontrar_duplicado(lista)})')




