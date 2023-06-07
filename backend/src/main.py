from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from .database import Base, engine
from .levels.router import router
from .features.router import router as features_router
from .parameters.router import router as parameters_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/api/levels")
app.include_router(features_router, prefix="/api/features")
app.include_router(parameters_router, prefix="/api/parameters")


@app.get("/", response_class=PlainTextResponse)
def home() -> str:
    return "http://localhost:8000/docs"
