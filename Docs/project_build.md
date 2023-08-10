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

Ajustar as configuraçoes de projeto

O que foi feito ate o momento:
 - foi instalado dependencias de desenvolvimento
 - foi instalado dependencias de produção
 - foi containerizado os serviços
 - foi orquestrado com docker compose os serviços
   - aplicação
   - banco
   
 Modelar o banco USERs
 - modelagem com SQLMODEL
 
 Ajustar as configuração de projeto usando o dynaconf
 Criar a conexão com o banco de dados
 Configurar para fazer as migraçoes com alambic
 
 Usando erd.dbdesignser.net 
    link erb.dbdesigner.net/designer/schema/

- Migrações com Alambique

 - Tabela de usuários e outra de todo
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
 

 
 ### Para facilitar o import da tabela User quando necessario
 ### Inserir no __init__.py do direotio models

 from sqlmode import SQLModel
 from .user import User
 
  __all__ * ['User', 'SQLModel']
  
   
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


# *****************************************************************************

## comandos no container 

╰─$ docker compose exec api poetry show --tree
The virtual environment found in /home/api/.venv seems to be broken.
Recreating virtualenv mytodo in /home/api/.venv                     <- CRIOU O AMBIENTE VIRTUAL  
blue 0.9.1 Blue -- Some folks like black but I prefer blue.
├── black 22.1.0
│   ├── click >=8.0.0 
│   │   └── colorama * 
│   ├── mypy-extensions >=0.4.3 
│   ├── pathspec >=0.9.0 
│   ├── platformdirs >=2 
│   └── tomli >=1.1.0 
└── flake8 >=3.8,<5.0.0
    ├── mccabe >=0.6.0,<0.7.0 
    ├── pycodestyle >=2.8.0,<2.9.0 
    └── pyflakes >=2.4.0,<2.5.0 
fastapi 0.100.0 FastAPI framework, high performance, easy to learn, fast to code, ready for production
├── pydantic >=1.7.4,<1.8 || >1.8,<1.8.1 || >1.8.1,<2.0.0 || >2.0.0,<2.0.1 || >2.0.1,<3.0.0
│   └── typing-extensions >=4.2.0 
├── starlette >=0.27.0,<0.28.0
│   └── anyio >=3.4.0,<5 
│       ├── idna >=2.8 
│       └── sniffio >=1.1 
└── typing-extensions >=4.5.0
httpx 0.24.1 The next generation HTTP client.
├── certifi *
├── httpcore >=0.15.0,<0.18.0
│   ├── anyio >=3.0,<5.0 
│   │   ├── idna >=2.8 
│   │   └── sniffio >=1.1 
│   ├── certifi * 
│   ├── h11 >=0.13,<0.15 
│   └── sniffio >=1.0.0,<2.0.0 (circular dependency aborted here)
├── idna *
└── sniffio *
ipdb 0.13.13 IPython-enabled pdb
├── decorator *
└── ipython >=7.31.1
    ├── appnope * 
    ├── backcall * 
    ├── colorama * 
    ├── decorator * 
    ├── jedi >=0.16 
    │   └── parso >=0.8.0,<0.9.0 
    ├── matplotlib-inline * 
    │   └── traitlets * 
    ├── pexpect >4.3 
    │   └── ptyprocess >=0.5 
    ├── pickleshare * 
    ├── prompt-toolkit >=3.0.30,<3.0.37 || >3.0.37,<3.1.0 
    │   └── wcwidth * 
    ├── pygments >=2.4.0 
    ├── stack-data * 
    │   ├── asttokens >=2.1.0 
    │   │   └── six * 
    │   ├── executing >=1.2.0 
    │   └── pure-eval * 
    └── traitlets >=5 (circular dependency aborted here)
