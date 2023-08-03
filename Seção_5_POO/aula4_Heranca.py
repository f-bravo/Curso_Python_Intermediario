print('# Herança:')

# Super classe:
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def class_name(self):
        print(self.nome, self.sobrenome, self.__class__.__name__) # Nome da classe    


# Subclass Cliente que herda de Pessoa
class Cliente(Pessoa):
    ...

# Subclass Aluno que herda de Pessoa
class Aluno(Pessoa):
    ...


c1 = Cliente('Bruno', 'Henrique')
c1.class_name()

a1 = Aluno('Gabriel', 'Barbosa')
a1.class_name()

# print(help(Cliente))
""" Ordem de execução para busca nas classes

 Method resolution order:
 |      Cliente
 |      Pessoa
 |      builtins.object
"""
# Observe que é de baixo p cima. Da subclass para a superclass
print('-----\n')


# -----------------------------------------------------------------------------


print('Sobreposição de métodos e super classe')

# 

class A:
    atributo_a = 'valor A'

    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'valor B'

    def metodo(self):
        print('B')


class C(B):
    atributo_c = 'valor C'

    def metodo(self):
        super().metodo() # Vai buscar o método na superclass(B)
        print('C')


c = C()
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)

c.metodo()
print(C.mro()) # veja a ordem no MRO abaixo:
# [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
print('-----\n')

# Quando vc herda de uam classe tudo é passado para as subclasses.
# Se na classe A tiver um __init__ com um parâmetro, ele será passado passado 
# para todas as outras subclasses e vc será obrigado a instânciar nelas.

# Se vc colocar um _init__ em B vc vai sobrepor o __init__ do A


class A(object):
    atributo_a = 'valor a'

    def __init__(self, atributo):
        self.atributo = atributo

    def metodo(self):
        print('A')


class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')


class C(B):
    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs):
        # print('EI, burlei o sistema.')
        super().__init__(*args, **kwargs)

    def metodo(self):
        # super().metodo()  # B
        # super(B, self).metodo()  # A
        # super(A, self).metodo()  # object
        A.metodo(self)
        B.metodo(self)
        print('C')


c = C('Atributo', 'Qualquer')
c.metodo()
print('-----\n')

# -------------------------------------------------------------------------------


print('Herança multipla\n')

# Herança Múltipla  uma classe pode estender várias outras classes.
# Herança simples:
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Herança múltipla e mixins
# Log -> FileLog
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Cliente(Pessoa, FileLog)
#
# A, B, C, D
# D(B, C) - C(A) - B(A) - A
#
# método -> falar
#           A
#         /   \
#        B     C
#         \   /
#           D
#
# Python 3 usa C3 superclass linearization para gerar o mro.
# Para saber a ordem de chamada dos métodos Use o método de classe Classe.mro()
# Ou o atributo __mro__ (Dunder - Double Underscore)

# A ordem da herança multipla importa. Quem é colocado primeiro será será buscado
# primeiro pelo mro.

class A:
    ...

    def quem_sou(self):
        print('A')


class B(A):
    ...

    # def quem_sou(self):
    #     print('B')


class C(A):
    ...

    def quem_sou(self):
        print('C')


class D(B, C):
    ...

    def quem_sou(self):
        print('D')


d = D()
d.quem_sou() # D
# print(D.__mro__)
print(D.mro())  # veja a ordem de busca da class D:
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, 
#  <class '__main__.A'>, <class 'object'>]
