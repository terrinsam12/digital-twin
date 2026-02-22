from fastapi import APIRouter
from main_service import service

router = APIRouter()

@router.get("/machine")
def get_machine():
    return service.get_machine_state()