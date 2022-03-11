from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from fastapi import Body
from pathlib import Path

from app.v1.schema import client_schema
from app.v1.service import client_service

from app.v1.utils.db import get_db


router = APIRouter(prefix="/api/v1/cuenta")

