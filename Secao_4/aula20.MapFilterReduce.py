from functools import partial
from types import GeneratorType


# map - para mapear dados
def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.10}
    for produto in produtos
]
print_iter(novos_produtos)
print('\n---------------------------------------------------\n')


def aumenta_preco(valor, porcentagem):
    return round(valor * porcentagem, 2)

aumento_dez_porcento = partial(
    aumenta_preco,
    porcentagem=1.1
)

novos_produtos2 = [
    {**p, 'preco': aumento_dez_porcento(p['preco'])}
    for p in produtos
]
print_iter(novos_produtos2)


# Função MAP --------------------------------------------------
# Para o iterator do MAP não esgotar converta numa lista(list) 


def muda_preco_de_produtos(produto):
    return {
        **produto,
        'preco': aumento_dez_porcento(
            produto['preco']
        )
    }


novos_produtos = list(map(
    muda_preco_de_produtos,
    produtos
))

print_iter(produtos)
print_iter(novos_produtos)


print(
    list(map(
        lambda x: x * 3,
        [1, 2, 3, 4]
    ))
)


print('\nFilter\n')
# FILTER --------------------------------------------------------

# Com list comprehension
produtos_filter = [
    p for p in produtos if p['preco'] > 23
]
print_iter(produtos_filter)

# Filter com função anônima:

novos_produtos3 = filter(
    lambda p: p['preco'] > 23, produtos
)
print_iter(novos_produtos3)

# Filter com função nomeada:

def filtrar_preco(produto):
    return produto['preco'] > 20

novos_produtos4 = filter(
    filtrar_preco, produtos
)
print_iter(novos_produtos4)

# Reduce -------------------------------------------------------

# Reduz um iterável em um único valor.
# Precisa importar de functools
from functools import reduce 

# forma convencional com acumulador e for
total = 0
for p in produtos:
    total += p['preco']

print(round(total,2))

# Usando sum:
print(sum([p['preco'] for p in produtos]))

# Com REDUCE:
# Sempre use um valor inicial(0) para evitar problemas
# A função receberá 2 parâmetros: o acumulador e o produto

def funcao_do_reduce(acumulador, produto):
    return acumulador + produto['preco']

total2 = reduce(
    funcao_do_reduce,
    produtos,
    0
)
print('Total:', total2)

# Reduce com função anônima

reduce_lambda = reduce(
    lambda total, produto: total + produto['preco'], produtos, 0
)

print('Reduce com Lambda:',reduce_lambda)