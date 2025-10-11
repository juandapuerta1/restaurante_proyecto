"""
Operaciones CRUD para Menu
"""

from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session
from database.models.menu import Menu


class MenuCRUD:
    def __init__(self, db: Session):
        self.db = db

    # ---------- CREAR ----------
    def crear_menu(
        self,
        nombre: str,
        descripcion: Optional[str],
        precio: float,
        disponible: bool,
        tiempo_preparacion: Optional[int],
        ingredientes: Optional[str],
        alergenos: Optional[str],
        categoria_id: UUID,
        restaurante_id: UUID,
    ) -> Menu:
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a 0")

        menu = Menu(
            nombre=nombre.strip(),
            descripcion=descripcion,
            precio=precio,
            disponible=disponible,
            tiempo_preparacion=tiempo_preparacion,
            ingredientes=ingredientes,
            alergenos=alergenos,
            categoria_id=categoria_id,
            restaurante_id=restaurante_id,
        )
        self.db.add(menu)
        self.db.commit()
        self.db.refresh(menu)
        return menu

    # ---------- OBTENER ----------
    def obtener_menu(self, menu_id: UUID) -> Optional[Menu]:
        return self.db.query(Menu).filter(Menu.id_menu == menu_id).first()

    def obtener_menus(self, skip: int = 0, limit: int = 100) -> List[Menu]:
        return self.db.query(Menu).offset(skip).limit(limit).all()

    # ---------- ACTUALIZAR ----------
    def actualizar_menu(self, menu_id: UUID, **kwargs) -> Optional[Menu]:
        menu = self.obtener_menu(menu_id)
        if not menu:
            return None

        for key, value in kwargs.items():
            if hasattr(menu, key):
                setattr(menu, key, value)

        self.db.commit()
        self.db.refresh(menu)
        return menu

    # ---------- ELIMINAR ----------
    def eliminar_menu(self, menu_id: UUID) -> bool:
        menu = self.obtener_menu(menu_id)
        if menu:
            self.db.delete(menu)
            self.db.commit()
            return True
        return False
