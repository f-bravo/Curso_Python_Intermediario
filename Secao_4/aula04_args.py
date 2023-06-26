# args - argumentos não nomeados
# * args(empacotamento e desempacotamento)

# Desempacotamento:
x, y, *resto = 1, 2, 3, 4, 5
print(x, y, resto) # 1 2 [3, 4, 5]

def soma_args(*args):
    print(args)  # (1, 2, 3, 4, 5)

soma_args(1,2,3,4,5)

def somatorio(*args):  # *args: empacota o que for enviar dentro de uma tupla
    total = 0 # Acumulador
    for num in args:
        total += num
    return total   

total = somatorio(1,2,3,4,5,6)
print(total) # 21

# Era só um exemplo. Existe uam função para somar no Python
numeros = 1,2,3,4,5,6
print(sum(numeros))








