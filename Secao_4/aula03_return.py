# Funções com return

def soma(x, y):
    print(x + y)

# Se quiser armazenar a soma numa variável e fazer outra soma?
soma1 = soma(2, 2)
soma2 = soma(3, 3)
# print(soma1 + soma2)     
# TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'       
# não é possível pois é preciso ter o retorno. Sem ele é um não valor. 
# Por isso se usa o return
# print é uma função da linguagem que mostra alguma coisa na tela.
def soma(x, y):
    return x + y

soma1 = soma(2, 2) # 4
soma2 = soma(3, 3) # 6
print(soma1 + soma2) # 10

# A paravra return indica para o Python: para tudo e retorne esse valor.
# Após o return a função não lê mais o código.

def soma_(x, y):
    if x > 10:
        return f'Maior que 10'
    return x + y

soma3 = soma_(11, 4)
print(soma3) # Maior que 10





