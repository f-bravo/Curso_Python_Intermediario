# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public - pode ser usado em qualquer lugar
# _ (um underline) = protected - não DEVE ser usado fora da classe ou subclasses.
# __ (dois underlines) = private - "name mangling" só DEVE ser usado na classe em
# que foi declarado.
#  _NomeClasse__nome_attr_ou_method

from functools import partial


class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'
        self.__private = 'isso é private'

    def metodo_publico(self):
        print(self.__private)
        self.__metodo_private()
        return 'metodo_publico'

    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'

    def __metodo_private(self):
        print('__metodo_private')
        return '__metodo_private'


f = Foo()
# print(f.public)
print(f.metodo_publico())
print('-----\n')


# -----------------------------------------------------------------------------


# Relação entre classes:
# Associação, agregação e composição.


print('# Associação:\n')


class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta    

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class FerramentaEscritor:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} em uso.'


escritor = Escritor('Bravo')
caneta = FerramentaEscritor('Caneta')
notebook = FerramentaEscritor('Computador')

escritor.ferramenta = notebook  # A instância escritor associada a instância notebook

print(caneta.escrever())
print(notebook.escrever())
print(escritor.ferramenta.escrever())
print('-----\n')


# -----------------------------------------------------------------------------


print('# Agregação:\n')

# Agregação é uma forma mais especializada de associação entre dois ou mais 
# objetos. 
# Cada objeto terá seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um objeto tem um ou muitos obj
# Os objetos podem viver separadamente, mas pode se tratar de uma relação onde 
# um objeto precisa de outro para fazer determinada tarefa.

 
class Carrinho:
    def __init__(self):
        self._produtos = []


    def total(self):
        return sum(p.preco for p in self._produtos)

    def inserir_produtos(self, *produtos):
        # self._produtos.extend(produtos)
        # self._produtos += produtos
        for produto in produtos:
            self._produtos.append(produto)

    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


carrinho = Carrinho()
p1, p2 = Produto('Teclado', 99.00), Produto('Mouse', 49.90)
carrinho.inserir_produtos(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())  # 148.9

# Carrinho tem um ou mais produtos - 'carrinho tem produtos'
print('-----\n')


# -----------------------------------------------------------------------------


print('# Composição:\n')

# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas as referências dos objetos
#  filhos também são apagadas.

# Para esse exemplo, precisa criar a classe endereço dentro da classe cliente 
# para quando o cliente for apagado o endereço também seja
# A instância de endereços estará dentro da classe cliente. Assim que apagar
# a instância cliente, a instância de endereço também será apagada


class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))  # Dentro da instância Cliente

    def inserir_enderecos_externo(self, endereco):
        self.enderecos.append(endereco)  # Fora da instância cliente

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero


cliente1 = Cliente('Luiz')
cliente1.inserir_endereco('Rua Brasil', 15)
cliente1.inserir_endereco('Av Americana', 592)

endereco_externo = Endereco('Av Madrid', 17555)
cliente1.inserir_enderecos_externo(endereco_externo)
cliente1.listar_enderecos()

del cliente1
print('Após deletar cliente1 ainda tem acesso ao endereço externo')
print(endereco_externo.rua, endereco_externo.numero)


# --------------------------------------------------------------------------------


# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela


class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante

    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome


class Fabricante:
    def __init__(self, nome):
        self.nome = nome


fusca = Carro('Fusca')
volkswagen = Fabricante('Volkswagen')
motor_1_0 = Motor('1.0')
fusca.fabricante = volkswagen
fusca.motor = motor_1_0
print(fusca.nome, fusca.fabricante.nome, fusca.motor.nome)

gol = Carro('Gol')
gol.fabricante = volkswagen
gol.motor = motor_1_0
print(gol.nome, gol.fabricante.nome, gol.motor.nome)

fiat_uno = Carro('Uno')
fiat = Fabricante('Fiat')
fiat_uno.fabricante = fiat
fiat_uno.motor = motor_1_0
print(fiat_uno.nome, fiat_uno.fabricante.nome, fiat_uno.motor.nome)

focus = Carro('Focus Titanium')
ford = Fabricante('Ford')
motor_2_0 = Motor('2.0')
focus.fabricante = ford
focus.motor = motor_2_0
print(focus.nome, focus.fabricante.nome, focus.motor.nome)
