from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, func, text
from datetime import datetime

from cosmetic_app.db import Base


class Profile(Base):
    nickname: Mapped[str] = mapped_column(default="", server_default="")
    phone: Mapped[str] = mapped_column(default="", server_default="")
    photo: Mapped[str] = mapped_column(default="", server_default="")
    first_name: Mapped[str] = mapped_column(default="", server_default="")
    last_name: Mapped[str] = mapped_column(default="", server_default="")
    user_id: Mapped[int] = mapped_column(ForeignKey("User", ondelete="CASCADE"))

    user = relationship("User", uselist=False, back_populates="profile")
    created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now()"))
    updated_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now()"), onupdate=datetime.utcnow)

    def __str__(self):
        return f"{self.__class__.__name__}, nickname={self.nickname}"

    def __repr__(self):
        return str(self)
