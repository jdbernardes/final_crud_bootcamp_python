from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database.database import Base


class ProductModel(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    category = Column(String, index=True)
    suplier_email = Column(String)
    created_at = Column(DateTime(timezone=True), default=func.now())
