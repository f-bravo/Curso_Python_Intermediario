# Comandos:

# ------------------------------------------------------

"""
# Iniciando o projeto: 
# Criando o ambiente virtual:
-> python -m venv venv
# Ativando oambiente virtual no Windows 
-> . venv\Scripts\Activate
# Atualizar o pip
-> pip install --upgrade pip
"""

#--------------------------------------------------------
# Configurando o git ignore --> arquivos que não vão para o repositório
"""
crei o .gitignore na raiz do projeto 
busque no google --> django gitignore 
https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/
Cole os comandos dentro da pasta .gitignore
"""

"""
# inicie o git dentro do projeto:
# -> git init

# se já criou um usuário globa não precisa executar o comando p nome e e-mail 
# ---------------------------------------------------------------------------
# Criando nome de usuário: git
-> git config --global user.name 'nome'
# Configurando email:
-> git config --global user.email 'email@email.com'
# ---------------------------------------------------------------------------

-> git status - ver as modificações feitas até aqui.

# Olhando as configurações do GIT:
-> git config --global
# Eu não alterei 0 defaultBranch para main - deixei como master
# estava dando erro na hora de dar o push


# Adicioanando:
-> git add .
-> git commit -m 'Initial'

# dando um git log - para ver o que foi feito:
# -> git log --oneline
# R: ..... (HEAD -> master) Initial

# Crie o repositório no perfil do github
Adicionando o repositório remoto: 
copie a chave https e dê o seguinte comando:
-> git remote add origin chave_http

# Enviando os commites: 
-> git push origin master

#------------------------------------------------------

# Sempre que modificar um arquivo ou vários tem que repetir o processo:

-> git add . (ou) git add nome_do_arquivo
-> git commit -m 'explicação'
-> git push origin master
# ------------------------------------------------------------

# OBS na próxima vez pode setar (-u) o nome para digitar apenas git push:
-> git push origin master -u
"""




















