from sqlalchemy.orm import Session

import models
import schemas


def get_recipe_by_name(db: Session, name: str):
    return db.query(models.Recipe).filter(models.Recipe.name == name).first()


def get_recipes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Recipe).offset(skip).limit(limit).all()


def create_recipe(db: Session, recipe: schemas.RecipeCreate):
    new_recipe = models.Recipe(
        name=recipe.name,
        foodtype=recipe.foodtype,
        ingredients=recipe.ingredients,
        directions=recipe.directions,
        observations=recipe.observations,
        nonix_rating=recipe.rating,
        reinus_rating=recipe.rating,
        cooked=recipe.already_cooked,
        vegetarian=recipe.vegetarian,
    )
    db.add(new_recipe)
    db.commit()
    db.refresh(new_recipe)
    return new_recipe
