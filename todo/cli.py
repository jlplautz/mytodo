from typing import Optional

import typer
from rich.console import Console
from rich.table import Table
from sqlmodel import Session, select

from todo.auth import authenticate_user
from todo.config import settings
from todo.db import engine
from todo.models import User, gen_user_name

main = typer.Typer(name='Todo CLI', add_completion=False)


@main.command()
def shell():
    """Opens interactive shell
    to run this shell into the container -> todo shell
    """
    _vars = {
        'settings': settings,
        'engine': engine,
        'select': select,
        'session': Session(engine),
        'gen_user_name': gen_user_name,
        'User': User,
        'authenticate_user': authenticate_user,
        'User': User,
    }

    typer.echo(f'Auto imports: {list(_vars.keys())}')
    try:
        from IPython import start_ipython

        start_ipython(
            argv=['--ipython-dir=/tmp', '--no-banner'], user_ns=_vars
        )
    except ImportError:
        import code

        code.InteractiveConsole(_vars).interact()


@main.command()
def hello():
    """Print Hello World"""
    print('Hello world')


@main.command()
def user_list():
    """List all users"""
    table = Table(title='Todo Users List')
    fields = ['name', 'user_name']
    for header in fields:
        table.add_column(header, style='cyan')

    with Session(engine) as session:
        users = session.exec(select(User).where(User.active))
        for user in users:
            table.add_row(
                *[getattr(user, field) for field in fields]
            )  # *[] para desempacotar uma lista

    Console().print(table)


@main.command()
def create_user(
    name: str, email: str, password: str, user_name: Optional[str] = None
):
    """Create a new uer."""
    with Session(engine) as session:
        user = User(
            name=name,
            email=email,
            password=password,
            user_name=user_name or gen_user_name(name),
        )
    session.add(user)
    session.commit()
    session.refresh(user)
    typer.echo(f'created {user.user_name} user.')
    return user
