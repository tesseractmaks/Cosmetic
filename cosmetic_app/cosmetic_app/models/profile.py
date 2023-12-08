import uuid

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, func, text
from datetime import datetime

from cosmetic_app.db import Base


class Profile(Base):
    nickname: Mapped[str] = mapped_column(default="t", server_default="y")
    phone: Mapped[str] = mapped_column(default="", server_default="")
    photo: Mapped[str] = mapped_column(default="", server_default="")
    first_name: Mapped[str] = mapped_column(default="t", server_default="y")
    last_name: Mapped[str] = mapped_column(default="t", server_default="y")

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("usermodels.id", ondelete="CASCADE"))

    user = relationship("UserModel", uselist=False, back_populates="profile", lazy='joined')

    created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
    updated_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"), onupdate=datetime.utcnow)

    def __str__(self):
        return f"{self.__class__.__name__}, nickname={self.nickname}"

    def __repr__(self):
        return str(self)
