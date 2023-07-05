# Try e except para tratar exceções

# Try não fucniona sozinho. Precisa do except ou do finally. 
# a = 18
# b = 0
# c = a / b

try:
    a = 18
    b = 0
    # print(b[0])
    #print('Linha 1'[1000])
    c = a / b
except ZeroDivisionError as e:
    print(e)
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error:  # 2 tratamentos numa linha. Não é muito usado
    print('Nome:', error.__class__.__name__)
except Exception:  # Todas as classes de exceção herdam de Exception
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')
print()

# Finally - ele sempre será executado no bloco de código.
print('\n# Finally\n')

try:
    print('ABRIR ARQUIVO')
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
except IndexError as error:
    print('IndexError')
except (NameError, ImportError):
    print('NameError, ImportError')
else:  # muito pouco usado mas existe.
    print('Não deu erro')
finally:
    print('FECHAR ARQUIVO')

print()

print('\n# Raise\n')
# Raise - lançando exceções
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions
def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero')
    return True


def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado.'
        )
    return True


def divide(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceito_zero(d)
    return n / d


print(divide(8, '0'))






