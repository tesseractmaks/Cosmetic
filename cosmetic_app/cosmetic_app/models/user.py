from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, func, text
from datetime import datetime

from cosmetic_app.db import Base


class UserModel(Base):
    email: Mapped[str]
    password: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    is_active: Mapped[bool]

    profile = relationship("Profile", uselist=False, back_populates="user", lazy='joined')

    created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    updated_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.utcnow)

    def __str__(self):
        return f"{self.__class__.__name__}, email={self.email}, is_active={self.is_active}"

    def __repr__(self):
        return str(self)