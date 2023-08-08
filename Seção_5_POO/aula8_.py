# Funções de coradoras e decoradores com classes

# Classes sem repr só mostra qual a classe e o endereço de memória que ela está

# Para evitar repetição de código sem precisar colocar um __repr__ em cada classe:


# Exemplo um com herança:

from typing import Any


class MyReprMixin:
    def __repr__(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr

class Time(MyReprMixin):
    def __init__(self, nome):
        self.nome = nome


class Planeta(MyReprMixin):
    def __init__(self, nome):
        self.nome = nome


brasil = Time('Brasil')
portugal = Time('Portugal')
print(brasil)
print(portugal)


terra = Planeta('Terra')
marte = Planeta('Marte')
print(terra)
print(marte)
print('-----\n')


# Exemplo com composição - caso queira evitar herança. 

# criada uma função que recebe uma classe.
# definiu uma função que recebe self
# Essa função é para funcionar como se ela estivesse dentro da classe
# Lá no repr dentro da função será atrelado o meu_repr da função


# Exemplo com @decorator

def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr


def adiciona_repr(cls):
    cls.__repr__ = meu_repr
    return cls


@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome


@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome


flamengo = Time('Flamengo')
botafogo = Time('Botafogo')
print(flamengo)
print(botafogo)

jupter = Planeta('jupter')
saturno = Planeta('Saturno')
print(jupter)
print(saturno)
print('-----\n')


# Decorando um método - é a mesma coisa de decorar funções com exceção de que
# métodos de classes são funções que recebe o self no primeiro parâmetro.


def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr


def adiciona_repr(cls):
    cls.__repr__ = meu_repr
    return cls


def meu_planeta(metodo):
    def interno(self, *args, **kwargs):
        resultado = metodo(self, *args, **kwargs)

        if 'Terra' in resultado:
            return 'Você está em casa'
        return resultado
    return interno


@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome


@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

    @meu_planeta
    def falar_nome(self):
        return f'O planeta é {self.nome}'


brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)

print(terra)
print(marte)

print(terra.falar_nome())
print('-----\n')


# -----------------------------------------------------------------------------


print('Método especial __call__')

# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma classe "callable".

# __call__ faz a instância, o objeto da instância ser executável.
# Pode chamar com os parênteses, passar atributos p dentro como o nome


class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, *args, **kwds):
        print('Chamando:', self.phone)

call1 = CallMe('21984674623')
call1()


class CallMe2:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'chamando:', self.phone)

call1 = CallMe2('21984674623')
call1('Felipe')
print('-----\n')


# -------------------------------------------------------------------------------


# Classes decoradoras. A própria classe vai decorar um objeto

"""
class Multiplicar:
    def __init__(self, func):
        self.func = func
        self._multiplicador = 10

        def __call__(self, *args, **kwargs):
            resultado = self.func(*args, **kwargs)
            return resultado * self._multiplicador


@Multiplicar
def soma(x, y):
    return x + y


total1 = soma(2, 5)
print(total1)
"""

class Multiplicar:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador

    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self._multiplicador
        return interna


@Multiplicar(7)
def soma(x, y):
    return x + y


dois_mais_quatro = soma(2, 5)
print(dois_mais_quatro)

