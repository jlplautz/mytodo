### Dica.01- Quando executar alguma alterar no codigo da branch main

Executar:

```bash

1- git stash (guarda as alteraçoes)
2- git checkout -b <nova branch>
3- git stash pop (para trazer as alteraçoes para a <nova branch>)
```

## Dica.02- CMDs docker
  
  Qdo usamos um diretorio para volume as caracteristica deste diretorio é alterado para root
  
  Para resolve a task clean basta mover o diretorio .postgres para a diretorio home echo ~
  Alterar o file docker-compose.yml para apontar para o novo diretorio na home
 

## Dica.03- Para facilitar import da tabela User

Para facilitar o import da tabela User quando necessario
inserir no `__init__.py` do diretório models

```bash
 from sqlmode import SQLModel
 from .user import User
 
  __all__ * ['User', 'SQLModel']
  
```

## Dica.04- Alguns comandos docker
```bash
docker compose up
docker compose prone
docker container ls
docker compouse build --no-cache
docker compouse --rm -ti <name> /bin/bash

─$ docker compose up 

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
=================================== test session starts ======================
platform linux -- Python 3.11.1, pytest-7.4.0, pluggy-1.2.0 -- /usr/local/bin/python3.11
cachedir: .pytest_cache
rootdir: /home/api
configfile: pyproject.toml
plugins: order-1.1.0, anyio-3.7.1, cov-4.1.0
collected 2 items                                                                          

tests/test_main_api.py::test_main_api_works_ok PASSED                                [ 50%]
tests/test_main_api.py::test_main_api_has_docs PASSED                                [100%]

```

## Dica.05- Detalhes sobre Dynaconf
```bash
SQLAlchemy - ORM
SQLMODEL   - ORM

Dynaconf - arquivo para ver variaveis de ambiente ambiente / 
         - ler password  
         - decouple

ORM - sql puro  

alembic + sq

Quando usamos email para authenticar podemos deixar exposto o email dos users.
procurar não mostrar o email no list

 SQLMODEL é uma abstração do sqlalchemy
```


## Dica.06- Para ver as variaveis env
```bash
╰─$ printenv | grep todo
OLDPWD=/home/plautz/Proj_2023/mytodo
PWD=/home/plautz/Proj_2023/mytodo
```

## Dica.07- Alguns commands na api todo
Para entrar no serviço
no container da app

```bash
❯ docker compose exec -ti api /bin/bash
app@e3fc8d3e808b:/home/api$ todo shell
Auto imports: ['settings', 'engine', 'select', 'session', 'User']

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
```

## Dica.08- Como despacotar uma lista
```bash
In [1]: lista = [1,2,3,4,5]
In [2]: primeiro, *meio, ultimo = lista
In [3]: primeiro
Out[3]: 1
In [4]: meio
Out[4]: [2, 3, 4]
In [5]: ultimo
Out[5]: 5
```


## Dica.09- Lei Geral de Proteção de Dados Pessoais (LGPD)
 Lei LGPD --> https://www.gov.br › mds › pt-br › acesso-a-informacao › lgpd


 Como verifiar variaveis de ambiente export TODO_SECRET_KEY=<security-key>
printenv | grep TODO

❯ docker compose exec api /bin/bash
                                              
app@fb9e47fdc11f:/home/api$ printenv | grep TODO
TODO_DB__connect_args={}
TODO_DB__uri=postgresql://postgres:postgres@db:5432/todo



## Dica.11- Serviço para guardar password
lastpass ou onepass



