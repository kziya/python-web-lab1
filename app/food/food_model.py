from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.db import Base


class Food(Base):
    __tablename__ = 'foods'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    price = Column(Float, nullable=False)

    orders = relationship("Order", back_populates="food")
