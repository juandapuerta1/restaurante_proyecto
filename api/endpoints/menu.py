"""
Endpoints para gestión de Menús
"""

from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api.schemas.menu_schema import MenuCreate, MenuResponse, MenuUpdate
from crud.menu_crud import MenuCRUD
from database.config import get_db

router = APIRouter(prefix="/menus", tags=["Menús"])


@router.post("/", response_model=MenuResponse, status_code=status.HTTP_201_CREATED)
def crear_menu(menu: MenuCreate, db: Session = Depends(get_db)):
    try:
        crud = MenuCRUD(db)
        nuevo_menu = crud.crear_menu(**menu.model_dump())
        return nuevo_menu
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al crear menú: {e}")


@router.get("/", response_model=List[MenuResponse])
def listar_menus(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    try:
        crud = MenuCRUD(db)
        return crud.obtener_menus(skip=skip, limit=limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al listar menús: {e}")


@router.get("/{menu_id}", response_model=MenuResponse)
def obtener_menu(menu_id: UUID, db: Session = Depends(get_db)):
    try:
        crud = MenuCRUD(db)
        menu = crud.obtener_menu(menu_id)
        if not menu:
            raise HTTPException(status_code=404, detail="Menú no encontrado")
        return menu
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener menú: {e}")


@router.put("/{menu_id}", response_model=MenuResponse)
def actualizar_menu(menu_id: UUID, menu: MenuUpdate, db: Session = Depends(get_db)):
    try:
        crud = MenuCRUD(db)
        datos = menu.model_dump(exclude_unset=True)
        if not datos:
            raise HTTPException(status_code=400, detail="Sin datos para actualizar")

        actualizado = crud.actualizar_menu(menu_id, **datos)
        if not actualizado:
            raise HTTPException(status_code=404, detail="Menú no encontrado")
        return actualizado
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar menú: {e}")


@router.delete("/{menu_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_menu(menu_id: UUID, db: Session = Depends(get_db)):
    try:
        crud = MenuCRUD(db)
        if not crud.eliminar_menu(menu_id):
            raise HTTPException(status_code=404, detail="Menú no encontrado")
        return None
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar menú: {e}")
