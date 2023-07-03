# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

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

# len - quantas chaves
print(len(pessoa)) # 5

# # keys - iterável com as chaves
print(pessoa.keys()) # dict_keys(['nome', 'sobrenome', 'idade', 'altura', 'endereços'])

# values - iterável com os valores
print(pessoa.values())
# dict_values(['Felipe', 'Bravo', 22, 1.76, [{'rua': 'tal tal', 'número': 123},
# {'rua': 'outra rua', 'número': 321}]])

# items - iterável com chaves e valores
print(pessoa.items())
# dict_items([('nome', 'Felipe'), ('sobrenome', 'Bravo'), ('idade', 22), ('altura', 1.76),
#  ('endereços', [{'rua': 'tal tal', 'número': 123}, {'rua': 'outra rua', 'número': 321}])])

# Fazendo a coerção de dict_values para tuple ou list:
print(tuple(pessoa.keys())) # ('nome', 'sobrenome', 'idade', 'altura', 'endereços')
print(list(pessoa.keys())) # ['nome', 'sobrenome', 'idade', 'altura', 'endereços']

print(tuple(pessoa.values()))
print(list(pessoa.values()))

print(tuple(pessoa.items()))
print(list(pessoa.items()))

# Ao chamar o iterador com um for está se referendo as chaves. Se quiser ver os valores
# precisa dizer pessoa.values()
for i in pessoa.values():
    print(i)

# para ver a cahve e valor use o items()
for i in pessoa.items():
    print(i)

# setdefault - adiciona valor se a chave não existe 
pessoa.setdefault('profissão', 'estudante')
print(pessoa['profissão']) # estudante
# Se a chave existir no dicionário o setdefault não faz nada
print()

# Tanto a lista como o dicionário tem o copy
# copy - retorna uma cópia rasa (shallow copy)
d1 = {
    'c1': 1,
    'c2': 2,
}
d2 = d1
print(d2) # {'c1': 1, 'c2': 2}
# nesse caso ele não copia pois usa o memos dicionário salvo na memória
# ao alterar d2, d1 também será alterado. 
d2['c1'] = 100
print(d1) # {'c1': 100, 'c2': 2}

# por isso quando trabalhar com valores mutáveis tem que ficar atendo ao fazer a 
# atribuição(=)

# Usando o copy()
d2 = d1.copy()
d2['c1'] = 1000
print(d1) # {'c1': 100, 'c2': 2}
print(d2) # {'c1': 1000, 'c2': 2}
# Copia raza: tudo que for imutável será copiado para o outro dicionário 
# Mas se tiver valores mutáveis, vai voltar a apontar para o mesmo lugar na memória. 
# Shelow copy - copia raza: não entra em subníveis 
dic1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0,1,2],
}
dic2 = dic1.copy()
dic2['c1'] = 111
print(dic1) # {'c1': 1, 'c2': 2, 'l1': [0, 1, 2]}
print(dic2) # {'c1': 111, 'c2': 2, 'l1': [0, 1, 2]}
# agora se alterar valores mutáveis como a lista:
dic2['l1'][2] = 99
print(dic1) # {'c1': 1, 'c2': 2, 'l1': [0, 1, 99]}
print(dic2) # {'c1': 111, 'c2': 2, 'l1': [0, 1, 99]}
# Alterando dic2 também alterou o dic1
# Copia os valores imutávels e linka os valores mutáveis

# Para copiar tudo Python tem um módulo:
import copy
dic1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0,1,2],
}
dic2 = copy.deepcopy(dic1)
dic2['c1'] = 111
dic2['l1'][2] = 99
print(dic1) # {'c1': 1, 'c2': 2, 'l1': [0, 1, 2]}
print(dic2) # {'c1': 111, 'c2': 2, 'l1': [0, 1, 99]}

# O deepcopy() entra em todos os subníveis de tudo que é mutável.
print()

# get - obtém uma chave - se a chave não existir o get retorna None
print(pessoa.get('nome')) # Felipe

# pop - Apaga um item com a chave especificada (del)
p1 = {
    'nome': 'Felipe',
    'sobrenome': 'Bravo',
}
nome = p1.pop('nome') # apaga a chave nome
print(nome)
print(p1) # Felipe , {'sobrenome': 'Bravo'}

# pop items elimina a última chave.
p2 = {
    'nome': 'Felipe',
    'sobrenome': 'Bravo',
}
last_key = p2.popitem()
print(p2) # {'nome': 'Felipe'}

# update - Atualiza um dicionário com outro - modifica valroes ou cria novos valores
p3 = {
    'nome': 'Felipe',
    'sobrenome': 'Bravo',
}

p3.update({
    'Curso': 'Ciência da Computação',
    'Profissão': 'Desenvolvedor de software'
})
print(p3)
# {'nome': 'Felipe', 'sobrenome': 'Bravo', 'Curso': 'Ciência da Computação', 'Profissão': 'Desenvolvedor de software'}
p3.update({'Profissão': 'Desenvolvedor Python'})

print(p3)
# {'nome': 'Felipe', 'sobrenome': 'Bravo', 'Curso': 'Ciência da Computação', 'Profissão': 'Desenvolvedor Python'}

# Outra maneira é passar argumentos nomeados:
p3.update(curso='Python')
print(p3)
# {'nome': 'Felipe', 'sobrenome': 'Bravo', 'Curso': 'Ciência da Computação', 'Profissão': 'Desenvolvedor Python', 'curso': 'Python'}  

# update também funciona em tuplas e listas
# p3.update(nome='novo valor', idade=30)
# tupla = (('nome', 'novo valor'), ('idade', 30))
# lembrando que a tupla não pdoe ser modificada diretamente. Precisa ser transformada numa lista
lista = [['nome', 'novo valor'], ['idade', 30]]
p3.update(lista)
print(p3)


# -------------------------------------------------------------------


# Exercício
print('\n------ Exercício ------ \n')

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    if acertou:
        qtd_acertos += 1
        print('Acertou')

    else:
        print('Errou')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas')      

