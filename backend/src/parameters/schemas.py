from pydantic import BaseModel

from src.features.schemas import Feature
from src.levels.schemas import Level


# [
#     {
#         "name": "Financial Institution - Name",
#         "col_code": "nic-fi-name",
#         "level": {
#             "name": "Tenant",
#             "parent": null,
#             "sub_level": null
#         },
#         "features": [
#             {
#                 "name": "Basic Details",
#                 "parent": null
#             }
#         ]
#     },
#     {
#         "name": "DCC Fees Do Not Block on Auth",
#         "col_code": "nic-ips-dcc-fees-fin-only-retail",
#         "level": {
#             "name": "PCT",
#             "parent": null,
#             "sub_level": null
#         },
#         "features": [
#             {
#                 "name": "Transaction Fees",
#                 "parent": "Fees"
#             }
#         ]
#     }
# ]

class ParameterBase(BaseModel):
    name: str
    col_code: str
    level: str
    features: list[str]


class ParameterCreate(ParameterBase):
    pass


class Parameter(ParameterBase):
    # id: int
    level: Level
    features: list[Feature]

    class Config:
        orm_mode = True
