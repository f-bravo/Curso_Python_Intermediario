# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que podem ter seus próprios 
# atributos(dados da classe) e métodos(ações da classe).
# Os objetos gerados pela classe podem usar seus dados internos para realizar
# várias ações.
# Por convenção, usamos PascalCase para nomes de classes.

"""
class Pessoa:
    ...

p1 = Pessoa() # <- os parênteses gera a instância(objeto p1) da classe Pessoa.    
p1.nome = 'Felipe'
p1.sobrenome = 'Bravo'

print(p1.nome)
print(p1.sobrenome)
"""

# Na classe o primeiro parâmetro é so self. 
# O self é uma convenção. Poderia ter qualquer outro nome.

class Pessoa:
    def __init__(self, nome, sobrenome):  # __init__ = inicializa o objeto e os atributos
        self.nome = nome  # <- cria os atributos dentro da classe
        self.sobrenome = sobrenome


p1 = Pessoa('Felipe', 'Bravo')
print(p1.nome)
print(p1.sobrenome)
print('-----\n')

# Se quer usar os dados da instância no método tem que passar o self.
# Qualquer método que tiver o self vai ter acesso a tudo que tem na class

# Classe - Molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando')    


car1 = Carro('Gol')
print(car1.nome)
car1.acelerar()  # para executar o método precisa ter os parênteses assim como numa função

car2 = Carro('Civic')
print(car2.nome)
car2.acelerar() # O python faz automaticamente. Carro.acelerar('Civic')
print('-------\n')


# ------------------------------------------------------------------------

# Passando parâmetro para um método de class

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'


Cachorro = Animal('Kera')
Cachorro.comendo('Ração')
# Quanto tem parâmetro no método precisa passar o parâmetro ao instânciar

print(Cachorro.nome)
print(Cachorro.comendo('Ração'))
print('--------\n')


# ------------------------------------------------------------------------

# Estados dentro da classe:
# Guardando estados das coiisas


class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando')
            return
        
        print(f'{self.nome} está filmando')   
        self.filmando = True 

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} não está filmando')
            return
        
        print(f'{self.nome} parando de filmar.')   
        self.filmando = False   

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando')
            return 

        print(f'{self.nome} está fotografando ')
        

c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.fotografar()
"""
Canon está filmando
Canon já está filmando
Canon não pode fotografar filmando
Canon parando de filmar.
Canon está fotografando
"""
print('--------\n')

# ------------------------------------------------------------------------


# Atributo de classe


class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('João', 35)
p2 = Pessoa('Helena', 12)

print(Pessoa.ano_atual)
# Pessoa.ano_atual = 1

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
print('--------\n')

# ---------------------------------------------------------------------------


# Os valores dos atributos do objeto(instância) são savos no __dict__
# __dict__ são os dados internos 
class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('João', 35)
print(p1.__dict__)
print(vars(p1))  # vars chama o __dicit_- do objeto

dados = {'nome': 'João', 'idade': 35}
p1 = Pessoa(**dados)  # desempacotando um dicionário 



