Para acessar a env do projeto.
.\env\Scripts\activate

Para instalar o Django
pip install django

Para criar o projeto em Django dentro do root do repositório.
django-admin startproject to_do_list .

O módulo **os** no Python é uma biblioteca padrão que permite interagir com o sistema operacional hospedeiro (Windows, Linux, macOS) de forma portátil. Ele possibilita manipular arquivos e diretórios (criar, listar, remover), gerenciar caminhos, ler variáveis de ambiente e executar comandos do terminal diretamente pelo Python.

Para executar um servidor de desenvolvimento do Django: python manage.py runserver

Pode-se utiliza a extensão Database Client para gerenciar as tabelas do SGBD SQLite.

Neste projeto para criar um APP, usa-se python manage.py startapp (nome do projeto)

Para iniciar o servidor Django: python manage.py runserver
Para iniciar o Tailwind Watcher: python manage.py tailwind start

python manage.py makemigrations
Migration é uma migração da model para tabela de banco de dados, primeiro você cria as migrations e depois você executa a migrate, transformando as classes criadas em tabelas no banco de dados.

python manage.py migrate
Esse comando faz a criação das tabelas através das migrations.

python manage.py createsuperuser
Para criar um super usuário que tem todas as permissões para o banco de dados. Ao criar utilizando este comando, já é utilizado criptografia.

Para senha, uma hash criptografada é gerada, e as senhas para autenticação são comparadas com essa hash. Se o banco for invadido, as senhas serão apenas hashs.