ipython 8.14.0 IPython: Productive Interactive Computing
├── appnope *
├── backcall *
├── colorama *
├── decorator *
├── jedi >=0.16
│   └── parso >=0.8.0,<0.9.0 
├── matplotlib-inline *
│   └── traitlets * 
├── pexpect >4.3
│   └── ptyprocess >=0.5 
├── pickleshare *
├── prompt-toolkit >=3.0.30,<3.0.37 || >3.0.37,<3.1.0
│   └── wcwidth * 
├── pygments >=2.4.0
├── stack-data *
│   ├── asttokens >=2.1.0 
│   │   └── six * 
│   ├── executing >=1.2.0 
│   └── pure-eval * 
└── traitlets >=5
isort 5.12.0 A Python utility / library to sort Python imports.
psycopg2-binary 2.9.6 psycopg2 - Python-PostgreSQL Database Adapter
pytest 7.4.0 pytest: simple powerful testing with Python
├── colorama *
├── iniconfig *
├── packaging *
└── pluggy >=0.12,<2.0
pytest-cov 4.1.0 Pytest plugin for measuring coverage.
├── coverage >=5.2.1
└── pytest >=4.6
    ├── colorama * 
    ├── iniconfig * 
    ├── packaging * 
    └── pluggy >=0.12,<2.0 
pytest-order 1.1.0 pytest plugin to run your tests in a specific order
└── pytest >=6.2.4
    ├── colorama * 
    ├── iniconfig * 
    ├── packaging * 
    └── pluggy >=0.12,<2.0 
sqlmodel 0.0.8 SQLModel, SQL databases in Python, designed for simplicity, compatibility, and robustness.
├── pydantic >=1.8.2,<2.0.0
│   └── typing-extensions >=4.2.0 
├── sqlalchemy >=1.4.17,<=1.4.41
│   └── greenlet !=0.4.17 
└── sqlalchemy2-stubs *
    └── typing-extensions >=3.7.4 
taskipy 1.11.0 tasks runner for python projects
├── colorama >=0.4.4,<0.5.0
├── mslex >=0.3.0,<0.4.0
├── psutil >=5.7.2,<6.0.0
└── tomli >=2.0.1,<3.0.0
uvicorn 0.23.1 The lightning-fast ASGI server.
├── click >=7.0
│   └── colorama * 
└── h11 >=0.8

## para evitar a criação do ambiente virtual no container
╰─$ docker compose exec api pip list | grep pytest 
pytest            7.4.0
pytest-cov        4.1.0
pytest-order      1.1.0

╰─$ docker compose exec api pip list | grep sql   
sqlalchemy2-stubs 0.0.2a35
sqlmodel          0.0.8

╰─$ docker compose exec api pip list | grep pyd   
pydantic          1.10.12

 
 - docker compose logs -t --follow db
 - docker compose logs -t --follow api
 
 
 ## ***************************************************************************
 
 Comunidade  26/07/23
 
 No file db.py
 
 """Database connection"""
 
 from sqlmodel import create_engine
 from todo.config import settings
 
 engine = create_engine(
    settings.db.uri,
    echo=settings.db.echo,
    connect_ag=settings.db.connect_args
)
 
create commit criada a conexao com o banco de dados


 ## ***************************************************************************
 
 Fazer as migraçoescommand
 
 poetry add alembic
 
 # depois de instalado lib alembic será necessario fazer task build
   As primeiras migraçoes precisam serem no container
 
 
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:
 ╭─plautz@ProBook-6470b ~/Proj_2023/mytodo ‹main●› 
╰─$ command -v python
/home/plautz/.pyenv/shims/python

╭─plautz@ProBook-6470b ~/Proj_2023/mytodo ‹main●› 
╰─$ poetry shell
The virtual environment found in /home/plautz/Proj_2023/mytodo/.venv seems to be broken.
Recreating virtualenv mytodo in /home/plautz/Proj_2023/mytodo/.venv
Spawning shell within /home/plautz/Proj_2023/mytodo/.venv
╭─plautz@ProBook-6470b ~/Proj_2023/mytodo ‹main●› 
╰─$ emulate bash -c '. /home/plautz/Proj_2023/mytodo/.venv/bin/activate'

(mytodo-py3.11) ╭─plautz@ProBook-6470b ~/Proj_2023/mytodo ‹main●› 
╰─$ command -v python
/home/plautz/Proj_2023/mytodo/.venv/bin/python
 
 tldr ls tem que instalar no bash
 
 # :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:
 
 poetry run alembic
 


 # :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:
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

 # :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:
 

## Cria o diretorio migrations
poetry run alembic init migrations

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



