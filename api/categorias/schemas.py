from pydantic import UUID4, Field
from typing import Annotated
from api.contrib.schemas import BaseSchemas

class CategoriaIn(BaseSchemas):
    nome: Annotated[str, Field(description="Nome do categoria", example="Scale", max_length=10)]

class CategoriaOut(CategoriaIn):
    idd: Annotated[UUID4, Field(description="Identificador da categoria")]
