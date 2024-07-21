from fastapi import APIRouter, Depends
from typing import Annotated
from repository import TaskRepository
from schemas import *

router = APIRouter(prefix ="/tasks", tags=["Таски"] )

@router.post("")
async def add_task(
    task: Annotated[STaskAdd, Depends()],
) -> STaskID:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True, "task_id": task_id}

@router.get("")
async def get_task() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks
