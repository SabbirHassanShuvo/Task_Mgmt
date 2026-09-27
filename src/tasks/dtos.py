from pydantic import BaseModel


class TaskDTO(BaseModel):
    title: str
    description: str
    is_completed: bool = False