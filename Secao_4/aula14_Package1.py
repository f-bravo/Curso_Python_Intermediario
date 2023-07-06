# Para importar um pacote(package) que é uma pasta é a mesma coisa
# de importar os módulos da aula anterior.
# Obs: desde que os arquivos estejam na mesma hierarquia, na mesma raiz.

# No módulo Patotes tem o arquivo Calculadora.py

from sys import path

# Formas de importação:
from Pacotes import Calculadora
print(Calculadora.calc_div(5,5))
print(Calculadora.calc_soma(5,5))
print('-------------')

from Pacotes.Calculadora import calc_soma, calc_div
print(calc_soma(10,10))
print(calc_div(10,10))
print('-------------')
import Pacotes.Calculadora
print(Calculadora.calc_soma(50,50))
print(Calculadora.calc_div(50,50))


# quando se tem muitos módulos pode ficar confuso o ponto de vista do __main__ 
print(__name__)

