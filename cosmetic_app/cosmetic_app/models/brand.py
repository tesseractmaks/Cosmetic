from sqlalchemy.orm import Mapped, relationship

from cosmetic_app.db import Base


class Brand(Base):
    title: Mapped[str]
    products = relationship("Brand", back_populates="brands")