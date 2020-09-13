from enum import Enum
from typing import Optional

from pydantic import BaseModel


class FoodTypeEnum(str, Enum):
    appetizer = "appetizer"
    first_course = "first_course"
    main_course = "main_course"
    dessert = "dessert"
    other = "other"


class RecipeBase(BaseModel):
    name: str
    ingredients: str
    directions: str


class RecipeCreate(RecipeBase):
    pass


class Recipe(RecipeBase):
    id: int
    foodtype: Optional[FoodTypeEnum] = None
    observations: Optional[str] = None
    nonix_rating: Optional[int] = None
    reinus_rating: Optional[int] = None
    already_cooked: bool
    is_vegetarian: Optional[bool] = None

    class Config:
        # Read data from dict and class attributes (.whatever)
        orm_mode = True
