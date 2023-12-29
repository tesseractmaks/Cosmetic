from sqlalchemy import UniqueConstraint
from sqlalchemy import ForeignKey
from sqlalchemy.orm import (Mapped,
                            mapped_column,
                            )
from cosmetic_app.db import Base


class AssociateCategoryProduct(Base):
    __tablename__ = "associate_categories"
    # __table_args__ = (
        # UniqueConstraint(
        #     "category_id",
        #     "product_id",
        #     name="idx_unique_c_p"
        # ),
    # )

    id: Mapped[int] = mapped_column(primary_key=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)
