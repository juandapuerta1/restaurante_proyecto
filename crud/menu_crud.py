from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session
from database.models.menu import Menu


class MenuCRUD:
    def __init__(self, db: Session):
        self.db = db

    def crear_menu(
        self,
        nombre: str,
        precio: float,
        categoria_id: UUID,
        restaurante_id: UUID,
        descripcion: Optional[str] = None,
        disponible: bool = True,
        tiempo_preparacion: Optional[int] = None,
        ingredientes: Optional[str] = None,
        alergenos: Optional[str] = None,
    ) -> Menu:
        """
        Crear un nuevo menú con validaciones.
        """
        if not nombre or len(nombre.strip()) == 0:
            raise ValueError("El nombre del menú es obligatorio")

        if len(nombre) > 200:
            raise ValueError("El nombre no puede exceder 200 caracteres")

        if precio <= 0:
            raise ValueError("El precio debe ser mayor que 0")

        menu = Menu(
            nombre=nombre.strip(),
            descripcion=descripcion.strip() if descripcion else None,
            precio=precio,
            disponible=disponible,
            tiempo_preparacion=tiempo_preparacion,
            ingredientes=ingredientes.strip() if ingredientes else None,
            alergenos=alergenos.strip() if alergenos else None,
            categoria_id=categoria_id,
            restaurante_id=restaurante_id,
        )
        self.db.add(menu)
        self.db.commit()
        self.db.refresh(menu)
        return menu

    def obtener_menu(self, menu_id: UUID) -> Optional[Menu]:
        """
        Obtener un menú por ID.
        """
        return (
            self.db.query(Menu)
            .filter(Menu.id_menu == menu_id, Menu.disponible == True)
            .first()
        )

    def obtener_menus(self, skip: int = 0, limit: int = 100) -> List[Menu]:
        """
        Obtener lista de menús disponibles con paginación.
        """
        return (
            self.db.query(Menu)
            .filter(Menu.disponible == True)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def actualizar_menu(self, menu_id: UUID, **kwargs) -> Optional[Menu]:
        """
        Actualizar un menú con validaciones.
        """
        menu = self.obtener_menu(menu_id)
        if not menu:
            return None

        if "nombre" in kwargs:
            nombre = kwargs["nombre"]
            if not nombre or len(nombre.strip()) == 0:
                raise ValueError("El nombre del menú es obligatorio")
            if len(nombre) > 200:
                raise ValueError("El nombre no puede exceder 200 caracteres")
            kwargs["nombre"] = nombre.strip()

        if "precio" in kwargs and kwargs["precio"] is not None:
            if kwargs["precio"] <= 0:
                raise ValueError("El precio debe ser mayor que 0")

        for key, value in kwargs.items():
            if hasattr(menu, key):
                setattr(menu, key, value)

        self.db.commit()
        self.db.refresh(menu)
        return menu

    def eliminar_menu(self, menu_id: UUID, soft_delete: bool = True) -> bool:
        """
        Eliminar un menú.
        Por defecto hace un soft delete (disponible=False).
        """
        menu = self.obtener_menu(menu_id)
        if not menu:
            return False

        if soft_delete:
            menu.disponible = False
            self.db.commit()
        else:
            self.db.delete(menu)
            self.db.commit()

        return True