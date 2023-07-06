from Pacotes import produtos
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
"""
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
"""

# Para treinar coloque a lista de produto em outro package e faça a importação
# Nesse exemplo está em Pacotes/mod_produtos
# OBS: 
# usando o __init__ aqui nesse arquivo importe o package Pacotes / produtos

import copy

novos_produtos = copy.deepcopy(produtos)

novos_produtos = [
    {**produto, 'preco': round(produto['preco'] * 1.1, 2)} 
    for produto in produtos]

print(*novos_produtos, sep='\n')
print()
# print(*produtos, sep='\n') conferindo se a lista original foi alterada


# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)


produtos_ordenados = sorted(
    copy.deepcopy(produtos),
    key=lambda produto: produto['nome'], 
    reverse=True
)
print(*produtos_ordenados, sep='\n')
print()

# Ordene os produtos por preco crescente e gere uma copia profunda
produtos_ordenados_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda produto: produto['preco']
)
print(*produtos_ordenados_preco, sep='\n')
print()

#----------------------------------------------------------------------


# Exercício - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, x):
    def func_interna(y):             
        return funcao(x,y)
    return func_interna


somando = criar_funcao(soma, 2)
print(somando(13))

multiplicando = criar_funcao(multiplica, 3)
print(multiplicando(10))