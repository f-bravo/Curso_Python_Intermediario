# Protocolo HTTP (HyperText Transfer Protocol)
# HTTP (HyperText Transfer Protocol) é um protocolo usado enviar e receber
# dados na Internet. Ele funciona no modo cliente/servidor, onde o cliente
# (seu navegador, por exemplo) faz uma requisição ao servidor (site, por exemplo)
# que responde com os dados adequados.
# A mensagem de requisição do cliente deve incluir dados como:
# - O método HTTP
#     - leitura (safe) - GET, HEAD (cabeçalhos), OPTIONS (métodos suportados)
#     - escrita (body)- POST (cria), PUT (substitui), PATCH (atualiza), DELETE
# - O endereço do recurso a ser acessado depois da raiz: Ex:(/users/)
# - Os cabeçalhos HTTP (Content-Type, Authorization) JWT(login)
# - O Corpo da mensagem (caso necessário, de acordo com o método HTTP)
#
# A mensagem de resposta do servidor deve incluir dados como:
# - código de status HTTP (200 success, 404 Not found, 301 Moved Permanently)
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
# - Os cabeçalhos HTTP (Content-Type, Accept)
# - O corpo da mensagem (Pode estar vazio em alguns casos)
"""
Informational responses (100 - 199)
Successful responses (200 - 299)
Redirection messages (300 - 399)
Client error responses (400 - 499)
Server error responses (500 - 599)
"""

# Ao abrir o arquivo index.html ele está em modo FILE.
# Precisa mudar p protocolo http e para isso:
# Digite no terminal o comando:
# -> python -m http.server -d Seção_7_WebScraping 3333
# python -m http.server -d Seção_7_WebScraping + n° da porta 3000
#  Serving HTTP on :: port 3333 (http://[::]:3333/) ...
# Tanto a porta 3333 ou 127.0.0.1:3333 apontam para o localhost
# Agora digite na barra de endereços:
# http://localhost:3333

# Ser a porta estiver sendo usada por outro serviço dará erro.
# Basta mudar a porta. 3001, 3002, 3003, etc.

# Instalar o módulo request
# Ele não vem com o python. Precisa instalar.
# -> pip install requests types-requests

# Quando um site começa com http: quer dizer que ele está rodando na porta 80 
# do serrvidor. Isso é automático.
# https: porta 443 quando não informada
# Não temais navegador. Agora o cliente é o código e o servidor continua o mesmo
# ou qualquer outro site que se´ra o seu servidor.

# Fazendo uma requisição só de leitura. Não precisa do cabeçalho nem do corpo da
# mensagem. 
import requests

url = 'http://localhost:3333/'
response = requests.get(url)

print(response.status_code)
# print(response.headers)
# print(response.content)
# print(response.json()) # Quando a resposta é em Json
print(response.text)
