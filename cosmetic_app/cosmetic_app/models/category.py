from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from cosmetic_app.db import Base


class Category(Base):
    __tablename__ = "categories"
    title: Mapped[str]
    products = relationship("Product", back_populates="categories")

    def __str__(self):
        return f"{self.__class__.__name__}, title={self.title}"

    def __repr__(self):
        return str(self)
