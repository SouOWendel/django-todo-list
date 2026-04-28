# Django To-Do List

Um aplicativo de Lista de Tarefas (To-Do List) básico desenvolvido em **Django** contemplando autenticação customizada e estilizado com **Tailwind CSS**.

## Módulos do Projeto
- `authenticated/`: Gestão de login e autenticação
- `register/`: Cadastro de novos usuários
- `to_do_lists/`: Gerenciamento das listas de tarefas
- `theme/`: Configuração e estilização usando Tailwind CSS

## Pré-requisitos
Certifique-se de ter o **Python** e o **Node.js** instalados na sua máquina.

## Como iniciar o projeto

### 1. Preparando o Ambiente Python
Crie o ambiente virtual do Python:
```bash
python -m venv env
```

Ative o ambiente virtual:
- **Windows**: `.\env\Scripts\activate`
- **Linux/macOS**: `source env/bin/activate`

### 2. Instalação das Dependências
Instale todas as dependências do projeto através do arquivo `requirements.txt`:
```bash
pip install -r requirements.txt
```

Em seguida, instale as dependências Node do Tailwind pelo próprio CLI do Django:
```bash
python manage.py tailwind install
```

### 3. Banco de Dados
Execute as migrações para criar as tabelas no banco de dados SQLite:
```bash
python manage.py migrate
```

Crie um usuário administrador para acessar a tela do "/admin" se desejar:
```bash
python manage.py createsuperuser
```

### 4. Executando a Aplicação
Para que o serviço funcione de forma completa com estilo e servidor base, abra duas janelas do terminal (com o ambiente `env` ativo em ambas):

**No Terminal 1**, inicie o servidor local:
```bash
python manage.py runserver
```

**No Terminal 2**, inicie o auto-reload do Tailwind CSS:
```bash
python manage.py tailwind start
```

Acesse a aplicação operando no seu navegador acessando: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)