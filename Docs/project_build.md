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
.

## Create files
╰─$ touch LICENSE
╰─$ touch .gitignore
╰─$ touch README.md 

## Edit files
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
╰─$ git branch                                                         
╰─$ git branch -M master main      
╭─plautz@ProBook-6470b ~/Proj_2023/mytodo ‹main› 


## Criar o prpjeto no github

## Criar git remote localmente

╭─plautz@ProBook-6470b ~/Proj_2023/mytodo ‹main› 
╰─$ git remote -v    

╰─$ git remote add origin git@github.com:jlplautz/mytodo.git
 
╰─$ git fetch                                               
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


## Criar a branch no github "Criar estrutua do Projeto"

╰─$ git fetch           
╰─$ git branch               
╰─$ git status
On branch main
╰─$ git checkout -b issue-1                                                                    
Switched to a new branch 'issue-1'

## Iniciar Poetry

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


─$ mkdir tests       
╰─$ cd tests        
╰─$ touch __init__py

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
╰─$ touch __init__py 

╰─$ cd ..  
╰─$ tree -L 2
.
├── LICENSE
├── pyproject.toml
├── README.md
├── tests
│   └── __init__py
└── todo
    ├── app.py
    ├── auth.py
    ├── cli.py
    ├── config.py
    ├── db.py
    ├── default.py
    ├── __init__py
    └── security.py

2 directories, 12 files

─$ mkdir models        
╰─$ mkdir routes                
╰─$ mkdir taks     

╰─$ touch models/__init__py                  
╰─$ touch routes/__init__py      
╰─$ touch tasks/__init__py      

╰─$ mkdir postgres 
╰─$ touch postgres/Dockerfile
╰─$ touch postgres/create_databases.sh         

## Fazer git add + commit + push

╰─$ git status                                                                                            130 ↵
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
 ╰─$ git status                                                                                            127 ↵
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
        
╰─$ git status                                                                                            127 ↵
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

╭─plautz@ProBook-6470b ~/Proj_2023/mytodo ‹issue-1●› 
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
╭─plautz@ProBook-6470b ~/Proj_2023/mytodo ‹issue-1› 
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
 
 ## Fazer checkout para branch main e fazer git pull
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
    
## Installar as dependencias de desenvolvimento no Projeto
    poetry add --group dev pytest pytest-order
    poetry add --group dev ipython
    poetry add --group dev ipdb
    poetry add --group dev flake8
    poetry add --group dev httpx
    
## Fazer git add + git commit + git push

─$ git status             
On branch issue-3
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   pyproject.toml

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        poetry.lock

no changes added to commit (use "git add" and/or "git commit -a")
 
╰─$ git add pyproject.toml
╰─$ git add poetry.lock   
╰─$ git commit -m 'feat(issue-3): Installed dev dependencies.'                          
[issue-3 c364bd3] feat(issue-3): Installed dev dependencies.
 2 files changed, 589 insertions(+)
 create mode 100644 poetry.lock

╰─$ git push origin issue-3                                   
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 4 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 7.35 KiB | 2.45 MiB/s, done.
Total 4 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
remote: 
remote: Create a pull request for 'issue-3' on GitHub by visiting:
remote:      https://github.com/jlplautz/mytodo/pull/new/issue-3
remote: 
To github.com:jlplautz/mytodo.git
 * [new branch]      issue-3 -> issue-3
 
╰─$ git checkout main                                         
Switched to branch 'main'

╰─$ git pull origin main   
remote: Enumerating objects: 6, done.
remote: Counting objects: 100% (6/6), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 4 (delta 2), reused 3 (delta 2), pack-reused 0
Unpacking objects: 100% (4/4), 7.71 KiB | 7.71 MiB/s, done.
From github.com:jlplautz/mytodo
 * branch            main       -> FETCH_HEAD
   d8079cb..9b4183f  main       -> origin/main
Updating d8079cb..9b4183f
Fast-forward
 poetry.lock    | 581 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 pyproject.toml |   8 ++
 2 files changed, 589 insertions(+)
 create mode 100644 poetry.lock
 
 *****************************************************************
 
 ## Criar nova branch no github
   --> Intall project dependencies.
   
╰─$ git checkout -b issue-5                                   
Switched to a new branch 'issue-5'
╭─plautz@ProBook-6470b ~/Proj_2023/mytodo ‹issue-5› 
╰─$ poetry add fastapi uvicorn


