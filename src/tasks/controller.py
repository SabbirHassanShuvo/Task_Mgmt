from src.tasks.dtos import TaskDTO


def create_task(body: TaskDTO):
    print(body.model_dump())
    return {"message": "Task created"}