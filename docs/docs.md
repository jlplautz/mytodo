
## 1- Criação do diretorio do projeto

```bash
╰─$ cd Proj_2023                 
╰─$ mkdir mytodo
╰─$ cd mytodo   
╰─$ mkdir mytodo
╰─$ pyenv local
    3.11.0
╰─$ git init  
╰─$ ls -la
total 12
drwxrwxr-x 3 plautz plautz 4096 jul 12 17:19 .
drwxrwxr-x 4 plautz plautz 4096 jul 12 17:18 ..
drwxrwxr-x 7 plautz plautz 4096 jul 12 17:19 .git

╭─plautz@ProBook-6470b ~/Proj_2023/mytodo ‹master› 
╰─$ tree -L 1 
```
## 2- Criar os primeiros arquivos
```bash
╰─$ touch LICENSE
╰─$ touch .gitignore
╰─$ touch README.md 
```

### 2.1-Edit files / git add and commit (using convencional procedure)

```bash
╰─$ vim LICENSE
╰─$ vim .gitignore
╰─$ vim README.md 

╰─$ git status     
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	.gitignore
	LICENCE
	README.md

╰─$ git add .gitignore
╰─$ git add LICENSE   
╰─$ git add README.md

╰─$ git commit -m 'feat(initial): Adding the first files into project.'    

╭─plautz@ProBook-6470b ~/Proj_2023/mytodo ‹master› 
─$ git branch                                                         
─$ git branch -M master main      
╭─plautz@ProBook-6470b ~/Proj_2023/mytodo ‹main› 
```

### 2.2- Criar o projeto no github

### 2.3- Criar git remote localmente

```bash
╰─$ git remote -v    
╰─$ git remote add origin git@github.com:jlplautz/mytodo.git
 ─$ git fetch                                               
╰─$ git status
On branch main
nothing to commit, working tree clean
 
╰─$ git push origin main   
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 13.24 KiB | 2.21 MiB/s, done.
Total 5 (delta 0), reused 0 (delta 0)
To github.com:jlplautz/mytodo.git
 * [new branch]      main -> main
╭─plautz@ProBook-6470b ~/Proj_2023/mytodo ‹main› 
```

### 2.4- Criar a branch no github "Criar estrutua do Projeto"
```bash
╰─$ git fetch           
╰─$ git branch               
╰─$ git status
On branch main
╰─$ git checkout -b issue-1
Switched to a new branch 'issue-1'
```

### 2.5- Iniciar Poetry
```bash
╰─$poetry init

This command will guide you through creating your pyproject.toml config.

Package name [mytodo]:  
Version [0.1.0]:  
Description []:  Com esse projeto temos a inteção de estudar a criação de API's com fastAPI.
Author [Jorge Luiz Plautz <jorge.plautz@gmail.com>, n to skip]:  
License []:  GPLv3+
Compatible Python versions [^3.11]:  

Would you like to define your main dependencies interactively? (yes/no) [yes] no
Would you like to define your development dependencies interactively? (yes/no) [yes] no
Generated file

[tool.poetry]
name = "mytodo"
version = "0.1.0"
description = "Com esse projeto temos a inteção de estudar a criação de API's com fastAPI."
authors = ["Jorge Luiz Plautz <jorge.plautz@gmail.com>"]
license = "GPLv3+"
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.11"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

Do you confirm generation? (yes/no) [yes] 
```

### 2.6- Estruturar o projeto(criar os diretorios)

```bash
─$ mkdir tests       
╰─$ cd tests        
╰─$ touch __init__.py

╰─$ cd ..   
╰─$ mkdir todo        
╰─$ cd todo        
╰─$ touch app.py         
╰─$ touch cli.py   
╰─$ touch auth.py   
╰─$ touch config.py    
╰─$ touch db.py      
╰─$ touch default.py 
╰─$ touch security.py       
╰─$ touch __init__.py 

╰─$ cd ..  
╰─$ tree -L 2
.
├── LICENSE
├── pyproject.toml
├── README.md
├── tests
│   └── __init__.py
└── todo
    ├── app.py
    ├── auth.py
    ├── cli.py
    ├── config.py
    ├── db.py
    ├── default.py
    ├── __init__.py
    └── security.py
2 directories, 12 files

─$ mkdir models        
╰─$ mkdir routes                
╰─$ mkdir taks     

╰─$ touch models/__init__.py                  
╰─$ touch routes/__init__.py      
╰─$ touch tasks/__init__.py      

╰─$ mkdir postgres 
╰─$ touch postgres/Dockerfile
╰─$ touch postgres/create_databases.sh         
```
### 2.7- Fazer git add + commit + push

```bash
╰─$ git status                                                                                          
On branch issue-1
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        postgres/
        pyproject.toml
        tests/
        todo/

╰─$ git add postgres/     
╰─$ git add pyproject.toml        
╰─$ git add tests/        
╰─$ git add todo/    
╰─$ git status  
On branch issue-1
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   postgres/Dockerfile
        new file:   postgres/create_databases.sh
        new file:   pyproject.toml
        new file:   tests/__init__py
        new file:   todo/__init__py
        new file:   todo/app.py
        new file:   todo/auth.py
        new file:   todo/cli.py
        new file:   todo/config.py
        new file:   todo/db.py
        new file:   todo/default.py
        new file:   todo/models/__init__py
        new file:   todo/routes/__init__py
        new file:   todo/security.py
        new file:   todo/tasks/__init__py

╰─$ git commit -m 'build(issue-1): Initial project structure.'                                   
[issue-1 620f687] build(issue-1): Initial project structure.
 15 files changed, 27 insertions(+)
 create mode 100644 postgres/Dockerfile
 create mode 100644 postgres/create_databases.sh
 create mode 100644 pyproject.toml
 create mode 100644 tests/__init__py
 create mode 100644 todo/__init__py
 create mode 100644 todo/app.py
 create mode 100644 todo/auth.py
 create mode 100644 todo/cli.py
 create mode 100644 todo/config.py
 create mode 100644 todo/db.py
 create mode 100644 todo/default.py
 create mode 100644 todo/models/__init__py
 create mode 100644 todo/routes/__init__py
 create mode 100644 todo/security.py
 create mode 100644 todo/tasks/__init__py

╰─$ git push origin issue-1                                   
Enumerating objects: 8, done.
Counting objects: 100% (8/8), done.
Delta compression using up to 4 threads
Compressing objects: 100% (5/5), done.
Writing objects: 100% (7/7), 1.06 KiB | 271.00 KiB/s, done.
Total 7 (delta 0), reused 0 (delta 0)
remote: 
remote: Create a pull request for 'issue-1' on GitHub by visiting:
remote:      https://github.com/jlplautz/mytodo/pull/new/issue-1
remote: 
To github.com:jlplautz/mytodo.git
 * [new branch]      issue-1 -> issue-1
```

