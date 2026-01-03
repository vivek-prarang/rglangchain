from sqlalchemy import String, Boolean,Numeric, ForeignKey,DateTime,Enum as SqlEnum
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.core.database import Base
from datetime import datetime
from enum import Enum


class CartStatus(str, Enum):
    init = "init"
    proccess="proccess"
    processed = "processed"


class Cart(Base):
	__tablename__="carts"
	id : Mapped[int]=mapped_column(primary_key=True, index=True, nullable=False)
	user_id: Mapped[int] = mapped_column(
			ForeignKey('users.id',ondelete="CASCADE"), nullable=False
		)
	status: Mapped[str]=mapped_column(SqlEnum(CartStatus),default=CartStatus.init)
	created_at: Mapped[datetime]=mapped_column(DateTime, default=datetime.utcnow)
	updated_at:  Mapped[datetime | None]=mapped_column(DateTime, default=datetime.utcnow, nullable=True)
	deleted_at: Mapped[datetime | None]=mapped_column(DateTime, nullable=True)
	# Relations
	items= relationship(CartItems, back_populates="cart", cascade="all, delete-orphan")

class CartItems(Base):
	__tablename__="cart_items"

	id : Mapped[int]=mapped_column(primary_key=True, index=True, nullable=False)
	cart_id: Mapped[int]=mapped_column(
			ForeignKey('carts.id', ondelete='CASCADE'), index=True, nullable=False
		)
	product_id: Mapped[int]= mapped_column(
			ForeignKey("products.id", ondelete="CASCADE"), index=True, nullable=False
		)
	quantity:Mapped[int]= mapped_column(Numeric(10), nullable=False, default=1)
	price :Mapped[float]= mapped_column(Numeric(10,2), nullable=False)
	created_at: Mapped[datetime]=mapped_column(DateTime, default=datetime.utcnow)
  	updated_at:  Mapped[datetime | None]=mapped_column(DateTime, default=datetime.utcnow, nullable=True)

  	# Relation Ship

  	cart=relationship(
  		"Cart",
  		back_populates="items"
  		)
