from sqlalchemy.orm import Mapped, relationship

from cosmetic_app.db.base_class import Base


class Brand(Base):
    title: Mapped[str]
    products = relationship("Product", back_populates="brand")

    def __str__(self):
        return f"{self.__class__.__name__}, title={self.title}"

    def __repr__(self):
        return str(self)