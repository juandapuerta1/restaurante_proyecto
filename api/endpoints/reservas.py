"""
Endpoints para gestión de Reservas
"""

from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api.schemas.reserva_schema import ReservaCreate, ReservaResponse, ReservaUpdate
from crud.reserva_crud import ReservaCRUD
from database.config import get_db

router = APIRouter(prefix="/reservas", tags=["Reservas"])


@router.post("/", response_model=ReservaResponse, status_code=status.HTTP_201_CREATED)
def crear_reserva(reserva: ReservaCreate, db: Session = Depends(get_db)):
    """
    Crear una nueva reserva
    """
    try:
        crud = ReservaCRUD(db)
        nueva = crud.crear_reserva(**reserva.model_dump())
        return nueva
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear reserva: {e}")


@router.get("/", response_model=List[ReservaResponse])
def listar_reservas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Listar todas las reservas
    """
    try:
        crud = ReservaCRUD(db)
        return crud.obtener_reservas(skip=skip, limit=limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al listar reservas: {e}")


@router.get("/{reserva_id}", response_model=ReservaResponse)
def obtener_reserva(reserva_id: UUID, db: Session = Depends(get_db)):
    """
    Obtener una reserva por ID
    """
    try:
        crud = ReservaCRUD(db)
        reserva = crud.obtener_reserva(reserva_id)
        if not reserva:
            raise HTTPException(status_code=404, detail="Reserva no encontrada")
        return reserva
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener reserva: {e}")


@router.put("/{reserva_id}", response_model=ReservaResponse)
def actualizar_reserva(
    reserva_id: UUID, reserva: ReservaUpdate, db: Session = Depends(get_db)
):
    """
    Actualizar una reserva existente
    """
    try:
        crud = ReservaCRUD(db)
        datos = reserva.model_dump(exclude_unset=True)
        if not datos:
            raise HTTPException(status_code=400, detail="Sin datos para actualizar")

        actualizada = crud.actualizar_reserva(reserva_id, **datos)
        if not actualizada:
            raise HTTPException(status_code=404, detail="Reserva no encontrada")
        return actualizada
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar reserva: {e}")


@router.delete("/{reserva_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_reserva(reserva_id: UUID, db: Session = Depends(get_db)):
    """
    Eliminar una reserva
    """
    try:
        crud = ReservaCRUD(db)
        if not crud.eliminar_reserva(reserva_id):
            raise HTTPException(status_code=404, detail="Reserva no encontrada")
        return None
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar reserva: {e}")
