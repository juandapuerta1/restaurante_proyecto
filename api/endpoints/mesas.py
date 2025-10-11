"""
Endpoints para gestión de Mesas
"""

from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api.schemas.mesa_schema import MesaCreate, MesaResponse, MesaUpdate
from crud.mesa_crud import MesaCRUD
from database.config import get_db

router = APIRouter(prefix="/mesas", tags=["Mesas"])


@router.post("/", response_model=MesaResponse, status_code=status.HTTP_201_CREATED)
def crear_mesa(mesa: MesaCreate, db: Session = Depends(get_db)):
    try:
        crud = MesaCRUD(db)
        nueva = crud.crear_mesa(**mesa.model_dump())
        return nueva
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear mesa: {e}")


@router.get("/", response_model=List[MesaResponse])
def listar_mesas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        crud = MesaCRUD(db)
        return crud.obtener_mesas(skip=skip, limit=limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al listar mesas: {e}")


@router.get("/{mesa_id}", response_model=MesaResponse)
def obtener_mesa(mesa_id: UUID, db: Session = Depends(get_db)):
    try:
        crud = MesaCRUD(db)
        mesa = crud.obtener_mesa(mesa_id)
        if not mesa:
            raise HTTPException(status_code=404, detail="Mesa no encontrada")
        return mesa
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener mesa: {e}")


@router.put("/{mesa_id}", response_model=MesaResponse)
def actualizar_mesa(mesa_id: UUID, mesa: MesaUpdate, db: Session = Depends(get_db)):
    try:
        crud = MesaCRUD(db)
        datos = mesa.model_dump(exclude_unset=True)
        if not datos:
            raise HTTPException(status_code=400, detail="Sin datos para actualizar")

        actualizada = crud.actualizar_mesa(mesa_id, **datos)
        if not actualizada:
            raise HTTPException(status_code=404, detail="Mesa no encontrada")
        return actualizada
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar mesa: {e}")


@router.delete("/{mesa_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_mesa(mesa_id: UUID, db: Session = Depends(get_db)):
    try:
        crud = MesaCRUD(db)
        if not crud.eliminar_mesa(mesa_id):
            raise HTTPException(status_code=404, detail="Mesa no encontrada")
        return None
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar mesa: {e}")
