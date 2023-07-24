# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - São úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120

def recursiva(inicio=0, fim=4):

    print(inicio, fim)

    # Caso base
    if inicio >= fim:
        return fim

    # Caso recursivo
    # contar até chegar ao final
    inicio += 1
    return recursiva(inicio, fim)


print(recursiva(0, 10)) # com 1mil:  996 1000
print()
# Toda vez que usa função recursiva o escopo inteiro é salvo na call stack.
# Por isso só conseguiu chegar até 996. O limite de recursão do Python é 1000. 

# Número fatorial:
print('Fatorial:\n')
def fatorial(n):
    if n <= 1:
        return 1
    
    return n * fatorial(n -1)

print(fatorial(5))
print(fatorial(10))
