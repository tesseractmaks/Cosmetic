from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship
from cosmetic_app.db.base_class import Base

if TYPE_CHECKING:
    from cosmetic_app.models import Product


class Tag(Base):
    title: Mapped[str]
    products_assoc: Mapped[list["Product"]] = relationship(secondary="associate_tags", back_populates="tags_assoc")

    def __str__(self):
        return f"{self.__class__.__name__}, title={self.title}"

    def __repr__(self):
        return str(self)