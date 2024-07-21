from database import new_session, TaskOrm
from sqlalchemy import select
from schemas import *
 

class TaskRepository: 
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session: 
            task_dict = data.model_dump()

            task = TaskOrm(**task_dict)
            session.add(task)
            # flush вносит все изменения как команды, но не позволяет им выполниться(сохраниться)
            await session.flush()
            # сохраняет всё
            await session.commit()
            return task.id

    # Возвращаем все строки из бд в качестве списка экземляров класса STask (благодаря парсингу)
    @classmethod
    async def find_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskOrm)
            # итератор 
            result = await session.execute(query)
            task_models = result.scalars().all() 
            return task_models
        
    