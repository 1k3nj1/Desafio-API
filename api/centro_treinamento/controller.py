from uuid import uuid4
from fastapi import APIRouter, HTTPException, status, Body
from pydantic import UUID4

from api.centro_treinamento.schemas import CentroTreinamentoIn, CentroTreinamentoOut
from api.contrib.dependencies import DatabaseDependency
from api.centro_treinamento.models import CentroTreinamentoModel
from sqlalchemy.future import select

router = APIRouter()

@router.post(
        '/',
        summary="Criar novo centro de treinamento",
        status_code=status.HTTP_201_CREATED,
        response_model=CentroTreinamentoOut
        )
async def post(
    db_session: DatabaseDependency, centro_treinamento_in: CentroTreinamentoIn = Body(...)
    ) -> CentroTreinamentoOut:
    
    centro_treinamento_out = CentroTreinamentoOut(id=uuid4(), **centro_treinamento_in.model_dump())
    centro_treinamento_model = CentroTreinamentoModel(**centro_treinamento_out.model_dump())

    db_session.add(centro_treinamento_model)
    await db_session.commit()

    return centro_treinamento_out

@router.get(
        '/',
        summary="Consultar todas os centros de treinamento",
        status_code=status.HTTP_200_OK,
        response_model=list[CentroTreinamentoOut]
        )
async def query(db_session: DatabaseDependency) -> list[CentroTreinamentoOut]:
    cts: list[CentroTreinamentoOut] = [
        await db_session.execute(select(CentroTreinamentoModel))].scalars().all()

    return cts


@router.get(
        '/{id}',
        summary="Consultar um centro de treinamento pelo ID",
        status_code=status.HTTP_200_OK,
        response_model=CentroTreinamentoOut
        )
async def query(idd: UUID4, db_session: DatabaseDependency) -> CentroTreinamentoOut:
    ct: CentroTreinamentoOut = await db_session.execute(select(CentroTreinamentoModel).filter_by(id=idd)).scalars().first()

    if not ct:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail=f"Centro de treinamento não encontrada pelo id = {idd}"
            )

    return ct