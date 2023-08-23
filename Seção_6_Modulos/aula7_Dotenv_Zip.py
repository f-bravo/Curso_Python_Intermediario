# Variáveis de ambiente com Python

# Windows Power Shell: $env:VARIAVEL="VALOR" | dir env:
# Linux e Mac: export NOME_VARIAVEL="VALOR" | echo $VARIAVEL

""" 
python-dotenv é uma biblioteca Python que permite que você faça uso de arquivos 
de configuração para armazenar e acessar as suas variáveis de ambiente de forma 
mais fácil e segura em seus projetos.

As variáveis de ambiente são valores que podem ser usados em seu código e que 
podem variar dependendo do ambiente em que o seu código está sendo executado 
(por exemplo, o ambiente de produção ou o ambiente de desenvolvimento).

O python-dotenv funciona lendo o arquivo .env e adicionando as variáveis de 
ambiente ao ambiente do sistema operacional, de forma que elas fiquem 
disponíveis para seu código usando a função os.getenv().
"""

# Para obter o valor das variáveis de ambiente
# os.getenv ou os.environ['VARIAVEL']
# Para configurar variáveis de ambiente
# os.environ['VARIAVEL'] = 'valor'
# Ou usando python-dotenv e o arquivo .env
# pip install python-dotenv
from dotenv import load_dotenv # type: ignore

load_dotenv()
# https://pypi.org/project/python-dotenv/
# OBS.: sempre lembre-se de criar um .env-example
import os

from dotenv import load_dotenv  # type: ignore

load_dotenv()

# print(os.environ) 
print(os.getenv('BD_PASSWORD'))
# Testando: modifique a senha dessa variável de Ambiente

# dotenv:
# O arquivo .env geralmente carrega todas as variáveis de ambiemte.
# Vc ao entrar no programa carrega o arquivo que carrega variáveis de ambiente
# É um arquivo que fica na raiz do programa e não vai p/ nenhum repositório

# Geralmente os projetos tem o arquivo .env-example que é para você copiar e 
# transformar em um .env.
# Basta tirar o -example que ele não será mais trackeado para p github


# -----------------------------------------------------------------------------
# ZIP - Compactando / Descompactando arquivos com zipfile.ZipFile

# -----------------------------------------------------------------------------

import os
import shutil
from pathlib import Path
from zipfile import ZipFile

# Caminhos
CAMINHO_RAIZ = Path(__file__).parent
CAMINHO_ZIP_DIR = CAMINHO_RAIZ / 'aula_7_zip'
CAMINHO_COMPACTADO = CAMINHO_RAIZ / 'aula7_compactado.zip'
CAMINHO_DESCOMPACTADO = CAMINHO_RAIZ / 'aula7_descompactado'
print(CAMINHO_RAIZ) # c:\Python_intermediario\Seção_6_Modulos


# Para apagar as pastas:
# shutil.rmtree(CAMINHO_ZIP_DIR, ignore_errors=True)
# Path.unlink(CAMINHO_COMPACTADO, missing_ok=True)
# shutil.rmtree(str(CAMINHO_COMPACTADO).replace('.zip', ''), ignore_errors=True)
# shutil.rmtree(CAMINHO_DESCOMPACTADO, ignore_errors=True)

# raise Exception()

CAMINHO_ZIP_DIR.mkdir(exist_ok=True)

def criar_arquivos(qtd: int, zip_dir: Path):
    for i in range(qtd):
        texto = 'arquivo_%s' % i
        with open(zip_dir / f'{texto}.txt', 'w', encoding='utf8') as arquivo:
            arquivo.write(texto)


criar_arquivos(5, CAMINHO_ZIP_DIR)

# Criando um zip e adicionando arquivos - compactando:
with ZipFile(CAMINHO_COMPACTADO, 'w') as zip:
    for root, dirs, files in os.walk(CAMINHO_ZIP_DIR):
        for file in files:
            # print(file)
            zip.write(os.path.join(root, file), file) 
            # ,file) para copiar tbm a estrutura das pastas

# Lendo arquivos de um zip
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

# Extraindo arquivos de um zip
with ZipFile(CAMINHO_COMPACTADO, 'r') as zip:
    zip.extractall(CAMINHO_DESCOMPACTADO)

