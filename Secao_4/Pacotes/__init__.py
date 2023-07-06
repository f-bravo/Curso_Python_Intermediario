# from .Calculadora import calc_div, calc_soma, calc_mult

# Um dos poucos lugares que o import usando o * "pode ser usado" é aqui.
# O import acima ficaria assim:
from Pacotes.Calculadora import *

print('Importando o:', __name__)

def quadrado(x):
    return x * x

# Lembrando novamente:
# O __init_- é executado assim que executa o Package. Assim pdoe fazer o
# Python achar que o Package é um módulo importando as cosias de dentro do
# Package aqui no __init__.py

from Pacotes.mod_produtos import produtos
