from pydantic import BaseModel, ConfigDict
from typing import Optional

class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None

class STask(STaskAdd):
    id: int
    # парсинг при работе с бд
    model_config = ConfigDict(from_attributes=True)

class STaskID(BaseModel):
    ok: bool = True
    task_id: int