git status                                                                                              
On branch issue-5
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   poetry.lock
        modified:   pyproject.toml

no changes added to commit (use "git add" and/or "git commit -a")

╰─$ git add poetry.lock       
╰─$ git add pyproject.toml
╭─plautz@ProBook-6470b ~/Proj_2023/mytodo ‹issue-5●› 
╰─$ git status            
On branch issue-5
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   poetry.lock
        modified:   pyproject.toml


╰─$ git commit -m 'feat(issue-5): Installed project dependencies.'   
[issue-5 4229fbb] feat(issue-5): Installed project dependencies.
 2 files changed, 238 insertions(+), 6 deletions(-)

╰─$ git push origin issue-5                                       
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 4 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 7.16 KiB | 2.39 MiB/s, done.
Total 4 (delta 3), reused 0 (delta 0)
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
remote: 
remote: Create a pull request for 'issue-5' on GitHub by visiting:
remote:      https://github.com/jlplautz/mytodo/pull/new/issue-5
remote: 
To github.com:jlplautz/mytodo.git
 * [new branch]      issue-5 -> issue-5
 
 
─$ git checkout main                                             
Switched to branch 'main'

╰─$ git pull origin main
From github.com:jlplautz/mytodo
 * branch            main       -> FETCH_HEAD
Updating 9b4183f..1bd4326
Fast-forward
 poetry.lock    | 242 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++---
 pyproject.toml |   2 +
 2 files changed, 238 insertions(+), 6 deletions(-)
    
******************************************************************************
 
 ## Task com TDD

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
 
***********************************************************
 
def test_main_api_works_ok(): 
    """This test guaranted that the endpoint works properly """
     response = client.get('/')
     assert response.status == status.HTTP_200_OK
     assert response.text == {'message': 'Hello_world!'}
     
     
def test_main_api_has_docs():
    response = Client.get('/docs')
    assert response.status_code == status.HTTP_200_OK     
    
***********************************************************
  link -> https://fastapi.tiangolo.com/tutorial/response-status-code/
  
--> file  app.py
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


******************************************************************************

## Colocar o PostGres como serviço

--> file .gitignore inserir
.vscode/
.idea/


## Qaundo executar alguma alterar no codigo da branch main

Executar:
1- git stash (guarda as alteraçoes)
2- git checkout -b <nova branch>
3- git stash pop (para trazer as alteraçoes para a <nova branch>)  

### Database volume
 Criar um diretorio na raiz do projeto
 Postgres -> para guardar o DB do volume

 Dentro do diretorio postgres 
 criar um file Dokefile
 ******************************************************
 FROM postgres:alpine3.18
 COPY create-databases.sh /docker-entrypoint-initdb.d/
 ******************************************************

 criar um file create-databases.sh
 *************************************************************
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

# ***************************************************************************

## issue-7 --> Creates Postgres service and first tests

git status   
On branch issue-7
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   postgres/Dockerfile
        modified:   postgres/create_databases.sh
        modified:   pyproject.toml
        deleted:    tests/__init__py
        deleted:    todo/__init__py
        modified:   todo/app.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        Docs
        tests/__init__.py
        tests/test_main_api.py
        todo/__init__.py


╰─$ git add todo/         
╰─$ git add postgres/     
╰─$ git add tests/   
╰─$ git add pyproject.toml
╰─$ git add Docs    
(mytodo-py3.11) ╭─plautz@ProBook-6470b ~/Proj_2023/mytodo ‹issue-7●› 
╰─$ git status  
On branch issue-7
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   Docs
        modified:   postgres/Dockerfile
        modified:   postgres/create_databases.sh
        modified:   pyproject.toml
        renamed:    tests/__init__py -> tests/__init__.py
        new file:   tests/test_main_api.py
        renamed:    todo/__init__py -> todo/__init__.py
        modified:   todo/app.py

(mytodo-py3.11) ╭─plautz@ProBook-6470b ~/Proj_2023/mytodo ‹issue-7●› 
╰─$ git commit -m 'feat(issue-7): Creates Postgres service and first tests.'                   
[issue-7 efb90a1] feat(issue-7): Creates Postgres service and first tests.
 8 files changed, 623 insertions(+), 1 deletion(-)
 create mode 100644 Docs
 rename tests/{__init__py => __init__.py} (100%)
 create mode 100644 tests/test_main_api.py
 rename todo/{__init__py => __init__.py} (100%)