## no arquivo env.py dentro do diretorio migrations
  
 from todo import models     
 from todo.db import engine
 from todo.config import settings
 # importar SQLModel metadata
 target_metadata =  models.SQLModel.metadata
 

## na função run_magrations_offline -> alterar
url = setting.db.uri

## na função run_magration_online -> alterar
connectable = engine

## No file .flake8 -> inserir
 exclude 
    migrations/
 
## no file script.py.mako -> inserir depois da linha import sqlalchemy as sa
import sqlmodel

 
### Fazer as migraçoes no container"""
alembic revision --autogenerate -m 'initial'

### comando dynaconf list no container da aplicação
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


### Aplicar a migração apos é possivel ver a tabela no Banco
alembic upgrade head
 
app@2d8596c45856:/home/api$ alembic upgrade head
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 67faedd1a399, initial


### No container os comandos para criar user.

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



Link
https://ahmed-nafies.medium.com/fastapi-with-sqlalchemy-postgresql-and-alembic-and-of-course-docker-f2b7411ee396

SQLAlchemy - ORM
SQLMODEL   - ORM

Dynaconf - arquivo para ver variaveis de ambiente ambiente / 
         - ler password  
         - decouple

ORM - sql puro  

alembic + sq


 ## ***************************************************************************
 
 Comunidade  02/08/23

 Quando usamos email para authenticar podemos deixar exposto o email dos users.
 procurar não mostrar o email no list

 SQLMODEL é uma abstração do sqlalchemy


### Alterar no pyproject.toml incluir apos o readme
# incluir pasta to projeto para possibilitar futuramente a exportação do projeto
packages = [{include = "todo"}]   

### Alterar no pyproject.toml incluir apos group.dev
[tool.poetry.scripts]
# para poder chamar o função cli
todo = "todo.cli:main" 
- precisa fazer buid depois da alteração do tool.poetry.script

### no file cli.py inserir
def main():
    print('Hello world')

### commit das alterações do pyproject.toml

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:

### no contanier da app executar para ver o erro do echo
alembic --help

app@5e2fd8ba1e2a:/home/api$ alembic history
67faedd1a399 -> 99b06a755b1a (head), teste
<base> -> 67faedd1a399, initial

# verify the error
alembic revision --autogenerate -m 'teste'

  File "/usr/local/lib/python3.11/site-packages/dynaconf/vendor/box/box.py", line 176, in __getattr__
    raise BoxKeyError(str(E)) from _A
dynaconf.vendor.box.exceptions.BoxKeyError: "'DynaBox' object has no attribute 'echo'"


### Corrigir no file config.py
preload=[os.path.join(HERE), 'default.toml'],  # corrigir como a linha baixo
preload=[os.path.join(HERE, 'default.toml')],

### Corrigir no db.py
echo=settings.db.echo,

### para ver as variaveis env
printenv | grep todo

╰─$ printenv | grep todo
OLDPWD=/home/plautz/Proj_2023/mytodo
PWD=/home/plautz/Proj_2023/mytodo


### commit da configuraçã dynaconf

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:

### alterar models -> user.py

username: str = Field(nullable=False, unique=True)
updated_at: Field(.... copiar do River)

### no contanier da app executar para ver o erro do echo
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

### commit da alteração do models user.py

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:

### Iniciar a criação do CLI

- usaremos duas feramentas:
  - poetry add typer rich 

  fazer build


### no container da app dar os comandos 
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

### no arquivo cli.py

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




app@d127c9b764a4:/home/api$ todo --help                                                                                                                               
 Usage: todo [OPTIONS]                                                                                                                                                                                                                              
 Opens interactive hell                                                                                                                
                                                                                                                                        
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

app@d127c9b764a4:/home/api$ todo --help
 Usage: todo [OPTIONS] COMMAND [ARGS]...                                                                                                
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                                                                          │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ hello                       Print Hello World                                                                                        │
│ shell                       Opens interactive shell                                                                                  │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
app@d127c9b764a4:/home/api$ todo hello
Hello world

app@d127c9b764a4:/home/api$ todo shell
Auto imports: ['settings', 'engine', 'select', 'session', 'User']

