# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer outra em Python. Porém, são funções
# anônimas que contém apenas uma linha.

# lista = [4, 32, 1, 34, 5, 6, 6, 21, ]
# lista.sort(reverse=True)
# sorted(lista)
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

def ordena(item):
    return item['nome']

lista.sort(key=ordena)

for i in lista:
    print(i)

# O python usa a tabale unicode para ordenar 
print('----------LAMBDA----------')
# A mesma função com Lambda:
lista.sort(key=lambda item: item['nome'])
for i in lista:
    print(i)

# Importante: usar Lambda com sort a lista é alterada.
# Caso não queira alterar a lista use sorted. Copia raza ok.
# Se quiser copia profunda ordena e faça o deep.copy() depois
print('------------LAMBDA com sorted: -------------\n')

def exibir(lista):
    for item in lista:
        print(item)

lista1 = sorted(lista, key=lambda item: item['nome'])
lista2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(lista1)
exibir(lista2)


# Convertendo funções em funções lambda:

def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y


print(soma(2,7)) 

print(executa(soma, 2, 5)) 

print(executa(lambda x,y: x + y, 2,3))

print()

def criar_multiplcador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica


duplica = criar_multiplcador(2)
duplica = executa(lambda m: lambda n: n * m, 3)

print(duplica(2))

print(executa(lambda *args: sum(args), 1,3,5,7,9))  # 25

# Lambda é para funções de uma linha.
# Não é recomendado para coisas complexas
