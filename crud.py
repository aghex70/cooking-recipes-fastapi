from typing import Union
import enum

from sqlalchemy.orm import Session

from models import Recipe
from schemas import (
    recipes as recipe_schema,
    reviews as reviews_schema,
    tasters as taster_schema
)


class FoodTypeEnum(enum.Enum):
    appetizer = "appetizer"
    first_course = "first_course"
    main_course = "main_course"
    dessert = "dessert"
    other = "other"


def get_recipe_by_name(db: Session, name: str):
    return db.query(Recipe).filter(Recipe.name == name).first()


def get_recipes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Recipe).offset(skip).limit(limit).all()


def get_user_favourite_recipes(db: Session, name: str):
    return db.query(Recipe)\
        .filter(Recipe.reviews.taster.name == name)\
        .order_by(Recipe.reviews.rating)


def get_random_recipe(db: Session, foodtype: FoodTypeEnum, already_cooked: bool = False):
    return db.query(Recipe) \
        .filter(Recipe.foodtype == foodtype.value, Recipe.already_cooked == already_cooked)\
        .one()


def get_recipes_by_ingredients(db: Session, foodtype: FoodTypeEnum, ingredients: Union[str, list]):
    return db.query(Recipe) \
        .filter(Recipe.foodtype == foodtype.value)\
        .all()


# def create_recipe(db: Session, recipe: recipe_schema.RecipeCreate):
#     new_recipe = Recipe(
#         name=recipe.name,
#         foodtype=recipe.foodtype,
#         ingredients=recipe.ingredients,
#         directions=recipe.directions,
#         observations=recipe.observations,
#         nonix_rating=recipe.rating,
#         reinus_rating=recipe.rating,
#         cooked=recipe.already_cooked,
#         vegetarian=recipe.vegetarian,
#     )
#     db.add(new_recipe)
#     db.commit()
#     db.refresh(new_recipe)
#     return new_recipe