## Dica.12- Tipos primitivos do Python
```bash
>>> type('')
<class 'str'>
>>> type(1)
<class 'int'>
>>> type(1.0)
<class 'float'>
>>> 'jorge'.upper()
'JORGE'
>>> ''.__dir__() -> o que podemos user são os metodos sem o dunder
['__new__', '__repr__', '__hash__', '__str__', '__getattribute__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__iter__', '__mod__', '__rmod__', '__len__', '__getitem__', '__add__', '__mul__', '__rmul__', '__contains__', 'encode', 'replace', 'split', 'rsplit', 'join', 'capitalize', 'casefold', 'title', 'center', 'count', 'expandtabs', 'find', 'partition', 'index', 'ljust', 'lower', 'lstrip', 'rfind', 'rindex', 'rjust', 'rstrip', 'rpartition', 'splitlines', 'strip', 'swapcase', 'translate', 'upper', 'startswith', 'endswith', 'removeprefix', 'removesuffix', 'isascii', 'islower', 'isupper', 'istitle', 'isspace', 'isdecimal', 'isdigit', 'isnumeric', 'isalpha', 'isalnum', 'isidentifier', 'isprintable', 'zfill', 'format', 'format_map', '__format__', 'maketrans', '__sizeof__', '__getnewargs__', '__doc__', '__setattr__', '__delattr__', '__init__', '__reduce_ex__', '__reduce__', '__getstate__', '__subclasshook__', '__init_subclass__', '__dir__', '__class__']

>>> 'a'. __lt__ ('b')
True
>>> 'a' < 'b'
True
>>> mydict = {}
>>> type(mydict)
<class 'dict'>
```

## Dica.13- salvar user no banco
```bash
app@8c71e385edd2:/home/api$ todo shell
Auto imports: ['settings', 'engine', 'select', 'session', 'gen_user_name', 'User']

In [1]: user = User(name='Jorge Plautz', email='plautz@email.com', password='1234',user_name='plautz')

In [2]: user
Out[2]: User(id=None, name='Jorge Plautz', email='plautz@email.com', password='$2b$12$pYXHdgj.nNCaqSkRonMsAeZPCvvcVqdpO.REUNCx6na9a2r3WeLYG', user_name='plautz', active=True, created_at=datetime.datetime(2023, 8, 14, 21, 59, 57, 191367), updated_at=datetime.datetime(2023, 8, 14, 21, 59, 57, 191372))

In [3]: session.add(user)

In [4]: session.commit()
In [6]: user.id
Out[6]: 1
In [9]: session.refresh(user)
```

 Caso tenha feito o git add das alterações na branch main, para reverter

1- git status  -> para verific ar os arquivos que foram colocados no stagge (verde)

2- git restore --staged <arquivo.py> <arquivo1.py>  -> para remover do stagge

3- git status -> os arquivos devem aparecer na cor vermelha (file untracked)

4- -> depois executar stash all changes (inserir nome que será solicitado)


## Dica.15- Verificar setting flake8
```bash
 flake8 instalar a lib
 poetry add --group dev flake8-pyproject

 no file pyproject.toml abaixo do task

 [tool.flake8]
 max-line-length = 120
 ```

