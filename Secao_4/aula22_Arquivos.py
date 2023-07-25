# No Windows:
# Sempre que precisar criar um caminho coloque a barra invertida dupla


# Sempre que abrir um arquivo precisa fechar. Deixar arquivo aberto gera problemas
# no próprio arquivo.

# Modos 
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)

caminho_arquivo = 'C:\\python_arquivos\\'
caminho_arquivo += 'aula22.txt'

# arquivo = open(caminho_arquivo, 'w')
# arquivo.close()

# Context manager - with(abre e fecha) arquivos

with open(caminho_arquivo, 'w') as arquivo:
    print('Abrindo arquivo')
    print('Fechando arquivo')

# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)

with open(caminho_arquivo, 'w') as arquivo:
    arquivo.write('Abrindo - linha 1\n')
    arquivo.write('Continuando - linha 2\n')

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())

# para escrever e ler o arquivo: 
# precisa do 'w+' e o seek para mover o cursor p o topo do arquivo
with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('Abrindo - linha 1\n')
    arquivo.write('Continuando - linha 2\n')
    arquivo.write('Escrevendo e lendo o arquivo')
    arquivo.seek(0, 0)
    print(arquivo.read())

# Para escrever um iterável dentro do objeto use writelines

# Modo 'w' - apaga tudo e escreve novamente
# Modo 'a' - não apaga e escreve no final. Append mode

# Enconding:

# No linux e Mac - usa o padrão de caracteres utf-8
# No Windows precisa usar colocar o enconding para caracteres acentuados
# Para salvar em UTF-8:

# with open(caminho_arquivo, 'w+', enconding='utf-8') as arquivo:

# Usando módulos:
import os

# Apagar o arquivo: ambos fazem a mesma coisa

# os.remove(caminho_arquivo)
# os.unlink(caminho_arquivo)

# Renomeando arquivo:
# os.rename(caminho_arquivo, 'aula_nova.txt')


# Salvando dados Python com módulo JSON

# A melhor estrutura de dados para salvar um dicionário Python é o Json

import json

pessoa = {
    'nome': 'Felipe',
    'sobrenome': 'Bravo',
    'enderecos': [
        {'rua': 'A', 'numero': 32},
        {'rua': 'B', 'numero': 55},
    ],
    'altura': 1.77,
    'numeros_preferidos': (3,7,9,11,23),
    'dev': True,
    'nada': None,
}

# with open('aula22.json', 'w', enconding='utf-8) as arquivo:
#     json.dump(pessoa, arquivo)

# {"nome": "Felipe", "sobrenome": "Bravo", "enderecos": [{"rua": "A", "numero": 32}, 
# {"rua": "B", "numero": 55}], "altura": 1.77, "numeros_preferidos": [3, 7, 9, 11, 23], 
# "dev": true, "nada": null}

# Geralmente é recomendado manter o arquivo dessa maneira por questões de 
# compatibilidade

# Mas se quiser coloque o esure_ascii=False - usa a codificação de caracteres
# do seu sistema. 
# Para formatar coloque ident=2

# OBS: JSOn não suporta coisas que executam ações:
# funções, métodos, classes.

with open('aula22.json', 'w', encoding='utf-8') as arquivo:
    json.dump(
        pessoa, 
        arquivo,
        ensure_ascii=False,
        indent=2,
    )


# Carregaundo um arquivo:
with open('aula22.json', 'r', encoding='utf-8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    print(type(pessoa)) # para ver o tipo

"""
{'nome': 'Felipe', 'sobrenome': 'Bravo', 'enderecos': [{'rua': 'A', 'numero': 32}, 
{'rua': 'B', 'numero': 55}], 'altura': 1.77, 'numeros_preferidos': [3, 7, 9, 11, 23], 
'dev': True, 'nada': None}
<class 'dict'>
"""