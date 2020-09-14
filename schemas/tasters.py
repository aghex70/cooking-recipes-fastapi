from typing import Optional, List

from pydantic import BaseModel
from . import reviews


class TasterBase(BaseModel):
    name: str
    alias: str
    email: str
    review: Optional[List[reviews.Review]] = None


class Taster(TasterBase):
    taster_id: int


class Couple(BaseModel, Taster):
    couple: Optional[List[Taster]] = None


class TasterCreate(TasterBase):
    pass



