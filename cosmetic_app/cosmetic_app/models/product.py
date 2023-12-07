from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import String
from sqlalchemy import ForeignKey, func, text
from datetime import datetime
from typing import TYPE_CHECKING

from cosmetic_app.db import Base

if TYPE_CHECKING:
    from cosmetic_app.models import Brand, Category


class Product(Base):
    title: Mapped[str]
    article_number: Mapped[str] = mapped_column(unique=True)
    price: Mapped[int]
    image: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now()"))
    updated_at: Mapped[datetime] = mapped_column(server_default=text("TIMEZONE('utc', now()"), onupdate=datetime.utcnow)

    brand_id: Mapped[int] = mapped_column(ForeignKey("brand.id", ondelete="CASCADE"))
    category_id: Mapped[int] = mapped_column(ForeignKey("category.id", ondelete="CASCADE"))

    brand: Mapped["Brand"] = relationship("Brand", back_populates="products")
    categories: Mapped["Category"] = relationship("Category", back_populates="products")

    def __str__(self):
        return f"{self.__class__.__name__}, title={self.title}, price={self.price}, article_number={self.article_number}"

    def __repr__(self):
        return str(self)
