from typing import Annotated, Optional
from pydantic import BaseModel, Field, PositiveFloat

from api.categorias.schemas import CategoriaIn
from api.centro_treinamento.schemas import CentroTreinamentoAtleta
from api.contrib.schemas import BaseSchemas, OutMixin

class Atleta(BaseSchemas):
    nome: Annotated[str, Field(description="Nome do atleta", example="Henrique", max_length=50)]
    cpf: Annotated[str, Field(description="CPF do atleta", example="11111111111", max_length=11)]
    idade: Annotated[int, Field(description="CPF do atleta", example=20)]
    peso: Annotated[PositiveFloat, Field(description="CPF do atleta", example=75.5)]
    altura: Annotated[PositiveFloat, Field(description="Altura do atleta", example=170.4)]
    sexo: Annotated[str, Field(description="Sexo do atleta", example="M", max_length=1)]
    categoria : Annotated[CategoriaIn, Field(description="Categoria do atleta")]
    centro_treinamento : Annotated[CentroTreinamentoAtleta, Field(description="Centro de treinamento do atleta")]

class AtletaIn(Atleta):
    pass

class AtletaOut(Atleta, OutMixin):
    pass    

class AtletaUpdate(BaseSchemas):
    nome: Annotated[Optional[str], Field(None, description="Nome do atleta", example="Henrique", max_length=50)]
    idade: Annotated[Optional[int], Field(None, description="CPF do atleta", example=20)]