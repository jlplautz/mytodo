"""Database connection"""
from fastapi import Depends
from sqlmodel import create_engine, Session

from todo.config import settings

engine = create_engine(
    settings.db.uri,
    echo=settings.db.echo,
    connect_args=settings.db.connect_args,
)


def get_session():
    # com gerador de context -> função geradora que cria a session e devolve
    with Session(engine) as session:
        yield session


ActiveSession = Depends(get_session)

# desta forma criamos um dependencia para injectar na views a session