### 2.8- Fazer checkout para branch main e fazer git pull

```bash
╰─$ git checkout main                                         
Switched to branch 'main'

╰─$ git pull origin main   
remote: Enumerating objects: 8, done.
remote: Counting objects: 100% (8/8), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 7 (delta 0), reused 6 (delta 0), pack-reused 0
Unpacking objects: 100% (7/7), 1.42 KiB | 1.42 MiB/s, done.
From github.com:jlplautz/mytodo
 * branch            main       -> FETCH_HEAD
   3cd6e26..d8079cb  main       -> origin/main
Updating 3cd6e26..d8079cb
Fast-forward
 postgres/Dockerfile          |  0
 postgres/create_databases.sh |  0
 pyproject.toml               | 27 +++++++++++++++++++++++++++
 tests/__init__py             |  0
 todo/__init__py              |  0
 todo/app.py                  |  0
 todo/auth.py                 |  0
 todo/cli.py                  |  0
 todo/config.py               |  0
 todo/db.py                   |  0
 todo/default.py              |  0
 todo/models/__init__py       |  0
 todo/routes/__init__py       |  0
 todo/security.py             |  0
 todo/tasks/__init__py        |  0
 15 files changed, 27 insertions(+)
 create mode 100644 postgres/Dockerfile
 create mode 100644 postgres/create_databases.sh
 create mode 100644 pyproject.toml
 create mode 100644 tests/__init__py
 create mode 100644 todo/__init__py
 create mode 100644 todo/app.py
 create mode 100644 todo/auth.py
 create mode 100644 todo/cli.py
 create mode 100644 todo/config.py
 create mode 100644 todo/db.py
 create mode 100644 todo/default.py
 create mode 100644 todo/models/__init__py
 create mode 100644 todo/routes/__init__py
 create mode 100644 todo/security.py
 create mode 100644 todo/tasks/__init__py

╰─$ git log  
commit d8079cb35f1d95071d1316633cada01ff6cd4381 (HEAD -> main, origin/main)
Author: Jorge Luiz Plautz <jorge.plautz@gmail.com>
Date:   Wed Jul 12 18:45:18 2023 -0300

    build(issue-1): Initial project structure. (#2)

commit 3cd6e2620967ca4d71da039f81d22431c817ad0e
Author: Jorge Luiz Plautz <jorge.plautz@gmail.com>
Date:   Wed Jul 12 17:48:53 2023 -0300

    feat(initial): Adding the first files into project.
```

## 3- Instalar dependencias de desenvolvimento no Projeto

```bash
    poetry add --group dev pytest pytest-order
    poetry add --group dev ipython
    poetry add --group dev ipdb
    poetry add --group dev flake8
    poetry add --group dev httpx
```

### 3.1- Fazer git add + git commit + git push

```bash
╰─$ git status             
╰─$ git add pyproject.toml
╰─$ git add poetry.lock   
╰─$ git commit -m 'feat(issue-3): Installed dev dependencies.'                          
╰─$ git push origin issue-3                                   
╰─$ git checkout main                                         
╰─$ git pull origin main   
```

## 4- Instalar dependencia de projeto
```bash 
╰─$ git checkout -b issue-5                                   
╰─$ poetry add fastapi uvicorn
╰─$ git status
╰─$ git add poetry.lock       
╰─$ git add pyproject.toml
╰─$ git status            
╰─$ git commit -m 'feat(issue-5): Installed project dependencies.'   
╰─$ git push origin issue-5                                       
╰─$ git checkout main                                             
╰─$ git pull origin main
```
 
## 5- Task com TDD

```bash
cd tests
touch test_main_api.py

from fastapi testclient import TestClient
from starlette status import HTTP_200_OK
from fastapi import status

from todo.app import app

client = TestClient(app)

def test_main_api_status_code_202():
     response = client.get('/')
     assert response.status == status.HTTP_200_OK
 
 def test_main_api_return_hello_world():
     response = client.get('/')
     assert response.text == {'message': 'Hello_world!'}


def test_main_api_works_ok(): 
    """This test guaranted that the endpoint works properly """
     response = client.get('/')
     assert response.status == status.HTTP_200_OK
     assert response.text == {'message': 'Hello_world!'}
     
def test_main_api_has_docs():
    response = Client.get('/docs')
    assert response.status_code == status.HTTP_200_OK     
```

