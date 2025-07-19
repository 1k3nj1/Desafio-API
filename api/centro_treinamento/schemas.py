from pydantic import UUID4, Field
from typing import Annotated
from api.contrib.schemas import BaseSchemas

class CentroTreinamentoIn(BaseSchemas):
    nome: Annotated[str, Field(description="Nome do centro de treinamento", example="CT 727", max_length=20)]
    endereco: Annotated[str, Field(description="Endereço do centro de treinamento", example="Rua tal, 1111", max_length=60)]
    proprietario: Annotated[str, Field(description="Proprietário do centro de treinamento", example="Arthur", max_length=30)]

class CentroTreinamentoAtleta(BaseSchemas):
    nome: Annotated[str, Field(description="Nome do centro de treinamento", example="CT 727", max_length=20)]

class CentroTreinamentoOut(CentroTreinamentoIn):
    idd: Annotated[UUID4, Field(description="Identificador do centro de treinamento")]

