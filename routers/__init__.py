from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from .. import crud, models, schemas
from .. database import SessionLocal