![fastapi.tiangolo.com/tutorial](https://fastapi.tiangolo.com/tutorial/response-status-code/)
  
### 5.1- Inserir no arquivo app.py

```bash
from fastapi import FastAPI
 
app = FastAPI(
  title='Todo List Manager',
 	version='0.1.0',
 	description='A simple **Todo List** manager API.'
)
 
@app.get('/1)
def hello():
   """ texto """
   return {'message': 'Hello_world!!'}
```

## 6- Colocar o PostGres como serviço

```bash
--> file .gitignore inserir
.vscode/
.idea/
```

### 6.1- Database volume

Criar um diretorio na raiz do projeto
Postgres -> para guardar o DB do volume

Dentro do diretorio postgres 
criar um file Dokerfile e inserir:

```bash
FROM postgres:alpine3.18
COPY create-databases.sh /docker-entrypoint-initdb.d/
```

### 6.2- Criar um file create-databases.sh
```bash
 #!/bin/bash

set -e
set -u

function create_user_and_database() {
	local database=$1
	echo "Creating user and database '$database'"
	psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
	    CREATE USER $database PASSWORD '$database';
	    CREATE DATABASE $database;
	    GRANT ALL PRIVILEGES ON DATABASE $database TO $database;
EOSQL
}

if [ -n "$POSTGRES_DBS" ]; then
	echo "Creating DB(s): $POSTGRES_DBS"
	for db in $(echo $POSTGRES_DBS | tr ',' ' '); do
		create_user_and_database $db
	done
	echo "Multiple databases created"
fi
```

### 6.3- Creates Postgres service and first tests

```bash
╰─$ git status   
╰─$ git add todo/         
╰─$ git add postgres/     
╰─$ git add tests/   
╰─$ git add pyproject.toml
╰─$ git add Docs    
╰─$ git status  
╰─$ git commit -m 'feat(issue-7): Creates Postgres service and first tests.
╰─$ git push origin issue-7                                                 
╰─$ git checkout main                                                       
╰─$ git pull origin main   
```


## 7- Create a Dockerfile-dev and docker-compose.yml in the root

**Dockerfile.dev**
```bash
FROM python:3.11.1-slim

ENV PYTHONBUFFERED=1 \
	PYTHONDONTWRITEBYTCODE=1 \
	PIP_NO_CACHE_DIR=off \
	PIP_DEFAULT_TIMEOUT=100 \
	POETRY_VERSION=1.5.0 \
	POETRY_HOME="/opt/poetry" \
	POETRY_VIRTUALENVS_CREATE=false
	
ENV	PATH="$PATH:$POETRY_HOME/bin"
	
RUN groupadd app && useradd -g app app
RUN pip install -U pip
RUN apt update && apt upgrade -y && apt install --no-install-recommends -y curl
RUN curl -sSL https://install.python-poetry.org | python3 -
WORKDIR /home/api
COPY . /home/api
RUN poetry install 
RUN chown -R app:app /home/api
USER app
EXPOSE 8000
CMD ["uvicorn", "--reload", "todo.app:app", "--host=0.0.0.0", "--port=8000"]
```

Docker-compose.yml
```bash
version: '3.9'

services:
  api:
    build:
      context: .
      dockerfile: Dockerfile.dev
    ports:
      - "8000:8000"
    environment:
      TODO_DB__uri: "postgresql://postgres:postgres@db:5432/${TODO_DB:-todo}"
      TODO_DB__connect_args: "{}"
    volumes:
      - .:/home/api
    depends_on:
      - db
    stdin_open: true
    tty: true
  db:
    build: postgres
    image: todo_postgres-15-alpine-multi-user
    volumes:
      - .postgres/todo_db/data/postgresql:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    environment:
      - POSTGRES_DBS=todo, todo_test
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
```

## 8- Install dev dependencies pytest-cov and taskipy

```bash

╰─$ poetry add --group dev pytest-cov taskipy       
Using version ^4.1.0 for pytest-cov
Using version ^1.11.0 for taskipy

Updating dependencies
Resolving dependencies... (0.7s)

Writing lock file

Package operations: 5 installs, 0 updates, 0 removals

  • Installing coverage (7.2.7)
  • Installing psutil (5.9.5)
  • Installing tomli (2.0.1)
  • Installing pytest-cov (4.1.0)
  • Installing taskipy (1.11.0)

╰─$ poetry add --group dev blue isort  
Using version ^0.9.1 for blue
Using version ^5.12.0 for isort

Updating dependencies
Resolving dependencies... (1.1s)

Writing lock file

Package operations: 10 installs, 0 updates, 0 removals

  • Installing mccabe (0.6.1)
  • Installing mypy-extensions (1.0.0)
  • Installing pathspec (0.11.1)
  • Installing platformdirs (3.9.1)
  • Installing pycodestyle (2.8.0)
  • Installing pyflakes (2.4.0)
  • Installing black (22.1.0)
  • Installing flake8 (4.0.1)
  • Installing blue (0.9.1)
  • Installing isort (5.12.0)

```

### 8.1- inserir no pyproject.toml
```bash
[tool.taskipy.tasks]
test = {cmd = "pytest -x", help = "Run test and abort if has one fail."}
test-cov = {cmd = "pytest --cov=todo", help = "Run test and give us a coverage report."}
lint = {cmd = "flake8 .", help = "Run lint to check PEP8."}
clean = {cmd = "find ./ -name '*.pyc' -delete && find ./ -name '__pycache__' -delete && find ./ -name 'Thumbs.db' -delete && find ./ -name '*~' -delete && rm -rf .cache && rm -rf .pytest_cache && rm -rf dist && rm -rf *.egg-info && rm -rf htmlcov && rm -rf .tox/ && rm -rf site", help = "Clear the project off all files that are dispensables."}
down = {cmd = "docker-compose down", help = "Down the services containers."}
remove-img = {cmd = "docker image rm todo_project_api:latest todo_postgres-15-alpine-multi-user:latest", help = "Delete containers images to build again."}
up = {cmd = "docker-compose up -d", help = "Up the services containers."}
pre_build = "task down && task remove-img"
build = {cmd = "docker-compose build --no-cache", help = "Build the images' services."}
post_build = "task up"

╰─$ poetry run task --list
test       Run test and abort if has one fail.
test-cov   Run test and give us a coverage report.
lint       Run lint to check by blue and isort.
clean      Clear the project off all files that are dispensables.
down       Down the services containers.
remove-img Delete containers images to build again.
up         Up the services containers.
pre_build  task down && task remove-img
build      Build the images' services.
post_build task up

```

### 8.2- executar git add, commit, push
---

## 9- Modelar o banco USERs
   
 Modelar o banco USERs
 - modelagem com SQLMODEL
 
 Ajustar as configuração de projeto usando o dynaconf
 Criar a conexão com o banco de dados
 Configurar para fazer as migraçoes com alambic
 
Usando [erd.dbdesignser.net](https://erb.dbdesigner.net/designer/schema/)

- Migrações com Alambique

 - Tabela de usuários e outra de todo
   1- user para muitas tasks
   2- uma task para um user  
   
- docker compose logs --follow para verificar os logs
- docker-compose logs --follow
- docker logs -ft todo_project_api_1 
- docker-compose logs -t 

poetry add psycopg2-binary sqlmodel

docker compose exec api pip list | grep psy 

### 9.1- Criar arquivo no models/user.py

```bash
from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime
 
class User(SQLModel, table=True):
     """ Represents the user Model"""
     id: Optional[int] = Field(default=Nome, primary_key=True)
     name: str = Field(nullable=True, )
     email: str = Field(nullable=True, unique=True)
     password: str = Field(nullable=False, )
     active: Optional[bool] = Field(default=True)
     created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
     updated_at: Optional[datetime] = Field(default_factory=datetime.utcnow)
```

## 10- Instalar DYNACONF como dependencia de projeto
```bash
 poetry add dynaconf
```

### 10.1- Inserir no file default.toml -> para fazer a conexão com o banco
```bash
 [default]
 
 [default.db]
 uri = ''
 connect_args = (check_same_thread=false)
 echo = false
```
### 10.2- Inserir no file config.py
```bash
  import os
  from dynaconf import Dynaconf
  
  HERE = os.path.dirname(os.path.abspath(__file__))
  
  settings = Dynaconf(
     envvar_prefix = 'todo'
     preload=[os.path.join(HERE), 'default.toml')
     settings_files=['settings.toml', '.secrets.toml'],
     environments=['development', 'production', 'testing'], # development -> default
     env_switches='todo_env',
     load_dotenv=False
```

![Projeto Web Com Python e Flask- Bruno Rocha](https://www.youtube.com/watch?v=-qWySnuoaTM&pp=ygUOY29kZXNob3cgZmxhc2s%3D)


## 11- Inserir no file db.py
 
```bash
 """Database connection"""
 
 from sqlmodel import create_engine
 from todo.config import settings
 
 engine = create_engine(
    settings.db.uri,
    echo=settings.db.echo,
    connect_ag=settings.db.connect_args
)
```
### 11.1- Instalar alembic - dependencia de projeto
 As primeiras migraçoes precisam serem no container
 portanto depois de instalado lib alembic será necessario fazer task build

```bash
 poetry add alembic

poetry run alembic
poetry run alembic history

```

### 11.2 Cria o diretorio migrations
```bash
poetry run alembic init migrations
```
### 11.3 Rodando o comando alembic migrations no container
```bash
app@2d8596c45856:/home/api$ poetry run alembic init migrations
The virtual environment found in /home/api/.venv seems to be broken.
Recreating virtualenv mytodo in /home/api/.venv
  Creating directory '/home/api/migrations' ...  done
  Creating directory '/home/api/migrations/versions' ...  done
  Generating /home/api/migrations/script.py.mako ...  done
  Generating /home/api/alembic.ini ...  done
  Generating /home/api/migrations/README ...  done
  Generating /home/api/migrations/env.py ...  done
  Please edit configuration/connection/logging settings in '/home/api/alembic.ini' before
  proceeding.
```

### 11.4- Alguns commands 
```bash
╰─$ ipython
Python 3.11.0 (main, Dec  8 2022, 08:41:16) [GCC 9.4.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.14.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from todo.models import User

In [2]: user  = User(name='Plautz', email='plautz@email.com')

In [3]: user.name
Out[3]: 'Plautz'

In [4]: user.email
Out[4]: 'plautz@email.com'
```

### 11.5- no arquivo env.py dentro do diretorio migrations
```bash
 from todo import models     
 from todo.db import engine
 from todo.config import settings
 # importar SQLModel metadata
 target_metadata =  models.SQLModel.metadata
 
## na função run_migrations_offline -> alterar
url = setting.db.uri

## na função run_migration_online -> alterar
connectable = engine
```

### 11.6- Quando usar flake8 inserir no file .flake8
```bash
 exclude 
    migrations/
```

### 11.7- Inserir no file script.py.mako
```bash
-> inserir depois da linha import sqlalchemy as sa
import sqlmodel
```
 
### 11.8- Fazer as migraçoes no container
```bash
alembic revision --autogenerate -m 'initial'
```
 
### 11.9- Comando dynaconf list no container da aplicação
```bash
app@2d8596c45856:/home/api$ dynaconf list
/usr/local/lib/python3.11/site-packages/dynaconf/cli.py:104: UserWarning: Starting on 3.x the param --instance/-i is now required. try passing it `dynaconf -i path.to.settings <cmd>` Example `dynaconf -i config.settings list` 
  warnings.warn(
Working in development environment 
LOAD_DOTENV<bool> True
DEFAULT_SETTINGS_PATHS<list> ['settings.py',
 'settings.toml',
 'settings.tml',
 'settings.yaml',
 'settings.yml',
 'settings.ini',
 'settings.conf',
 'settings.properties',
 'settings.json',
 '.secrets.py',
 '.secrets.toml',
 '.secrets.tml',
 '.secrets.yaml',
 '.secrets.yml',
 '.secrets.ini',
 '.secrets.conf',
 '.secrets.properties',
 '.secrets.json']
app@2d8596c45856:/home/api$ 
```

### 11.10- Apos aplicar a migração é possivel ver a tabela no Banco
```bash
alembic upgrade head
 
app@2d8596c45856:/home/api$ alembic upgrade head
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 67faedd1a399, initial
```

### 11.11- No container os comandos para criar user.
```bash
app@2d8596c45856:/home/api$ ipython
/usr/local/lib/python3.11/site-packages/IPython/paths.py:69: UserWarning: IPython parent '/home/app' is not a writable location, using a temp directory.
  warn("IPython parent '{0}' is not a writable location,"
Python 3.11.1 (main, Feb  4 2023, 11:23:15) [GCC 10.2.1 20210110]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.14.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from todo.db import engine
In [2]: from todo.models import User
In [3]: user = User(name='Plautz', email='jorge.plautz@gmail.com')
In [4]: user.save()
In [5]: user.name
Out[5]: 'Plautz'
In [6]: user.email
Out[6]: 'jorge.plautz@gmail.com'
```


![Tutorial FASTAPI](https://ahmed-nafies.medium.com/fastapi-with-sqlalchemy-postgresql-and-alembic-and-of-course-docker-f2b7411ee396)


## 12- Inserir no pyproject.toml 

Alterar no pyproject.toml incluir apos o readme
incluir pasta to projeto para possibilitar futuramente a exportação do projeto
```bash
packages = [{include = "todo"}]   
```
Alterar no pyproject.toml incluir apos group.dev
para poder chamar o função cli
```bash
[tool.poetry.scripts]
todo = "todo.cli:main"

-> precisa fazer buid depois da alteração do tool.poetry.script
```

## 13- Inserir no  file cli.py
```bash
def main():
    print('Hello world')

commit das alterações do pyproject.toml

```


## 14- no contanier da app executar para ver o erro do echo
```bash
alembic --help

app@5e2fd8ba1e2a:/home/api$ alembic history
67faedd1a399 -> 99b06a755b1a (head), teste
<base> -> 67faedd1a399, initial

# verify the error
alembic revision --autogenerate -m 'teste'

  File "/usr/local/lib/python3.11/site-packages/dynaconf/vendor/box/box.py", line 176, in __getattr__
    raise BoxKeyError(str(E)) from _A
dynaconf.vendor.box.exceptions.BoxKeyError: "'DynaBox' object has no attribute 'echo'"
```

### 14.1- Corrigir o erro no file config.py
```bash
preload=[os.path.join(HERE), 'default.toml'],  # corrigir como a linha baixo
preload=[os.path.join(HERE, 'default.toml')],
```
### 14.2- Corrigir no db.py
```bash
echo=settings.db.echo,
```



## 15- Alterar models -> user.py
```bash
username: str = Field(nullable=False, unique=True)
updated_at: Field(.... copiar do River)
```

### 15.1- No contanier da app executar para ver o erro do echo
```bash
alembic revision --autogenerate -m 'Criando user_name'

app@55a933f1b842:/home/api$ alembic revision --autogenerate -m 'Criando user_name'
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.ddl.postgresql] Detected sequence named 'user_id_seq' as owned by integer column 'user(id)', assuming SERIAL and omitting
INFO  [alembic.autogenerate.compare] Detected added column 'user.user_name'
INFO  [alembic.autogenerate.compare] Detected NOT NULL on column 'user.updated_at'
INFO  [alembic.autogenerate.compare] Detected added unique constraint 'None' on '['user_name']'
  Generating /home/api/migrations/versions/9a25f7c6d946_criando_user_name.py ...  done

alembic upgrade head

app@55a933f1b842:/home/api$ alembic upgrade head
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade 67faedd1a399 -> 9a25f7c6d946, Criando user_name
```


## 16- Iniciar a criação do CLI
 ```bash
- usaremos duas feramentas:
  - poetry add typer rich 

-->  fazer build
```

### 16.1- No container da app dar os comandos 
```bash
chamar ipython
 In [1]: from todo.models import User
 In [2]: from todo.db import engine
 In [3]: from sqlmodel import Session, select
 In [4]: query = select(User)
 In [5]: print(query)
SELECT "user".id, "user".name, "user".email, "user".password, "user".user_name, "user".active, "user".created_at, "user".updated_at 
FROM "user"

In [8]: with Session(engine) as session:
   ...:     users = session.exec(query)
   ...:     print(users)
   ...: 
<sqlalchemy.engine.result.ScalarResult object at 0x7f8924154310>

In [6]: with Session(engine) as session:
   ...:     users = session.exec(query).all()
   ...:     print(users)
   ...: 
[]
```


### 16.2- Alterar no  arquivo cli.py

```bash

from typer import Typer

from sqlmode import Session, select
from todo.config import settings
from todo.db import engine
from todo.models import User

main = Typer(name='Todo CLI', add_completion=False)

@main.command()
def shell():
    """Opens interactive shell"""
    -vars = {
      'settings': settings,
      'engine': engine,
      'select': select,
      'session': Session(engine),
      'User': User,
    }

    typer:echo(f'Auto imports: (list(_vars.keys))')
    try:
      from _ipython import  start_ipython

      start_ipython(
        args=['--ipython-dir=/tmp', '--no-banner'], user_ns=_vars
      )
    except ImportError:
      import code

      code.InteractiveConsole(_vars).interact()

@main.command()
def hello():
    """Print Hello World"""
    print("Hello World")


@main.command()
def user_list():
    """Lists all users"""
    table = Table(title='Todo Users List')
    fields = ['name', 'user_name', 'active', 'created_at']
    for header in fields:
      table.add_column(header, style='magenta')

    with Session(engine) as session:
      users = session.exec(select(Users))

      for user in users:
        table.add_row(*[getattr(user, field) for field in fields])

  Console.print(table)

```


## 17- Cuidar com o password

### 17.1- inserir um lib para manipular o password e criar um função para normalizar o password
```bash
poetry add python-slugify
```
### 17.2- no cli.py inserir
```bash
 from slugify import slugify

 -vars = {
 ...
 slugify: slugify,
 ...
 }
```

### 17.3- No file user.py fora da classe User inserir a função para normalisar o user-name
```bash
def gen_user_name(name: str) -> str:
    """Generate a slug user-name from a name"""
    return slugify(name)
```

### 17.4- Como fica a normalização do user-name
```bash
In [1]: text = 'Jorge Plautz'
In [2]: print(slugify(text))
jorge-plautz
```

### 17.5- Informação sobre o atributo ACTIVE do model USER
```bash
active: Optional[bool] = Field(default=True)

-> atributo active na classe User é para mostrar o usuario esta ativo.
   Quando deletar o user, não será deletado é sim o atributo ativo=True para False
```
### 17.6- No container um comando para fazer uma query
```bash
app@c2b33ba4290b:/home/api$ todo shell
Auto imports: ['settings', 'engine', 'select', 'session', 'slugify', 'User']
In [1]: name = 'Jorge Plautz'
In [2]: from slugify import slugify
In [3]: print(slugify(name))
jorge-plautz

In [4]: query = select(User).where(User.active == True)
In [5]: print(query)
SELECT "user".id, "user".name, "user".email, "user".password, "user".user_name, "user".active, "user".created_at, "user".updated_at 
FROM "user" 
WHERE "user".active = true

In [6]: users = session.exec(query)

In [7]: users
Out[7]: <sqlalchemy.engine.result.ScalarResult at 0x7f820bd4ce10>

In [8]: list(users)
Out[8]: []

app@c2b33ba4290b:/home/api$ todo user-list
               Todo Users List                
┏━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ name ┃ user_name ┃ created_at ┃ updated_at ┃
┡━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━┩
└──────┴───────────┴────────────┴────────────┘
```

### 17.6- Comando similar para fazer query
```bash
SELECT * FROM user WHERE active = true
 ```

## 18- Lib para implementat hashn o password e criar um função para normalizar o password
```bash
poetry add passlib[bcrypt]

❯ docker compose exec api /bin/bash
app@b31ee44209b3:/home/api$ pip list | grep passlib
passlib           1.7.4
app@b31ee44209b3:/home/api$ pip list | grep bcrypt
bcrypt            4.0.1
```

### 18.1- Alterar o file default.toml -> inserir
```bash
[default.security]
# Set secret key_in .secrets.toml
# SECRET_KEY = ""
ALGORITHM = "HS256"
ACCES_TOKEN_EXPIRE_MINUTES = 20
REFRESH_TOKEN_EXPIRE_MINUTES = 600
```

### 18.1- Criar arquivo na raiz .secrets.toml -> não deve subir para o github
```bash
[development]
dynaconf_merge = true

[development.security]
SECRET_KEY = "47d9cbc27d04c43fd30d2d66e827d9d412465a19ada8ec01242f33b6d9b11376"
```

### 18.2- Para gerar a secret_key com command python
```bash
❯ python -c "print(__import__('secrets').token_hex(32))"              
47d9cbc27d04c43fd30d2d66e827d9d412465a19ada8ec01242f33b6d9b11376

❯ openssl rand -hex 32                     
d7b57f4f10ce3d475363dc8698fc3e81eba20e2cee77d323fe1963183dde4664

app@b31ee44209b3:/home/api$ export TODO_SECRET_HEY=47d9cbc27d04c43fd30d2d66e827d9d412465a19ada8ec01242f33b6d9b11376
```

### 18.3- Inserir no config.py 
```bash
from dynaconf import Dynaconf, Validator

setting.validators.register:
  Validator('security.SECRET_KEY', must_exit=True, is_type_of=str)  
```


## 19- Segurança no file security.py inserir
```bash
"""Security utilities"""

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifies a hash against a plain_password."""
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """Generae a hash from plain text
    Args:
        password(str): Plain Text Password
    Returns:
       str: Hased Passwod
    """
    return pwd_context.hash(password)

class HashedPassword(str):
    """Takes a plain text password and hashes it.
    We can use it a field on our SQLModel
    class User(SQLModel, table=True):
        user_name= str
        password = HashedPassword
    """
    @classmethod
    def __get_validators_(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        """Accepts a plain password and returns a hashed password."""
        if not isinstance(v, str):
            raise TypeError('string required')

        hashed_password = get_password_hash(v)
        return cls(hashed_password)
```

### 19.1- No file user.py na class User
```bash
from todo.security import HashedPassword

password = HashedPassword
```

### 19.2- Comands no container criar o user
```bash
In [1]: user = User(name='Jorge Plautz', email='plautz@email.com', password='1234',user_name='plautz')

In [2]: user
Out[2]: User(id=None, name='Jorge Plautz', email='plautz@email.com', password='$2b$12$HrAxMEeMGLoWbiIqxtk3au4nANGwoXizQ22idzacwmgSksIp7e8XW', user_name='plautz', active=True, created_at=datetime.datetime(2023, 8, 14, 21, 49, 53, 788262), updated_at=datetime.datetime(2023, 8, 14, 21, 49, 53, 788268))

In [3]: from todo.security import verify_password

In [1]: user = User(name='Jorge Plautz', email='plautz@email.com', password='1234',user_name='plautz')

In [2]: user
Out[2]: User(id=None, name='Jorge Plautz', email='plautz@email.com', password='$2b$12$HrAxMEeMGLoWbiIqxtk3au4nANGwoXizQ22idzacwmgSksIp7e8XW', user_name='plautz', active=True, created_at=datetime.datetime(2023, 8, 14, 21, 49, 53, 788262), updated_at=datetime.datetime(2023, 8, 14, 21, 49, 53, 788268))

In [3]: from todo.security import verify_password

In [5]: user.password
Out[5]: '$2b$12$HrAxMEeMGLoWbiIqxtk3au4nANGwoXizQ22idzacwmgSksIp7e8XW'

In [7]: verify_password('plautz', user.password)
Out[7]: False

In [8]: verify_password('1234', user.password)
Out[8]: True
```

## 20- Comamd CREATE_USER
```bash
@main.command()
def create_user(
    name: str,
    email: str,
    password: str,
    user_name: Optional[str] = None
):
    """ Create a new uer."""

    with Session(engine) as session:
        user = User(
            email=email,
            password=password,
            user_name=user_name or gen_user_name(name)
        )
    session.add(user)
    session.commit()
    session.refresh(user)
    typer.echo(f'created {user.user_name} user.')
    return user
```
### 20.1- Para criar user no container
```bash
❯ docker compose exec api /bin/bash
app@798f762f0a69:/home/api$ todo create-user 'jorge' 'jlp@gmail.com' teste123
created jorge user.

app@798f762f0a69:/home/api$ todo create-user 'Gabriela Plautz' 'gabi@gmail.com' teste123
created gabriela-plautz user.
```

### 20.2- List todo user-list para verificar
```bash
app@798f762f0a69:/home/api$ todo user-list
           Todo Users List            
┏━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
┃ name            ┃ user_name        ┃
┡━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
│ Jorge Plautz    │ plautz           │
│                 │ jorge            │
│                 │ lindalene-plautz │
│                 │ rafaela-plautz   │
│ Gabriela Plautz │ gabriela-plautz  │
└─────────────────┴──────────────────┘
```

### 20.3- Comando TODO shell to check all users
```bash
In [2]: query = select(User).where(User.user_name=='gabriela-plautz')

In [3]: print(query)
SELECT "user".id, "user".name, "user".email, "user".password, "user".user_name, "user".active, "user".created_at, "user".updated_at 
FROM "user" 
WHERE "user".user_name = :user_name_1

In [4]: user = session.exec(query).first()

In [5]: user
Out[5]: User(email='gabi@gmail.com', user_name='gabriela-plautz', created_at=datetime.datetime(2023, 8, 18, 21, 54, 8, 156661), password='$2b$12$YzqiLP5LkuVd9tdspxpe5.pJh7Ju2wSmZ2Y2qBb9wMYkps4PAk2gK', id=7, name='Gabriela Plautz', active=True, updated_at=datetime.datetime(2023, 8, 18, 21, 54, 8, 156665))
```

## 21- Serialização inserir no model
```bash
Como este api é pequena vamos criar a serialização dentro do file user.py no models

 import pydantic ...

 class UserResponse(BaseModel):
      """ Serializer for Get all User Response."""
      name: str
      user_name: str

class UserDetailRespose(UserResponse):
      """Serializer for Detail Response."""
      active: bool
      created_at: datetime
      updated_at: datetime

class UserRequest(BaseModel):
    name: str,
    email: str,
    password: Optional[str] = None
    
    @root_validator(pre=True)
    def generate_user_name_if_not_set(cls, values):
        """Generate username if not send."""
        if not values.get('user_name'):
            values['user_name'] = gen_user_name(values['name'])
        return values
```

### 21.1- Inserir no __init__.py models ....
```bash
UserDeatilResponse, UserTRequest, ....
```

### 21.2- Como criar User
```bash
❯ docker compose exec api /bin/bash
app@83656b244372:/home/api$ todo shell
Auto imports: ['settings', 'engine', 'select', 'session', 'gen_user_name', 'User']
In [1]: from todo.models.user import UserResponse, UserDetailResponse, UserRequest
In [2]: new_user = UserRequest(name='Teste Simples', email='teste#email.com', password='teste1234')

In [3]: new_user
Out[3]: UserRequest(name='Teste Simples', email='teste#email.com', password='teste1234', user_name='teste-simples')

In [4]: db_user = User.from_orm(new_user)

In [5]: db_user
Out[5]: User(id=None, active=True, created_at=datetime.datetime(2023, 8, 21, 18, 55, 18, 666042), updated_at=datetime.datetime(2023, 8, 21, 18, 55, 18, 666047), name='Teste Simples', email='teste#email.com', password='$2b$12$gs6IyYJCMefg1sbHfUR.kutPto4DHTcHK.6qd4.w5tol46Yuf/t9m', user_name='teste-simples')

In [6]: UserResponse.parse_obj(db_user).json()
Out[6]: '{"name": "Teste Simples", "user_name": "teste-simples"}'

In [7]: UserDetailResponse.parse_obj(db_user).json()
Out[7]: '{"name": "Teste Simples", "user_name": "teste-simples", "active": true, "created_at": "2023-08-21T18:55:18.666042", "updated_at": "2023-08-21T18:55:18.666047"}'


In [2]: users = session.exec(select(User)).all()

In [3]: for u in users:
   ...:     print(u.name)
   ...: 
Jorge Plautz
None
None
None
Gabriela Plautz
```

## 22- Injeção de dependencia
```bash
Com gerador de context -> função geradora que cria a session e devolve

Inserir no file db.py

from fastapi import Depends

def get_session():
    with Session(engine) as session:
        yield session

ActiveSession = Depends(get_session)


### Criar as views e rotas 
Dentro do diretorio routes criar

from fastapi import APRouter
from fastapi exception inport HTTPException
from sqlmodel inport Session, select

from todo.db import ActiveSession
from todo.models import User, UserDetailResponse, UserRequest, UserResponse

router = APIRuter()


@route.get('/', response_model-list[UserResponse])
# *, da função significa que aceita somente argumentos nomeados 
# não aceita argumentos posicionais
async def list_users(*, session: Session = ActiveSession):
    """List all users."""
    users = session.exec(select(User)).all()
    return users

@route.get('/(user_name)', response_model=UserDetailResponse)
async def get_user_by_user_name(*,user_name: str, session:Session = ctiveSession):
    """Get user bt user_name."""
    query =select(User).where(user.user_name == user_name)
    users = session.exec(query).first()
    if nor user:
        raise HTTPExecption(status_code=status.HTTP_404_NOT_FOUND, detail='User not found.')
    return user


@router.post('/', response_model=UserRespone, status_code=status.HTTP_201_CREATED)
async def create_user(
  *, user: UserRequest, session: Session = ActiveSession
):
    """Create new user"""
    # TODO: Validar informaçoes recebidas com as constraints do banco
    db_user = user,from_orm(user)  
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user
```

### 22.1- Abri o __init__.py do routes
```bash
from fastapi import APIRouter
from .user import router as router_user

main_router = APORouter()
main_router: include_router(router_user, prefix='/user', tags=['user'])
```
### 22.2- Inserir no app.py
```bash
from todo,routes import main_router
```

## 23- Melhorar a rota do User
 Models/user.py  
 -> fat mode (tudo relacionado a modelo deixar dentro do models, 
    não dentro da class User)

### 23.1- Criar uma função (get_user)
```bash
from sqlmodel import Sesion, select
from tod.db import engine

def get_user(user_name: str = None) -> User | list[User] | None:
    """Função pode retornar um User ou uma lista de Users
        Usando a instrução "if ternário"
    """
    query = select(User).where(User.user_name == user_name) if user_name else select(User)
    # with -> gerenciador de contexto
    with Session(engine) as session:
      users =session.exec(select(User).first() if user_name else session.exec(query).all()
    return
```




### 23.2- Abri o __init__.py do models -> inserir o get_user
```bash
from .user import (User,UserDetailResponse,UserRequest,UserResponse,gen_user_name,
    get_user,
)
__all__ = ['SQLModel','User','UserDetailResponse','UserRequest',
    'UserResponse','gen_user_name','get_user',
]
```

### 23.3- Alterar as demais rotas com a função get_user
```bash
@router.get('/', response_model=list[UserResponse])
async def list_users(*, session: Session = ActiveSession):
    """List all users."""
    users = get_user()
    return users

    user = get_user(user_name=user_name)
```
 

## 24- Prepara o projeto para rota de autenticação 30/08/23
```bash
poetry add python-jose[cryptography]
```

### 24.1 Inserir no file auth.py
```bash
"""Token based auth"""

from datetime import timedelta, datetime
from functools import partial
from fastapi import HTTPException, status

from jose import jwt, JWTError
from pydantic import BaseModel
from todo.config import settings
from todo.models import get_user, User

SECRET_KEY = settings.security.SECRET_KEY
ALGORITHM = settings.security.ALGORITHM

# Models
class TokenData(BaseModel):
  user_name: str | None

# functions
def create_access_token(
    data: dict,
    expires_delta: timedelta = None,
    scope: str = 'access_token'
) -> str:

    """Creates a JWT Token from user data"""
    to_encode = data.copy()
    # definido a variavel com o timedelta default
    expire = datetime.utcnow() + timedelta(minutes=15)

    # Caso seja definido um timedelta diferente
    if expires_delta:
        expire = datetime.utcnow() + expires_delta

    to_encode.update({'exp': expire, 'scope': scope})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

# neste caso será gerado um refresh_token, recebe todos os paremetros
# access_token, mas vai mudar o escopo para refresh
# funcionalidade da functools
create_refresh_token = partial(create_access_token, scope='refresh_token')


def get_current_user(token: str):
    """Get current user autehnticated"""

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials.',
        headers={'WWW-Authenticate': 'Bearer'},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_name = payload.get('sub')
        if user_name is None:
            raise credentials_exception
        token_data = TokenData(user_name=user_name)
    except JWTError:
        raise credentials_exception

    user = get_user(user_name=token_data.user_name)

    if user is None:
        raise credentials_exception
    return user

def validate_token(token: str) -> User:
    """Validate user Token"""
    user = get_current_user(token=token)
    return user
```

### 24.2- Teste -> Activar no container todo shell
```bash
❯ docker compose exec api todo user-list
            Todo Users List            
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
┃ name             ┃ user_name        ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
│ Jorge Plautz     │ plautz           │
│ Gabriela Plautz  │ gabriela-plautz  │
│ Jorge            │ jorge            │
│ Lindalene Plautz │ lindalene-plautz │
│ Rafaela Plautz   │ rafaela-plautz   │
│ Teste Teste      │ teste-teste      │
└──────────────────┴──────────────────┘

❯ docker compose exec api todo shell    
Auto imports: ['settings', 'engine', 'select', 'session', 'gen_user_name', 'User']

In [1]: from todo.auth import create_access_token, validate_token
In [2]: token = create_access_token({'sub': 'plautz'})
In [3]: token
Out[3]: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJwbGF1dHoiLCJleHAiOjE2OTQ4MDM1MjcsInNjb3BlIjoiYWNjZXNzX3Rva2VuIn0.1-Ff984a-ruEh5Dw0ZkcYLV2AnspPKGnKUT_QFv5Jmg'

In [4]: validate_token(token=token)
Out[4]: User(password='$2b$12$pYXHdgj.nNCaqSkRonMsAeZPCvvcVqdpO.REUNCx6na9a2r3WeLYG', name='Jorge Plautz', id=1, active=True, updated_at=datetime.datetime(2023, 8, 14, 21, 59, 57, 191372), email='plautz@email.com', user_name='plautz', created_at=datetime.datetime(2023, 8, 14, 21, 59, 57, 191367))
```


***********************************************

04Out23

Rever o arquivo auth.py (regra de negocio de autenticação)
Rever o arquivo cli.py


Criar rotas para autenticação

Criar um novo file no routes -> auth.py

from fastapi import APIRouter, Dependes, HTTPxception, status
from fastapi.security import OAuth2PasswordRequestForm

from todo.auth import Token, authenricate_user
from todo.config import settings
from todo.models import User, get_user

ACCES_TOKEN_EXPIRE_MINUTES = settings.security.access_token_expire_minutes
REFRESH_TOKEN_EXPIRE_MINUTES = settings.security.refresh_token_expire_minutes

router = APIRouter()

@router.post('/token', response_model=Token)
async def login_for_access_token(
  form_data: OAuth2PasswordRequestForm=Depends()
):
  user = authewnticate_user(get_user, form_data.username, form_data.password)
  if not user or not isinstance(user, User):
    raise HTTPException(
      status_code=status.HTTD_401_UNAUTHORIZED,
      detail='Incorrect username or password',
      header={'WWW-Authenticate': 'Bearer'}
    )
  access_token_expires = timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
  access_token = create_access_token(
    data = {'sub': user.user_name, 'fresh': True}, expires_delta=access_token_expires
  )
  refresh_token_expires = timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
  refresh_token = create_refresh_token(
    data = {'sub': user.user_name}, expires_delta=access_token_expires
  )
  return {
    'access_token': access_token,
    'refresh_token': refresh_token,
    'token_type': 'bearer'
  }



@router.post('/token', response_model=Token)
async def refresh_token(form_data: RefreshToken):
  user = await validate

  ...


  Editar o __init__.py -> inserir as rotas

  instalar a lib python-multitask


## Monitoria 25/10/2023

Criar SuperUser

Ajustar modulo User
Para alterar user será necessário ter atributos administrador
- super_user: Option[bool] = Field(default=False)

class UserDetialResponse(...):
  super_user: Optional[bool] = False

class UserRequest(...):
inserir a informação superuser

  Rodar a migração
  docker compose exec api alembic revision -- autogenerate
  docker compose exec api alembic upgrade head

Proteger as rotas
 na função get_curretnt_active_user

criar a função assync def get_current_super_user

ver as rotas:
- router.get( ... dependencies=[]

## **************************************************************
Correction -> todo/routes/auth.py", line 53, in refresh_token

  File "/home/api/todo/routes/auth.py", line 53, in refresh_token
    user = await validate_token(token=form_data.refresh_token)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: object User can't be used in 'await' expression

## **************************************************************