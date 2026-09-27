from fastapi import APIRouter
from src.tasks import controller
from src.tasks.dtos import TaskDTO

task_router = APIRouter(prefix="/tasks")


@task_router.post("/create")
def create_task(body: TaskDTO):
    return controller.create_task(body)
