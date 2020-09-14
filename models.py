from datetime import datetime
import enum
from sqlalchemy.orm import deferred, relationship, backref
from sqlalchemy import Boolean, Column, Date, Integer, String, Text, ARRAY, ForeignKey, Table, Enum

from database import Base

couple_couple = Table(
    'couples', Base.metadata,
    Column('couple_id', Integer, primary_key=True),
    Column('first_taster_id', Integer, ForeignKey('tasters.taster_id')),
    Column('second_taster_id', Integer, ForeignKey('tasters.taster_id'))
)


class FoodTypeEnum(enum.Enum):
    appetizer = "appetizer"
    first_course = "first_course"
    main_course = "main_course"
    dessert = "dessert"
    other = "other"


class Taster(Base):
    __tablename__ = "tasters"

    taster_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    review = relationship("Review", back_populates="tasters")
    alias = Column(String, unique=True, index=True)

    couple = relationship(
        'Taster',
        secondary=couple_couple,
        primaryjoin=taster_id == couple_couple.c.first_taster_id,
        secondaryjoin=taster_id == couple_couple.c.second_taster_id,
        backref=backref('couples')
    )


class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    foodtype = Column(Enum(FoodTypeEnum))
    ingredients = Column(Text)
    directions = deferred(Column(Text, nullable=True))
    already_cooked = Column(Boolean, default=False)
    created_date = Column(Date, default=datetime.today())
    thermomix_recipe = Column(Boolean, default=True)
    is_vegetarian = Column(Boolean, nullable=True)
    reviews = relationship("Review")


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    observations = deferred(Column(Text, nullable=True))
    rating = Column(Integer, nullable=True)
    cooked_date = Column(Date, nullable=True)
    images = Column(ARRAY(String))
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    taster = relationship("Taster", uselist=False, back_populates="reviews")