In [1]: User
Out[1]: todo.models.user.User
In [2]: query = select(User)
In [3]: print(query)
SELECT "user".id, "user".name, "user".email, "user".password, "user".user_name, "user".active, "user".created_at, "user".updated_at 
FROM "user"
In [4]: session.exec(query)
Out[4]: <sqlalchemy.engine.result.ScalarResult at 0x7ff95282acd0>

In [5]: users = session.exec(query).all()
In [6]: users
Out[6]: []

### como despacotar uma lista
In [1]: lista = [1,2,3,4,5]
In [2]: primeiro, *meio, ultimo = lista
In [3]: primeiro
Out[3]: 1
In [4]: meio
Out[4]: [2, 3, 4]
In [5]: ultimo
Out[5]: 5


### Para entrar no serviço
❯ docker compose exec -ti api /bin/bash
app@e3fc8d3e808b:/home/api$ ^C
app@e3fc8d3e808b:/home/api$ todo shell
Auto imports: ['settings', 'engine', 'select', 'session', 'User']


### no container da app

docker exec -ti todo_project_api_1 /bin/bash
docker exec -ti todo_project_api_1 todo shell

todo shell
todo.models.user User
query = select(user)
print(query)

session.exec(query)
users = session.exec(query).all()
users -> volta vazio

user = User(name='Sergio', )
   
# .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-

import Typer

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


### commit da criação do CLI


 ## ***************************************************************************
 
 Comunidade  09/08/23

 ### Rever o conteudo do projeto
 Lei Geral de Proteção de Dados Pessoais (LGPD)
 Lei LGPD --> https://www.gov.br › mds › pt-br › acesso-a-informacao › lgpd


### inserir um lib para manipular o password e criar um função para normalizar o password
poetry add python-slugify

no cli.py inserir
 from slugify import slugify

 -vars = {
 ...
 slugify: slugify,
 ...
 }

 ### Dentro do file user.py fora da classe inserir

def gen_user_name(name: str) -> str:
    """Generate a slug """

### Faser o commit Instalado a lib python-slugify e criado a função


### inserir um lib para implementat o hash o password e criar um função para normalizar o password
poetry add passlib[bcrypt]

### altera o file default.toml -> inserir

[default.security]
# Set secret key_in .secrets.toml
# SECRET_KEY = ""
ALGORITHM = "HS256"
ACCES_TOKEN_EXPIRE_MINUTES = 20
REFRESH_TOKEN_EXPIRE_MINUTES = 600

### Criar arquivo na raiz .secrets.loml -> não deve subir para o githib

[development]
dynaconf_merge = true

[development.security]
SECRET_KEY = "128782340856cdef18becc37febf9e80176c714c9166b5632bbcfd6141a96a4e"


### Para gerar a secret_key com command python

python -c "print(__import__('secrets').token_hex(32))"
128782340856cdef18becc37febf9e80176c714c9166b5632bbcfd6141a96a4e

❯ openssl rand -hex 32                     
d7b57f4f10ce3d475363dc8698fc3e81eba20e2cee77d323fe1963183dde4664


### inserir no config

Validator

setting.validators.register:
    Validator('security.SECRET_KEY', must_exit=True, is_type_of=str)  -> faltou completar


  export TODO_SECRET_KEY=<security-key>
  printenv | grep TODO

  app@1e98e483d548:/home/api$ printenv | grep TODO
TODO_DB__connect_args={}
TODO_DB__uri=postgresql://postgres:postgres@db:5432/todo


### Serviço para guarda password
    lastpass ou onepass


### Segurança no file security.py inserir
"""Security utilities"""

from passlib.context import CryptContext
pwd_context = CryptContext(schemes=['bycrpt'].deprecated='auto')

def verify.password(plain_password: str, hashed_password: str) -> bool:
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
      """ Takes a plain text password and hashes it.

      We can use it a field on our SQLModel
      class User(SQLModel, table=True):
            user_name= str
            password = HashedPassword
      """

      @classmethod
      def __get_validators_(cls):
          yield cls.validate

      @classmethod
      def validate(cls, y):
          """ Accepts ...."""
          if not isinstance(v, str)
              raise TypeError('string required')
          
          hashed_password = get_password_hash(v)
          return cls(hashed_password)


### No file user.py

from Todo.security import HashedPassword
password = HashedPassword


No container 

user = User(name='plautz', email='plautz@email.com', password='1234',)

