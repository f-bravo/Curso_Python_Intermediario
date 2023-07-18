# isinstance: para checar os tipos dos objetos 
# É instância de?

lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

for item in lista:
    if isinstance(item, set):
        print('SET')
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        print('STR')
        print(item)
    
    elif isinstance(item, (int, float)):
        print('Número')
        print(item)

    else:
        print('Outros')
        print(item)    


print('\n# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis\n')
# Mutáveis [] {} set()
# Imutáveis () "" 0, 0.0, None, False, range(0, 10)

# Todos os valores abaixo são considerados falsos
lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteito = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)


print('\n# Iterável e iterator:\n')
# Iterável - detem os valores
# Iterator - entrega um valor por vez - só entrega o próximo valor (next)

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__
print(next(iterator))
print(next(iterator))
print(next(iterator))


print('\n # Generator: funções que sabem pausar em determinado ponto')
import sys

# A lista já está na memória - pode acessar índice por índice
# O generator espera que peça um valor para ele

lista = [n for n in range(100)]
generator = (n for n in range(100)) # só entrega um valor por vez

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(generator)
for n in generator:
    print(n)


print('\n# Generator functions\n')

def generator1(n=0):
    yield 1
    print('Continuando')
    yield 2
    print('mais uma vez')
    yield 3
    print('Terminando')
    return  # para finalizar

gen = generator1(n=0)
for i in gen:
    print(i)


def generator(n=0, maximum=10):
    while True:
        yield n # pausa e guarda o valor
        n += 1

        if n >= maximum:
            return

gen = generator(n=2, maximum=7)
for n in gen:
    print(n)


