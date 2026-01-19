from typing import TYPE_CHECKING
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import UserRelationMixin


class Profile(UserRelationMixin, Base):
    __tablename__ = "profiles"
    first_name: Mapped[str | None] = mapped_column(String(32))
    last_name: Mapped[str | None] = mapped_column(String(32))
    bio: Mapped[str | None] = mapped_column(String(128))
    _user_id_unique = True
    _user_back_populates = "profile"

    # user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)
