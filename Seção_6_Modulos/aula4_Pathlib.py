# Pathlib - usada em algo relacionado com caminhos no sistema operacional

# O objetivo é evitar escrever caminhos de forma hardcode pois isso não roda de
# forma igual em todos os sistemas operacionais

from pathlib import Path

# Pegando a pasta do projeto.
caminho_aula4 = Path()

print(caminho_aula4) # caminho relativo --> . retorna um ponto
print(caminho_aula4.absolute()) # caminho absoluto 
# C:\Python_intermediario

# Pegando o caminho do arquivo atual aula4_Pathlib.py
caminho_arquivo = Path(__file__)
print(caminho_arquivo)
# c:\Python_intermediario\Seção_6_Modulos\aula4_Pathlib.py

# Para pegar o caminho da pasta Seçã_6 que é o "pai" do caminho_arquivo:
print(caminho_arquivo.parent) 
# c:\Python_intermediario\Seção_6_Modulos

print(caminho_arquivo.parent.parent)
# c:\Python_intermediario
# parent: sempre retorna uma pasta a cima ou p trás. 

# Criando um caminho:
# / = truediv - junta caminhos
novo_caminho = caminho_arquivo.parent / 'aula4_testando'
print(novo_caminho)
# c:\Python_intermediario\Seção_6_Modulos\aula4_testando

# Tudo isso feito em memória. Apenas gera os caminhos.
print('----------------------------------------------------')

# Para pegar a home:
print(Path.home()) # C:\Users\bravo

arquivo1 = Path.home() / 'arquivo_teste.txt'
print(arquivo1) 
# C:\Users\bravo\arquivo_teste.txt

# Para salvar o arquivo:
arquivo1.touch()

# Para escrever: feito p coisa rápida - sempre sobrescreve a anterior 
arquivo1.write_text('Olá Bravo')

# Para ler:
print(arquivo1.read_text()) # Olá Bravo

# Para apagar o arquivo:
# arquivo1.unlink()
print('----------------------------------------------------')

# Para salvar mais de uma linha por exemplo sem apagar o último save:

arquivo2 = Path.home() / 'arquivo_teste2.txt'
with arquivo2.open('a+') as file:
    file.write('Linha 1 testando\n')
    file.write('Linha 2 testando novamente\n')

print(arquivo2.read_text())
print('----------------------------------------------------')

pasta_teste = Path.home() / 'Python_teste_23'
pasta_teste .mkdir(exist_ok=True)

arquivo3 = Path.home() / 'Python_teste_23' / 'subpasta_teste'
arquivo3.mkdir(exist_ok=True)

arquivo_subpasta = arquivo3 / 'testa_subpasta1.txt'
arquivo_subpasta.touch()
arquivo_subpasta.write_text('Testando criação de arquivo na subpasta')

# Para apagar arquivos e pastas:
# Só pode ser apagada de fora recursiva. 
# Pode ser feito usando shutil ou os.walk feito na aula 2 por exemplo.

# Criando uma subpasta dentro de Python_teste_23 para apagar de forma recursiva:

# Dentro de qualquer Path tem como saber se é um arquivo, diretório e se existe:
# file.is_file() True ou False para todos
# file.is_dir()
# file.exist()

# Touch() é usado para atualizar a última vez que foi modificado
arquivo4 = Path.home() / 'Python_teste_23' / 'subpasta_temporaria'
arquivo4.mkdir(exist_ok=True)

for i in range(10):
    file = arquivo4 / f'file_{i}.txt'
    file.touch()

    if file.exists():
        file.unlink() # se existir apague
    else:
        file.touch() # se não crie   

    with file.open('a+') as texto:
        texto.write('Texto linha 1\n')
        texto.write(f'file_{i}.txt')

# Usando o rmtree para apagar:
from shutil import rmtree
# rmtree(arquivo4) 

# Usando recursão para apagar os arquivos da pasta: arquivo4
# A função vai receber um caminho e vai iterar dentro da pasta - apenas o conteúdo
# glob('*') apagar tudo*
# Sempre que for um diretório a função chama a recursividade para chegar no 
# arquivo que está dentro do diretório e apagar com o rmtree()
def rmtree(root: Path, remove_root=True):
    for file in root.glob('*'):
        if file.is_dir():
            print('DIR:', file)
            rmtree(file, False)
            file.rmdir()  
        else:
            print('FILE:', file)
            file.unlink()      
    
    if remove_root: 
        root.rmdir()  # Remove a pasta

rmtree(arquivo4)