(mytodo-py3.11) ╭─plautz@ProBook-6470b ~/Proj_2023/mytodo ‹issue-7› 
╰─$ git push origin issue-7                                                 
Enumerating objects: 19, done.
Counting objects: 100% (17/17), done.
Delta compression using up to 4 threads
Compressing objects: 100% (11/11), done.
Writing objects: 100% (11/11), 5.66 KiB | 1.13 MiB/s, done.
Total 11 (delta 2), reused 0 (delta 0)
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
remote: 
remote: Create a pull request for 'issue-7' on GitHub by visiting:
remote:      https://github.com/jlplautz/mytodo/pull/new/issue-7
remote: 
To github.com:jlplautz/mytodo.git
 * [new branch]      issue-7 -> issue-7

╰─$ git checkout main                                                       
Switched to branch 'main'

╰─$ git pull origin main   
remote: Enumerating objects: 19, done.
remote: Counting objects: 100% (17/17), done.
remote: Compressing objects: 100% (9/9), done.
remote: Total 11 (delta 2), reused 10 (delta 2), pack-reused 0
Unpacking objects: 100% (11/11), 6.02 KiB | 3.01 MiB/s, done.
From github.com:jlplautz/mytodo
 * branch            main       -> FETCH_HEAD
   1bd4326..5815446  main       -> origin/main
Updating 1bd4326..5815446
Fast-forward
 Docs                              | 566 +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
 postgres/Dockerfile               |   2 +
 postgres/create_databases.sh      |  22 +++
 pyproject.toml                    |   2 +-
 tests/{__init__py => __init__.py} |   0
 tests/test_main_api.py            |  19 +++
 todo/{__init__py => __init__.py}  |   0
 todo/app.py                       |  13 ++
 8 files changed, 623 insertions(+), 1 deletion(-)
 create mode 100644 Docs
 rename tests/{__init__py => __init__.py} (100%)
 create mode 100644 tests/test_main_api.py
 rename todo/{__init__py => __init__.py} (100%)


# ***************************************************************************

## issue-9 --> Create a Dockerfile-dev and docker-compose.yml in the root

Dockerfile.dev
******************************************************************
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
******************************************************************

Docker-compose.yml

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

      ******************************************************************

## executar git status, add, commit, push


# **************************************************************************

## issue-11 --> Install dev dependencies pytest-cov and taskipy

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

╰─$ poetry  remove --group dev flake8                                                                          1 ↵
Updating dependencies
Resolving dependencies... (0.3s)

Writing lock file

Package operations: 0 installs, 0 updates, 4 removals

  • Removing flake8 (6.0.0)
  • Removing mccabe (0.7.0)
  • Removing pycodestyle (2.10.0)
  • Removing pyflakes (3.0.1)


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

### inserir no pyproject.toml
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


## executar git status, add, commit, push


# *****************************************************************************

 CMDs docker
  
  
  Qdo usamos um diretorio para volume as caracteristica deste diretorio é alterado para root
  
  Para resolve a task clean basta mover p diretorio .postgres para a diretorio home echo ~
  Alterar o file docker-compose.yml para apontar para o novo diretorio na home
 
 

# *****************************************************************************

data: 19/07/23 Comunidade live 45

Modelar o banco  branch#20

- Migrações com Alambique

 - Tabela de usuários e outra de todo
 
   link erb.dbdesigner.net/designer/schema/
   
   1- user para muitas tasks
   2- uma task para um user  
   
- docker compose logs --follow pata verificar os logs
- docker-compose logs --follow
- docker logs -ft todo_project_api_1 
- docker-compose logs -t 

poetry add psycopg2-binary sqlmodel

docker compose exec api pip list | grep psy 

criar arquivo no models
 - user.py
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
 
  - no __init__.py inserir
 
 Para facilitar o import quando necessario
 
 from sqlmode import SQLModel
 from .user import User
 
  __ALL__ * ['User', 'SQLModel']
  
   
 poetry add dynaconf
  
 fazer um task build
 
  no file default.toml # para fazer a conexão com o banco
 
 [default]
 
 [default.db]
 uri = ''
 connect_args = (check_same_thread=false)
 echo = false
 
 
  no file config.py
  
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
 
  
 Link -> https://www.youtube.com/watch?v=-qWySnuoaTM&pp=ygUOY29kZXNob3cgZmxhc2s%3D
 
 commit branch 21 alteração no projeto com Dynaconf