## Dica.16- Comandos docker
```bash
❯ docker compose exec api todo shell 
Auto imports: ['settings', 'engine', 'select', 'session', 'gen_user_name', 'User']

In [1]: query = select(User)
In [2]: print(query)
SELECT "user".id, "user".name, "user".email, "user".password, "user".user_name, "user".active, "user".created_at, "user".updated_at 
FROM "user"

In [3]: users = session.exec(query).all()
In [4]: users
Out[4]: 
[User(email='plautz@email.com', user_name='plautz', created_at=datetime.datetime(2023, 8, 14, 21, 59, 57, 191367), name='Jorge Plautz', password='$2b$12$pYXHdgj.nNCaqSkRonMsAeZPCvvcVqdpO.REUNCx6na9a2r3WeLYG', id=1, active=True, updated_at=datetime.datetime(2023, 8, 14, 21, 59, 57, 191372)),
 User(email='gabi@gmail.com', user_name='gabriela-plautz', created_at=datetime.datetime(2023, 8, 18, 21, 54, 8, 156661), name='Gabriela Plautz', password='$2b$12$YzqiLP5LkuVd9tdspxpe5.pJh7Ju2wSmZ2Y2qBb9wMYkps4PAk2gK', id=7, active=True, updated_at=datetime.datetime(2023, 8, 18, 21, 54, 8, 156665)),
 User(email='jlp@gmail.com', user_name='jorge', created_at=datetime.datetime(2023, 8, 18, 20, 30, 55, 509438), name='Jorge', password='$2b$12$pn2iDR1LXwHSYpDKT/pXKergA24uPbLs5WIWIbCdDoy1KORZqhqe.', id=2, active=True, updated_at=datetime.datetime(2023, 8, 18, 20, 30, 55, 509444)),
 User(email='llp@gmail.com', user_name='lindalene-plautz', created_at=datetime.datetime(2023, 8, 18, 21, 20, 7, 308983), name='Lindalene Plautz', password='$2b$12$XwUjDItPCb5PijZpClx1Q.2CbzteBPzVFWWouHT/QOF85YS/vtudu', id=3, active=True, updated_at=datetime.datetime(2023, 8, 18, 21, 20, 7, 308989)),
 User(email='rafa@gmail.com', user_name='rafaela-plautz', created_at=datetime.datetime(2023, 8, 18, 21, 49, 28, 268458), name='Rafaela Plautz', password='$2b$12$DcwwQFGvSFV.EfTjAsyUG.pXW034WFcTsB6IMo/D61gNGbVclPSLS', id=4, active=True, updated_at=datetime.datetime(2023, 8, 18, 21, 49, 28, 268463)),
 User(email='test@email.com', user_name='teste-teste', created_at=datetime.datetime(2023, 8, 22, 11, 44, 8, 78616), name='Teste Teste', password='$2b$12$nl0QfJrztVt4GhnOtVDJ/uf4pSW.Pn.zUd9cW5uvp8CcpG773pF0e', id=9, active=True, updated_at=datetime.datetime(2023, 8, 22, 11, 44, 8, 78622))]

In [5]: query = select(User).where(User.user_name == 'plautz')

In [6]: print(query)
SELECT "user".id, "user".name, "user".email, "user".password, "user".user_name, "user".active, "user".created_at, "user".updated_at 
FROM "user" 
WHERE "user".user_name = :user_name_1
### parametro .first() -> para consumir o object scalar result 
### que retorna da query
In [7]: user = session.exec(query).first()

In [8]: user
Out[8]: User(email='plautz@email.com', user_name='plautz', created_at=datetime.datetime(2023, 8, 14, 21, 59, 57, 191367), name='Jorge Plautz', password='$2b$12$pYXHdgj.nNCaqSkRonMsAeZPCvvcVqdpO.REUNCx6na9a2r3WeLYG', id=1, active=True, updated_at=datetime.datetime(2023, 8, 14, 21, 59, 57, 191372))


❯ docker compose exec api todo shell
Auto imports: ['settings', 'engine', 'select', 'session', 'gen_user_name', 'User']

In [1]: from todo.models.user import get_user

In [2]: users = get_user()

In [3]: users
Out[3]: 
[User(email='plautz@email.com', user_name='plautz', created_at=datetime.datetime(2023, 8, 14, 21, 59, 57, 191367), name='Jorge Plautz', password='$2b$12$pYXHdgj.nNCaqSkRonMsAeZPCvvcVqdpO.REUNCx6na9a2r3WeLYG', id=1, active=True, updated_at=datetime.datetime(2023, 8, 14, 21, 59, 57, 191372)),
 User(email='gabi@gmail.com', user_name='gabriela-plautz', created_at=datetime.datetime(2023, 8, 18, 21, 54, 8, 156661), name='Gabriela Plautz', password='$2b$12$YzqiLP5LkuVd9tdspxpe5.pJh7Ju2wSmZ2Y2qBb9wMYkps4PAk2gK', id=7, active=True, updated_at=datetime.datetime(2023, 8, 18, 21, 54, 8, 156665)),
 User(email='jlp@gmail.com', user_name='jorge', created_at=datetime.datetime(2023, 8, 18, 20, 30, 55, 509438), name='Jorge', password='$2b$12$pn2iDR1LXwHSYpDKT/pXKergA24uPbLs5WIWIbCdDoy1KORZqhqe.', id=2, active=True, updated_at=datetime.datetime(2023, 8, 18, 20, 30, 55, 509444)),
 User(email='llp@gmail.com', user_name='lindalene-plautz', created_at=datetime.datetime(2023, 8, 18, 21, 20, 7, 308983), name='Lindalene Plautz', password='$2b$12$XwUjDItPCb5PijZpClx1Q.2CbzteBPzVFWWouHT/QOF85YS/vtudu', id=3, active=True, updated_at=datetime.datetime(2023, 8, 18, 21, 20, 7, 308989)),
 User(email='rafa@gmail.com', user_name='rafaela-plautz', created_at=datetime.datetime(2023, 8, 18, 21, 49, 28, 268458), name='Rafaela Plautz', password='$2b$12$DcwwQFGvSFV.EfTjAsyUG.pXW034WFcTsB6IMo/D61gNGbVclPSLS', id=4, active=True, updated_at=datetime.datetime(2023, 8, 18, 21, 49, 28, 268463)),
 User(email='test@email.com', user_name='teste-teste', created_at=datetime.datetime(2023, 8, 22, 11, 44, 8, 78616), name='Teste Teste', password='$2b$12$nl0QfJrztVt4GhnOtVDJ/uf4pSW.Pn.zUd9cW5uvp8CcpG773pF0e', id=9, active=True, updated_at=datetime.datetime(2023, 8, 22, 11, 44, 8, 78622))]

In [6]: user = get_user(user_name='teste-teste')

In [7]: user
Out[7]: User(email='test@email.com', user_name='teste-teste', created_at=datetime.datetime(2023, 8, 22, 11, 44, 8, 78616), name='Teste Teste', password='$2b$12$nl0QfJrztVt4GhnOtVDJ/uf4pSW.Pn.zUd9cW5uvp8CcpG773pF0e', id=9, active=True, updated_at=datetime.datetime(2023, 8, 22, 11, 44, 8, 78622))


❯ docker compose exec api todo shell
Auto imports: ['settings', 'engine', 'select', 'session', 'gen_user_name', 'User']

In [1]: user_name = 'jorge-luiz-plautz'

In [2]: query = select(User).where(User.user_name == user_name)

In [3]: print(query)
SELECT "user".id, "user".name, "user".email, "user".password, "user".user_name, "user".active, "user".created_at, "user".updated_at 
FROM "user" 
WHERE "user".user_name = :user_name_1
### Comando de SELECT similar via SQL
In [4]: SELECT * FROM "user" WHERE "user".user_name = 'jorge-luiz-plautz'
### a outra query do comando caso não tenha user_name
In [4]: query = select(User)

In [5]: print(query)
SELECT "user".id, "user".name, "user".email, "user".password, "user".user_name, "user".active, "user".created_at, "user".updated_at 
FROM "user"

### Verificar obejct ScalarResult
❯ docker compose exec api todo shell
Auto imports: ['settings', 'engine', 'select', 'session', 'gen_user_name', 'User']

In [1]: user_name='plautz'

In [2]: query = select(User).where(User.user_name == user_name)

In [3]: user = session.exec(query)

In [4]: user
Out[4]: <sqlalchemy.engine.result.ScalarResult at 0x7f69ae84cbd0>

In [5]: u = list(user)

In [6]: u
Out[6]: [User(email='plautz@email.com', user_name='plautz', created_at=datetime.datetime(2023, 8, 14, 21, 59, 57, 191367), name='Jorge Plautz', password='$2b$12$pYXHdgj.nNCaqSkRonMsAeZPCvvcVqdpO.REUNCx6na9a2r3WeLYG', id=1, active=True, updated_at=datetime.datetime(2023, 8, 14, 21, 59, 57, 191372))]
```


## Dica.17- Comandos para visualizar os logs do container API
```bash
docker compose logs api
```


## Dica.18- Video sobre contexto 
![contexto](https://www.youtube.com/watch?v=IM0o8dFE0WU)