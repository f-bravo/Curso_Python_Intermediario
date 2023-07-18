# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice" e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro dicionário.
# Usamos as chaves - {} - ou a classe dict para criar dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list

# pessoa = dict(nome='Felipe', sobrenome='Bravo')

# Formas de criar um dicionário:
pessoa = dict(nome='Felipe', sobrenome='Bravo') # menos usada

pessoa = {
    'nome': 'Felipe',
    'sobrenome': 'Bravo',
}
print(pessoa, type(pessoa)) 
# {'nome': 'Felipe', 'sobrenome': 'Bravo'} <class 'dict'>

# Dicionário:
# veja endereços: é uma lista de dicionários. 
pessoa = {
    'nome': 'Felipe',
    'sobrenome': 'Bravo',
    'idade': 22,
    'altura': 1.76,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321},
    ]
}
print(pessoa['nome']) # Felipe
print(pessoa['altura'])  # 1.76
print(pessoa['endereços'][0])  # {'rua': 'tal tal', 'número': 123}
print(pessoa['endereços'][1])  # {'rua': 'outra rua', 'número': 321}

# Para pegar o dicionário com a chave e valor:
for chave in pessoa:
    print(chave, pessoa[chave])
print('-------------------')
for i, k in pessoa.items():
    print(i,k)
print('---------------------\n')

# Criando chaves:
pessoa2 = {}
chave = 'nome'
pessoa2[chave] = 'Felipe'
print(pessoa2[chave])
print(pessoa2)
# Alterando a chave:
pessoa2[chave] = 'Luiz'
print(pessoa2) # Luiz
pessoa2['sobrenome'] = 'Bravo'
print(pessoa2) # {'nome': 'Luiz', 'sobrenome': 'Bravo'}
del pessoa2['sobrenome']
print(pessoa2) # {'nome': 'Luiz'}


# Obtendo a chave se ela existir:
if pessoa2.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa2['sobrenome'])    

# Não existe - ela foi apagada no del
