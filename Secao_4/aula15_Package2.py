# Os package são arquivos onde organiza os módulos de arquivos Python.
# É do módulo que se importa  
# O pacote é somente uma pasta, um name_space.

# Criando um arquivo __init__ no arquivo Pacotes:

# O arquivo __init__.py é importado assim que o package é executado.
import Pacotes

# Importando o: Pacotes
# Pacotes.Calculadora  


# Qualquer coisa que executar no __init__ vai ficar disponíivel no package
"""
Quando importa algo o Python automaticamente exporta o __init__ e pode usar
em outros módulos. Dessa maneira é usado para "enganar" o Python.
"""
print(Pacotes.quadrado(5))

# Como exportar tudo do Módulo Calculadora usando o __init__?
# ao fazer o import o package Pacotes é considerado como um módulo.
# Quando faz import dentro de um módulo i Python exporta todas as coisas.
# Nesse exemplo serão exportadas tds as funções. Inclusive a nova função
# que multiplica 3 variáveis.
print(Pacotes.calc_mult(2,2,2))

# Se quisesse outros módulos vindo do package Pacotes, bastaria fazer o import
# dentro do __init__. from Pacotes.Calculadora import *.
# Basta substituir o nome Calculadora pelo módulo que deseja importar.