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


class RecipeScrapperCreate(RecipeBase):
    pass


class RecipeCreate(RecipeBase):
    foodtype: Optional[FoodTypeEnum] = None
    already_cooked: bool
    thermomix_recipe: bool
    is_vegetarian: Optional[bool] = None


class Recipe(RecipeBase, RecipeCreate):
    id: int

    class Config:
        # Read data from dict and class attributes (.whatever)
        orm_mode = True
