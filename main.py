# pyrefly: ignore [missing-import]
from fastapi import FastAPI
from src.utils.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Mgmt Api", description="Task Mgmt Api", version="1.0.0")