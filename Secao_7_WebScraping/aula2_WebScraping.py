# + Web Scraping com Python usando requests e bs4 BeautifulSoup
# - Web Scraping é o ato de "raspar a web" buscando informações de forma
# automatizada, com determinada linguagem de programação, para uso posterior.
# - O módulo requests consegue carregar dados da Internet para dentro do seu
# código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML
# em formato de objetos Python para facilitar a vida do desenvolvedor.
# - Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
# + Instalação
# - pip install requests types-requests bs4

import re

import requests
from bs4 import BeautifulSoup

url = "http://localhost:3333/"
response = requests.get(url)
raw_html = response.text  # html cru
parsed_html = BeautifulSoup(raw_html, "html.parser")  # html convertido em obj python

# retornando o título - colocando .text no final retorna sem as TAGs
print(parsed_html.title.text)  # retorna mais de uma coisa. TAG ou None. Má 
# programação. Sempre que desenvolver algo q outros vão usar: 
# Retorne uma coisa ou levante uma exceção para o .text deixar de ficar vermelho
#, tem que fazer uma condição: if...

if parsed_html.title is not None:
    print(parsed_html.title.text)

# -----------------------

# clicando com botão direito inspecionar na parte TOP 3 JOBS do site

# novamente:
# clique com botão direito na TAG h2 TOP 3 jobs:
# COPY + selector - vai copiar o seletor CSS desse local
""" foi copiado -->:  #intro > div > div > article > h2"""
# select_one para selecionar uma coisa:  Um título

top_jobs_heading = parsed_html.select_one("#intro > div > div > article > h2")

if top_jobs_heading is not None:
    print(top_jobs_heading.text)  # TOP 3 jobs

# pegando o (PAI), o elemento acima dele, que sustenta ele que é o article
if top_jobs_heading is not None:
    article = top_jobs_heading.parent
    print(article)
    # Pegando os <p> parágrafos dentro da tag article
    if article is not None:
        for p in article.select("p"): # seleciona todas as tags <p>
            print(re.sub(r"\s{1,}", " ", p.text).strip())

# Para remover os espaços em branco do html precisa usar expressões regulares
# import re
# substituindo espaçoes maior que dois para apenas um espaço
# strip( para cortar espaços do começo e final da string)
"""print(re.sub(r'\s{1,}', ' ', p.text).strip())"""

# WEB SCRAPING
# Acessar o site, pegar o HTML, converter o HTML e transformar em objetos e usar
# o html(objeto) dentro do código p fazer alguma coisa.