# *****************************************************************************

## Alguns comandos docker

docker compose up
docker compose prone
docker container ls
docker compouse build --no-cache
docker compouse --rm -ti <name> /bin/bash

─$ docker compose up -d                                                              125 ↵
[+] Running 3/3
 ✔ Network mytodo_default  Created                                                     0.1s 
 ✔ Container mytodo-db-1   Started                                                     0.6s 
 ✔ Container mytodo-api-1  Started                                                     1.0s 

╰─$ docker container ls   
CONTAINER ID   IMAGE                                COMMAND                  CREATED          STATUS          PORTS                                       NAMES
77b32afbaa2f   mytodo-api                           "uvicorn --reload to…"   15 seconds ago   Up 13 seconds   0.0.0.0:8000->8000/tcp, :::8000->8000/tcp   mytodo-api-1
8d19c5d29c5d   todo_postgres-15-alpine-multi-user   "docker-entrypoint.s…"   15 seconds ago   Up 14 seconds   0.0.0.0:5432->5432/tcp, :::5432->5432/tcp   mytodo-db-1

╰─$ docker exec -it mytodo-api-1 /bin/bash      
app@77b32afbaa2f:/home/api$ ls
 Dockerfile.dev   LICENSE     docker-compose.yml   postgres        'sk '    todo
 Docs             README.md   poetry.lock          pyproject.toml   tests
app@77b32afbaa2f:/home/api$ pytest
=================================== test session starts ====================================
platform linux -- Python 3.11.1, pytest-7.4.0, pluggy-1.2.0 -- /usr/local/bin/python3.11
cachedir: .pytest_cache
rootdir: /home/api
configfile: pyproject.toml
plugins: order-1.1.0, anyio-3.7.1, cov-4.1.0
collected 2 items                                                                          

tests/test_main_api.py::test_main_api_works_ok PASSED                                [ 50%]
tests/test_main_api.py::test_main_api_has_docs PASSED                                [100%]

===================================== warnings summary =====================================
../../usr/local/lib/python3.11/site-packages/_pytest/config/__init__.py:1433
  /usr/local/lib/python3.11/site-packages/_pytest/config/__init__.py:1433: PytestConfigWarning: No files were found in testpaths; consider removing or adjusting your testpaths configuration. Searching recursively from the current directory instead.
    self.args, self.args_source = self._decide_args(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=============================== 2 passed, 1 warning in 2.31s ===============================
app@77b32afbaa2f:/home/api$ pytest --cov=todo
=================================== test session starts ====================================
platform linux -- Python 3.11.1, pytest-7.4.0, pluggy-1.2.0 -- /usr/local/bin/python3.11
cachedir: .pytest_cache
rootdir: /home/api
configfile: pyproject.toml
plugins: order-1.1.0, anyio-3.7.1, cov-4.1.0
collected 2 items                                                                          

tests/test_main_api.py::test_main_api_works_ok PASSED                                [ 50%]
tests/test_main_api.py::test_main_api_has_docs PASSED                                [100%]

===================================== warnings summary =====================================
../../usr/local/lib/python3.11/site-packages/_pytest/config/__init__.py:1433
  /usr/local/lib/python3.11/site-packages/_pytest/config/__init__.py:1433: PytestConfigWarning: No files were found in testpaths; consider removing or adjusting your testpaths configuration. Searching recursively from the current directory instead.
    self.args, self.args_source = self._decide_args(

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html

---------- coverage: platform linux, python 3.11.1-final-0 -----------
Name               Stmts   Miss  Cover
--------------------------------------
todo/__init__.py       0      0   100%
todo/app.py            5      0   100%
todo/auth.py           0      0   100%
todo/cli.py            0      0   100%
todo/config.py         0      0   100%
todo/db.py             0      0   100%
todo/default.py        0      0   100%
todo/security.py       0      0   100%
--------------------------------------
TOTAL                  5      0   100%

=============================== 2 passed, 1 warning in 4.39s ===============================