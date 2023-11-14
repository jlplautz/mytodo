from fastapi import APIRouter, Response, status
from fastapi.exceptions import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlmodel import Session

from todo.auth import AuthenticatedUser, SuperUser
from todo.db import ActiveSession
from todo.models import (
    User,
    UserDetailResponse,
    UserRequest,
    UserResponse,
    get_user,
)

router = APIRouter()


@router.get(
    '/', response_model=list[UserResponse], dependencies=[AuthenticatedUser]
)
async def list_users():
    """List all users."""
    users = get_user()
    return users


@router.get(
    '/{user_name}/',
    response_model=UserDetailResponse,
    dependencies=[AuthenticatedUser],
)
async def get_user_by_user_name(*, user_name: str):
    """Get user by user_name."""
    user = get_user(user_name=user_name)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='User not found.'
        )
    return user


@router.post(
    '/',
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[SuperUser],
)
async def create_user(*, user: UserRequest, session: Session = ActiveSession):
    """Create new user"""
    # TODO: Validar informaçoes recebidas com as constraints do banco

    db_user = User.from_orm(user)
    session.add(db_user)
    try:
        session.commit()
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail='Email or user-name already exist.',
        )
    session.refresh(db_user)
    return db_user


@router.delete(
    '/{user_name}/',
    response_model=UserDetailResponse,
    dependencies=[AuthenticatedUser],
)
async def delete_user_by_user_name(
    *, user_name: str, session: Session = ActiveSession
):
    """Get user by user_name."""
    user = get_user(user_name=user_name)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='User not found.'
        )
    session.delete(user)
    session.commit()
    return Response(status_code=200)


# @router.put(
#     '/{user_name}/',
#     response_model=UserDetailResponse,
#     dependencies=[AuthenticatedUser],
# )
# async def update_user(*, user: UserRequest, session: Session = ActiveSession):
#     db_user = User.from_orm(user)
#     session.add(db_user)

#     user = get_user(user_name=user_name)
#     if not user:
#          status_code=status.HTTP_404_NOT_FOUND, detail='User not found.'

#     user.user_name = user.user_name
#     user.password = user.password
#     user.email = user.email
#     user.super_user = user.super_user

#     session.commit()
#     session.refresh(user)

#     return user
