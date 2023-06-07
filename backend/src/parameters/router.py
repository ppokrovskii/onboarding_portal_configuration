from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from . import service
from .dependencies import valid_parameter_create
from .schemas import Parameter, ParameterCreate
from ..dependencies import get_db

# from .schemas import ParameterCreate

router = APIRouter()


@router.get("/",
            response_model_exclude_none=True, )
async def get_parameters(db: Session = Depends(get_db)) -> list[Parameter]:
    parameters = service.get_parameters(db)
    parameters = parameters or []
    return parameters


@router.get("/name/{name}",
            response_model_exclude_none=True,
            )
def get_parameter_by_name(name: str, db: Session = Depends(get_db)) -> Parameter:
    parameter = service.get_parameter_by_name(db, name=name)
    if parameter is None:
        raise HTTPException(status_code=404, detail=f"Parameter with name {name} not found")
    return parameter


@router.post("/",
             # response_model=Parameter,
             response_model_exclude_none=True,
             status_code=status.HTTP_201_CREATED,
             )
def create_parameter(parameter: ParameterCreate = Depends(valid_parameter_create),
                     db: Session = Depends(get_db)) -> Parameter:
    return service.create_parameter(db, parameter)
