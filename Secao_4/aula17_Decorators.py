# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python usar as funções decoradoras em 
# outras funções.

# Funções decoradoras em Python tem que receber uma função - é padrão do Python

# Funções decoradoras - o trabalho dela é receber uma função e criar uma função
# interna para que tenha um closure e essa função interna nã oserá executa e sim
# retornada sem execução para quem for usar a função decoradora possa executar
# a função que está sendo decorada

def criar_funcao(func):  # <- agora a invert_string vira esse parâmetro
    def interna(*args, **kwargs):  # invert_string vira interna
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        return resultado
    return interna

@criar_funcao   # decorador
def inverte_string(string):
    print(f'{inverte_string.__name__}')
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


invertida = inverte_string('123')
print(invertida)  # 321


print('\n# Decoradores com parãmetros\n')

# A0 decorar uma função o Python passa essa função que foi decorada para dentro
# da função decoradora e guarda o valor no escopo da função, na closure.
# A closure será retornada sem ser executada. É como substituir a função(func) externa 
# pela função interna(aninhada)
# Ao decorar a função soma ela vira a função aninhada

def decoradora(func):
        print('Decoradora 1')

        def aninhada(*args, **kwargs):
            print('Aninahda')
            res = func(*args, **kwargs)
            return res
        return aninhada


@decoradora
def soma(x, y):
    return x + y


dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)
print('---------\n')


# ----------------------------------------------------------------------

# Colocando os parenteses na decoradora()
# vc executa o decorador antes que o Python - ele depois tenta pegar o retorno
# do decorador(aninhada).
# A partir do momento que não executa o decorador o Python vai executar a função
# decorada soma. Ele vai na função decorada, passa a função soma para o parâmetro 
# func e vai p aninhada. 
# A partir do momento que cria uma função e executa o python vai tentar executar
# essa função de novo como um decorador porq ele está esperando um decorador( uma
# função decoradora que recebe uma função)
# Com isso agora pode ter acesso aos parâmetros(1,2,3) do decorador

def fabrica_de_decoradores(a=None, b=None, c=None):
    def fabrica_de_funcoes(func):
        print('Decoradora 1')

        def aninhada(*args, **kwargs):
            print('Parâmetros do decorador, ', a, b, c)
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes


@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    return x + y


# multiplica = fabrica_de_decoradores(1,2,3)(lambda x,y: x*y) = linha de baixo
decoradora = fabrica_de_decoradores()
multiplica = decoradora(lambda x, y: x * y)

dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplica(10, 5)
print(dez_mais_cinco)
print(dez_vezes_cinco)
print()
# Decoradora 1 aparece 2 vezes por causa do decorador da soma e decorada = fabrica...

# A função aninhada mais interna é a que vai subistituir a função real (soma)
# para passar parâmetros para o decorador precisa criar outra função e colocar
# para criar o escopo dessa função colocando a fabricada de função dentro
# Primeira função: para pegar os parâmetros do decorador
# Segunda função: é o decorador
# Terceira função: é a função que será executada 

# ----------------------------------------------------------------------------

# Ordem dos decoradores: 
def parametros_decorador(nome):
    def decorador(func):
        print('Decorador:', nome)

        def sua_nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)    
            final = f'{res} {nome}' # f string para concatenar + nome decorador
            return final
        return sua_nova_funcao
    return decorador

@parametros_decorador(nome='terceiro')
@parametros_decorador(nome='segundo')
@parametros_decorador(nome='primeiro')
def soma(x,y):
    return x + y


dez_mais_dez = soma(10, 10)
print(dez_mais_dez)




