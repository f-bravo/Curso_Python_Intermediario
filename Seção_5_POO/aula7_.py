# Special Methods, Magic Methods ou Dunder Methods
# Dunder = Double Underscore = __dunder__
# Antigo útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# Self = lado esquerdo e other = lado direito
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str


# Ao criar um classe vc pode definir um método para ver a representação do objeto.
# __repr__(self) - str : para ver representação de objetos, para de devs


class Ponto:
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        # class_name = self.__class__.__name__
        class_name = type(self).__name__
        return f'{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r})'    


p1 = Ponto(1, 2)
p2 = Ponto(88, 99)

# Ao definir a função str para ver o __repr__ precisa usar a função repr
print(p1) # (1, 2) - retorna str
print(repr(p2)) # Ponto(x=88, y=99, z='String') - retorna repr

# Repr dentro de uma f'string':
print(f'{p2!r}') # Ponto(x=88, y=99, z='String')
print('-----\n')


# -----------------------------------------------------------------------------


# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e retornar o novo objeto. Por isso, 
# new recebe cls para criar a instância.
# __new__ DEVE retornar o novo objeto
# __init__ é o método responsável por inicializar a instância. Por isso, init 
# recebe self.
# __init__ NÃO DEVE retornar nada (None)
# object é a super classe de uma classe


class A:
    def __new__(cls, *args, **kwargs):
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, x):
        self.x = x
        print('Sou o init')

    def __repr__(self):
        return 'A()'


a = A(123)
print(a.x)
print('-----\n')
# O __init__ - vai usar o tempo todo.
# O __new__ - vai usar muito pouco


# -----------------------------------------------------------------------------


print('# Context Manager\n')
# Como implementar classe com Context Manager
# Tudo que tem o conceito de abrir e fecar, conectar e desconectar, capturar e
# liberar. Tudo isso pdoe fazer um context manager

# Context Manager com classes - Criando e Usando gerenciadores de contexto
# Você pode implementar seus próprios protocolos apenas implementando os dunder
#  methods que o Python vai usar.
# Isso é chamado de Duck typing. Um conceito relacionado com tipagem dinâmica 
# onde o Python não está interessado no tipo, mas se alguns métodos existem no 
# seu objeto para que ele funcione de forma adequada.
# Duck Typing:
# Quando vejo um pássaro que caminha como um pato, nada como
# um pato e grasna como um pato, eu chamo aquele pássaro de pato.
# 
# Para criar um context manager, os métodos __enter__ e __exit__ devem ser 
# implementados.
# O método __exit__ receberá a classe de exceção, a exceção e o traceback. 
# Se ele retornar True, exceção no with será suprimidas.
# Ex:
# with open('aula7.txt', 'w') as arquivo:


class MyOpen:
    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('ABRINDO ARQUIVO')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo

    def __exit__(self, class_exception, exception_, traceback_):
        print('FECHANDO ARQUIVO')
        self._arquivo.close()


with MyOpen('S5_aula7.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)

print('-----\n')


# -----------------------------------------------------------------------------


# Outra forma de Criar context manager com decorator

from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        yield arquivo
    except Exception as e:
        print('Ocorreu erro', e)
    finally:
        print('Fechando arquivo')
        arquivo.close()


with my_open('S5_aula7_1.txt', 'w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n', 123)
    arquivo.write('Linha 3\n')
    print('WITH', arquivo)







