# Closure e funções que retornam outra funções

# vc adia a execução da função interna para que force o Python a salvar
# o resultado da função que foi adiada na memória.


def criar_saucacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar  # não colocando os parênteses() força o adiamento

bom_dia = criar_saucacao('Bom dia')
boa_noite = criar_saucacao('Boa noite')

print(bom_dia('Bravo'))
print(boa_noite('Bravo'))
print('---------------------')

for nome in ['Maria', 'juliana', 'Bravo']:
    print(bom_dia(nome))

for nome in ['Maria', 'juliana', 'Bravo']:
    print(boa_noite(nome))


# Exercício: crie função que duplicam, triplicam e quadruplicam o número
# recebido como parâmetro


def criar_multiplicador(multiplicador):  # recebe o multipliador
    def multiplicar(numero):             # recebe o número
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)
# Foi adiado passar o parâmetro número
print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))




