# random tem geradores de números pseudoaleatórios
# Obs: números pseudoaleatórios significa que os números parecem ser aleatórios,
# mas na verdade não são. Portanto, este módulo não deve ser usado para 
# segurança ou uso criptográfico.
# O motivo disso é que quando temos uma mesma entrada e um mesmo algorítimo,
# a saída pode ser previsível.
# doc: https://docs.python.org/pt-br/3/library/random.html
import random

# Funções:
# seed
#   -> Inicializa o gerador de random (por isso "números pseudoaleatórios")
# random.seed(0)

# random.randrange(início, fim, passo)
# Gera um número inteiro aleatório dentro de um intervalo específico
r_range = random.randrange(10, 20, 2)
print(r_range)

# random.randint(início, fim)
# Gera um número inteiro aleatório dentro de um intervalo "sem passo"
r_int = random.randint(10, 20)
print(r_int)

# random.uniform(início, fim)
# Gera um número flutuante aleatório dentro de um intervalo "sem passo"
r_uniform = random.uniform(10, 20)
print(r_uniform)

print('\nShuffle')
# random.shuffle(SequenciaMutável) -> Embaralha a lista original
nomes = ['Luiz', 'Maria', 'Helena', 'Joana']
random.shuffle(nomes)
print(nomes)

print('\nSample')
# random.sample(Iterável, k=N)
# Escolhe elementos do iterável e retorna outro iterável (não repete)
novos_nomes = random.sample(nomes, k=3)
# print(nomes)
print(novos_nomes)

print('\nChoices')
# random.choices(Iterável, k=N)
# Escolhe elementos do iterável e retorna outro iterável (repete valores)
novos_nomes = random.choices(nomes, k=3)
print(nomes)
print(novos_nomes)

# random.choice(Iterável) -> Escolhe um elemento do iterável
print(random.choice(nomes))
print('\n-------------------------------------------------\n')

# -----------------------------------------------------------------------------
# Secrets - gera números aleatórios seguros
# -----------------------------------------------------------------------------


# secrets gera números aleatórios seguros
import secrets

# SystemRandom - mais seguro 

# Para deixa o módulo random seguro:
random = secrets.SystemRandom()

# print(secrets.randbelow(100))
# print(secrets.choice([10, 11, 12]))

# Funções:
# seed -> NÃO funciona
# random.seed(10)

# random.randrange(início, fim, passo)
#   -> Gera um número inteiro aleatório dentro de um intervalo específico
r_range = random.randrange(10, 20, 2)
print(r_range)

# random.randint(início, fim)
#   -> Gera um número inteiro aleatório dentro de um intervalo "sem passo"
r_int = random.randint(10, 20)
print(r_int)

# random.uniform(início, fim)
#   -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"
r_uniform = random.uniform(10, 20)
print(r_uniform)

# random.shuffle(SequenciaMutável) -> Embaralha a lista original
nomes = ['Luiz', 'Maria', 'Helena', 'Joana']
# random.shuffle(nomes)
print(nomes)

# random.sample(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (não repete)
novos_nomes = random.sample(nomes, k=3)
print(nomes)
print(novos_nomes)

# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
novos_nomes = random.choices(nomes, k=3)
print(nomes)
print(novos_nomes)

# random.choice(Iterável) -> Escolhe um elemento do iterável
print(random.choice(nomes))

import string as s
from secrets import SystemRandom as Sr

print(s.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(s.digits) # 0123456789
print(s.punctuation) # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

# usando todos os caracteres para formar senhas de forma aleatória.
# .join uni todas. Sr é a instância com apelido do SystemRandom.
print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=64)))

# Comando para digitar no terminal e formar uma senha aleatória:
# python -c "import string as s;from secrets import SystemRandom as Sr; print(''.join(Sr().choices(s.ascii_letters + s.punctuation + s.digits,k=12)))"
print('\n-----------------------------------------------\n')


# -----------------------------------------------------------------------------
# Módulo string - class Template - para substituir variáveis em texto
# -----------------------------------------------------------------------------


# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.

import locale
import string
from datetime import datetime
from pathlib import Path

CAMINHO_ARQUIVO = Path(__file__).parent / 'aula6.txt'

locale.setlocale(locale.LC_ALL, '')


def converte_para_brl(numero: float) -> str:
    brl = 'R$ ' + locale.currency(numero, symbol=False, grouping=True)
    return brl


data = datetime(2023, 8, 23)
dados = dict(
    nome='João',
    valor=converte_para_brl(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='F. B.',
    telefone='+55 (11) 98808-8188'
)
import json
print(json.dumps(dados, indent=2, ensure_ascii=False))

# Delimitador é o simbolo que vai trocar de lugar com a variável do dict dados
# se precisar colocar alguma coisa colada na variável faça: %{empresa}

# criando o prórrio delimiter do Template.
class MyTemplate(string.Template):
    delimiter = '%'

# template.substitute - substitui os valores. Se tiver faltando algo da erro.

with open(CAMINHO_ARQUIVO, 'r', encoding='utf8') as arquivo:
    texto = arquivo.read()
    # template = string.Template(texto) com o delimitador $ que é o default
    template = MyTemplate(texto)  # criando uma classe para modificar o delimitador
    print(template.substitute(dados))

""" 
Prezado(a) João,

Informamos que sua mensalidade será cobrada no valor de R$ 1.234.456,00 no dia 
23/08/2023. Caso deseje cancelar o serviço, entre em contato com a F. B. pelo 
telefone +55 (11) 98808-8188.  

Atenciosamente,

F. B.,
"""
