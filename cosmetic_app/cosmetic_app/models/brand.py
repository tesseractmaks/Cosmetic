from sqlalchemy.orm import Mapped, relationship

from cosmetic_app.db import Base


class Brand(Base):
    title: Mapped[str]
    products = relationship("Brand", back_populates="brands")

    def __str__(self):
        return f"{self.__class__.__name__}, title={self.title}"

    def __repr__(self):
        return str(self)