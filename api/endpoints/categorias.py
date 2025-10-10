"""
Endpoints para gestión de Categorías
"""

from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api.schemas.categoria_schema import (
    CategoriaCreate,
    CategoriaResponse,
    CategoriaUpdate,
)
from crud.categoria_crud import CategoriaCRUD
from database.config import get_db

# IMPORTANTE: Esta línea debe estar aquí
router = APIRouter(prefix="/categorias", tags=["Categorías"])


@router.post("/", response_model=CategoriaResponse, status_code=status.HTTP_201_CREATED)
def crear_categoria(categoria: CategoriaCreate, db: Session = Depends(get_db)):
    """
    Crear una nueva categoría
    """
    try:
        crud = CategoriaCRUD(db)
        nueva_categoria = crud.crear_categoria(
            nombre=categoria.nombre, descripcion=categoria.descripcion
        )
        return nueva_categoria
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al crear categoría: {str(e)}",
        )


@router.get("/", response_model=List[CategoriaResponse])
def listar_categorias(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Listar todas las categorías activas
    """
    try:
        crud = CategoriaCRUD(db)
        categorias = crud.obtener_categorias(skip=skip, limit=limit)
        return categorias
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al listar categorías: {str(e)}",
        )


@router.get("/{categoria_id}", response_model=CategoriaResponse)
def obtener_categoria(categoria_id: UUID, db: Session = Depends(get_db)):
    """
    Obtener una categoría por ID
    """
    try:
        crud = CategoriaCRUD(db)
        categoria = crud.obtener_categoria(categoria_id)
        if not categoria:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Categoría no encontrada"
            )
        return categoria
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener categoría: {str(e)}",
        )


@router.put("/{categoria_id}", response_model=CategoriaResponse)
def actualizar_categoria(
    categoria_id: UUID, categoria: CategoriaUpdate, db: Session = Depends(get_db)
):
    """
    Actualizar una categoría existente
    """
    try:
        crud = CategoriaCRUD(db)

        datos_actualizacion = categoria.model_dump(exclude_unset=True)

        if not datos_actualizacion:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No se proporcionaron datos para actualizar",
            )

        categoria_actualizada = crud.actualizar_categoria(
            categoria_id, **datos_actualizacion
        )

        if not categoria_actualizada:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Categoría no encontrada"
            )

        return categoria_actualizada
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al actualizar categoría: {str(e)}",
        )


@router.delete("/{categoria_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_categoria(categoria_id: UUID, db: Session = Depends(get_db)):
    """
    Eliminar una categoría (soft delete)
    """
    try:
        crud = CategoriaCRUD(db)
        if not crud.eliminar_categoria(categoria_id, soft_delete=True):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Categoría no encontrada"
            )
        return None
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al eliminar categoría: {str(e)}",
        )
