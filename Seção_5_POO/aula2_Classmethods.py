# Método de classe:

# @classmethod -> é um decorator. Com ele da para chamar a classe sem
# passar self. Mas precisa receber um parâmetro que é a própria chamado de cls


# O método de classe pode ser usado para fazer um factory method que é um método
# que cria um outro objeto da mesma classe.
# O Método de classe (CLS) é o molde da classe.
# Assim vc chama diretamente a classe e não a instância. Você não tem acesso a
# instância dentro desse método.


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def medoto_de_classe(cls):
        ('Hello')

    @classmethod
    def criar_idoso(cls, nome):
        return cls(nome, 60)
    
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)


p1 = Pessoa('João', 34)
p2 = Pessoa.criar_idoso('Maria')
p3 = Pessoa('Anônima', 23)
p4 = Pessoa.criar_sem_nome(29)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)
print('--------\n')


# ------------------------------------------------------------------------


# método estático: é um decorator
# @classmethod -> é uma função que está dentro da classe.
# Ele não tem acesso self e cls
# Usado mais por organização para que o método fique dentro da classe


# ------------------------------------------------------------------------


# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático não tem (self e cls)

# Forma comum da programação

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password    


c1 = Connection()
c1.set_user('Felipe')
c1.set_password('1234')
print(c1.user, c1.password)
print('-----\n')

# Cria uma conexão que já recebe user e password
# Como criar uma classe que já configura user e password?
# Mesmo não configurando o __init será possível passar user e password

class Connection2:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    @classmethod
    def user_authentication(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod
    def log(msg):
        print('Log:', msg)

c2 = Connection2.user_authentication('Bravo', '12345')
print(Connection2.log('Log ok'))
print(c2.user, c2.password)
print('-----\n')


# ------------------------------------------------------------------------


# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto. É um método que se comporta como um
# atributo.
# Geralmente @property é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código


class Caneta:
    def __init__(self, cor):
        self.cor = cor

    def get_cor(self):
        print('GET cor')
        return self.cor    


caneta = Caneta('Azul')
print(caneta.get_cor())
print('-----\n')

# @property - método que se comporta como atributo.

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property   # getter para obter um valor
    def cor(self):
        print('Executando uma "ação"')
        return self.cor_tinta

Canetinha = Caneta('Preta')
print(Canetinha.cor)  # método cor que se comporta como atributo
print('-----\n')


# ------------------------------------------------------------------------


# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.

# OBS: @property -> é um método. Método não salva valor. Apenas executa ações.

# Precisa ter um atributo para salvar a cor:
# Existe uma conveção para usar o atributo com um ou dois underline (_cor)
# Significa que esse atributo não deve ser usado fora da classe pois é protegido. 
# Isso se chama encapsulamento. Será visto em uma aula mais a frente

# O setter é bom para fazer restrição. 
# Exemplo: se não quiser usar uma cor faça um if no setter

class Caneta2:
    def __init__(self, cor):
        self._cor = cor

    @property
    def cor(self):
        print('@property')
        return self._cor

    @cor.setter 
    def cor(self, valor):  # precisa do self e precisa receber um valor
        print('@cor.setter')
        self._cor = valor  # aqui configura o valor do atributo _cor


caneta2 = Caneta2('Preta')  # ao instânciar a classe não executa setter
print(caneta.cor)
print('-----')
caneta2.cor = 'Marrom'
print(caneta2.cor)
print('-----\n')

# OBS: se tirar o underline (_cor) do self._cor = cor:
# ao instânciar a classe ela vai passar no setter já no __init__ pois o @cor.setter
# é o nome do método - def cor(): chamar o setter diretamente


# Acrescentando a cor da tampa com getter e setter:

class Caneta3:
    def __init__(self, cor):
        # private protected
        self.cor = cor
        self._cor_tampa = None  # O cor_tampa n ta configurado no init. Por isso = None

    @property
    def cor(self):
        print('ESTOU NO GETTER')
        return self._cor

    @cor.setter
    def cor(self, valor):
        print('ESTOU NO SETTER')
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


caneta4 = Caneta3('Preta')
caneta4.cor = 'Verde'
caneta4.cor_tampa = 'Azul'
print('Caneta:', caneta4.cor)
print('Cor_tampa:', caneta4.cor_tampa)
