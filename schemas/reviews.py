from datetime import date
from typing import Optional, List

from pydantic import BaseModel
from . import tasters


class ReviewBase(BaseModel):
    observations: str
    rating: int
    cooked_date: date
    images: Optional[List[str]] = None
    recipe_id: int
    taster: tasters.Taster


class ReviewCreate(ReviewBase):
    pass


class Review(ReviewBase):
    id: int
