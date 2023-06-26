# Escopo de função:
# Escopo significa o local onde aquele código pode atingir.
# existe o escopo local e global
# Global: é o escopo onde todo o código é alcançável
# local: é o escopo onde apenas nomes de mesmo local podem ser alcaçados

def escopo():
    x = 1
    print(x)

# print(x) # 'x' is not define - fora da função n tem acesso a X
escopo()
# mas de definir a variável como global ela poderá ser acessada.

x = 1

def escopo2():
    def escopo_interno():
        y = 2
        print(x, y)
    # print(y) aqui não da para acessar 'Y' in not define. Y é do escopo_interno()
    
    escopo_interno() # p/ executar a função interna precisa chamar ela na 'externa'
    print(x) # 1

escopo2() # 1, 2

# Só é possível acessar as variáveis dos escopos de cima. Mas não pdoe acessar dos
# escopos internos. É o caso do Y. Ele só pode ser acessado no escopo_interno.

# Veja a mesma função abaixo:
# Ela tem o mesmo nome da variável X porém ela usa a variável do escopo da função

def escopo3():
    x = 10
    def escopo_interno2():
        y = 2
        print(x, y)
    
    escopo_interno2()
    print(x) # 10

escopo3() # 10, 2
print(x) # 1 -> X fora do escopo continua sendo X


# É como aquela boneca Russa que vc tira uma de dentro da outra. A mais interna tem
# o escopo mais fechado.
def escopo4():
    x = 10
    def escopo_interno3():
        x = 100
        y = 2
        print(x, y) # 100, 2
    
    escopo_interno3()
    print(x) # 10

escopo4() 
print(x) # 1
print('\n-----------')
# se quiser o X global internamente na função, basta declarar como global. global x

def escopo5():
    global x
    def escopo_interno4():
        x = 100
        y = 2
        print(x, y) # 100, 2
    
    escopo_interno4()
    print(x) # 1 -> agora o x do escopo5 é o global

escopo4() 
