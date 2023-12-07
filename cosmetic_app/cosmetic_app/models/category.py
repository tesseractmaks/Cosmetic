from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from cosmetic_app.db import Base


class Category(Base):
    title: Mapped[str]
    products = relationship("Product", back_populates="categories")
