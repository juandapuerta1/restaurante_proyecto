"""
Endpoints para gestión de Restaurantes
"""

from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api.schemas.restaurante_schema import (
    RestauranteCreate,
    RestauranteResponse,
    RestauranteUpdate,
)
from crud.restaurante_crud import RestauranteCRUD
from database.config import get_db

router = APIRouter(prefix="/restaurantes", tags=["Restaurantes"])


@router.post(
    "/", response_model=RestauranteResponse, status_code=status.HTTP_201_CREATED
)
def crear_restaurante(restaurante: RestauranteCreate, db: Session = Depends(get_db)):
    try:
        crud = RestauranteCRUD(db)
        nuevo = crud.crear_restaurante(**restaurante.model_dump())
        return nuevo
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear restaurante: {e}")


@router.get("/", response_model=List[RestauranteResponse])
def listar_restaurantes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        crud = RestauranteCRUD(db)
        return crud.obtener_restaurantes(skip=skip, limit=limit)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al listar restaurantes: {e}"
        )


@router.get("/{restaurante_id}", response_model=RestauranteResponse)
def obtener_restaurante(restaurante_id: UUID, db: Session = Depends(get_db)):
    try:
        crud = RestauranteCRUD(db)
        restaurante = crud.obtener_restaurante(restaurante_id)
        if not restaurante:
            raise HTTPException(status_code=404, detail="Restaurante no encontrado")
        return restaurante
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al obtener restaurante: {e}"
        )


@router.put("/{restaurante_id}", response_model=RestauranteResponse)
def actualizar_restaurante(
    restaurante_id: UUID, restaurante: RestauranteUpdate, db: Session = Depends(get_db)
):
    try:
        crud = RestauranteCRUD(db)
        datos = restaurante.model_dump(exclude_unset=True)
        if not datos:
            raise HTTPException(status_code=400, detail="Sin datos para actualizar")

        actualizado = crud.actualizar_restaurante(restaurante_id, **datos)
        if not actualizado:
            raise HTTPException(status_code=404, detail="Restaurante no encontrado")
        return actualizado
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al actualizar restaurante: {e}"
        )


@router.delete("/{restaurante_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_restaurante(restaurante_id: UUID, db: Session = Depends(get_db)):
    try:
        crud = RestauranteCRUD(db)
        if not crud.eliminar_restaurante(restaurante_id):
            raise HTTPException(status_code=404, detail="Restaurante no encontrado")
        return None
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Error al eliminar restaurante: {e}"
        )
