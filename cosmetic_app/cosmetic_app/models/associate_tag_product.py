from sqlalchemy.orm import (Mapped,
                            mapped_column,
                            )
from sqlalchemy import UniqueConstraint
from sqlalchemy import ForeignKey

from cosmetic_app.db import Base


class AssociateTagProduct(Base):
    __tablename__ = "associate_tags"
    # __table_args__ = (
    #     UniqueConstraint(
    #         "tag_id",
    #         "product_id",
    #         name="idx_unique_t_p"
    #     ),
    # )

    id: Mapped[int] = mapped_column(primary_key=True)
    tag_id: Mapped[int] = mapped_column(ForeignKey("tags.id"), nullable=False)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"), nullable=False)





