# O que é JSON - JavaScript Object Notation
# JSON - JavaScript Object Notation (extensão .json)
# É uma estrutura de dados que permite a serialização de objetos em texto 
# simples para facilitar a transmissão de dados através da rede, APIs web ou 
# outros meios de comunicação.
# O JSON suporta os seguintes tipos de dados:
# Números: podem ser inteiros ou com ponto flutuante, como 42 ou 3.14
# Strings: são cadeias de caracteres, como "Olá, mundo!" ou "12345"
# As strings devem ser envolvidas por aspas duplas
# Booleanos: são os valores verdadeiro (true) ou falso (false)
# Arrays: são listas ordenadas de valores, como [1, 2, 3] ou
#   ["Oi", "Olá", "Bom dia"]
# Objetos: são conjuntos de pares chave/valor -> {"nome": "João", "idade": 30}
# null: é um valor especial que representa ausência de valor
#
# Ao converter de Python para JSON:
# Python        JSON
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         false
# None          null


# C:\Teste_Python

string_json = '''
{
    "title": "O Senhor dos Anéis: A Sociedade do Anel",
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
    "is_movie": true,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
    "budget": null
  }
'''
print(string_json)

import os
import json
from pprint import pprint

# dumps - jogar p fora. O (s) no final é para trabalhar com strings
# loads - carregar p dentro

# Carregando o Json p ser convertido no formato do Python loads()

filme = json.loads(string_json)
print(filme)
print('-----')
pprint(filme, width=50)

print(filme["title"])  # O Senhor dos Anéis: A Sociedade do Anel
print(filme["characters"][2])  # Gandalf


from typing import TypedDict
# TypedDict - habilita que vc crie uma classe e herder de TypedDict
# Basta colocar a tipagem:

class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None | float

filme: Movie = json.loads(string_json)
print(filme["year"])  # agora ao colocar os colchetes mostra as chaves do arquivo
print(filme["imdb_rating"])

# Jogando de Python p Json --> dumps
# Forma mais fácil de visualizar 
json_string = json.dumps(filme, ensure_ascii=False, indent=2)
print(json_string)


# existe maneira mais fácil de fazer hoje em dia. Mas por muitos anos foi assim
# Hoje em dia usa a path.lib

# Agora é com arquivos

NOME_ARQUIVO = 'aula3_Json.json'
CAMINHO_ARQUIVO_ABSOLUTO = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        NOME_ARQUIVO
    )
)

print(__file__) # c:\Python_intermediario\Seção_6_Modulos\aula3_Json.py

# Caminho absoluto do diretório atual:
print(os.path.dirname(__file__)) # c:\Python_intermediario\Seção_6_Modulos

# Unindo os dois:
print(os.path.join(os.path.dirname(__file__),NOME_ARQUIVO))
# c:\Python_intermediario\Seção_6_Modulos\aula3_Json.json


dicionario_filme = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel', 
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring', 
    'is_movie': True, 
    'imdb_rating': 8.8, 
    'year': 2001, 
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'], 
    'budget': None
}
# Criando e salvando esse dicionário_filme em um arquivo:
with open(CAMINHO_ARQUIVO_ABSOLUTO, 'w', encoding='utf8') as arquivo:
    json.dump(dicionario_filme, arquivo, ensure_ascii=False, indent=2)

# Lendo:
with open(CAMINHO_ARQUIVO_ABSOLUTO, 'r', encoding='utf8') as arquivo:
    filme_json = json.load(arquivo)
    print(filme_json)