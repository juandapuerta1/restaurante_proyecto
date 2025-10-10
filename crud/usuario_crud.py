"""
Operaciones CRUD para Usuario
"""

import re
from typing import List, Optional
from uuid import UUID

from auth.security import PasswordManager
from database.models.usuario import Usuario
from sqlalchemy.orm import Session


class UsuarioCRUD:
    def __init__(self, db: Session):
        self.db = db

    # ------------------ VALIDACIONES ------------------
    def _validar_email(self, email: str) -> bool:
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email) is not None

    def _validar_telefono(self, telefono: str) -> bool:
        pattern = r"^\+?[\d\s\-\(\)]{7,15}$"
        return re.match(pattern, telefono) is not None

    def _validar_nombre_usuario(self, nombre_usuario: str) -> bool:
        pattern = r"^[a-zA-Z0-9_]{3,20}$"
        return re.match(pattern, nombre_usuario) is not None

    # ------------------ CREAR ------------------
    def crear_usuario(
        self,
        nombre: str,
        apellido: str,
        nombre_usuario: str,
        email: str,
        contrasena: str,
        telefono: Optional[str] = None,
        es_admin: bool = False,
    ) -> Usuario:
        if not nombre.strip():
            raise ValueError("El nombre es obligatorio")
        if not apellido.strip():
            raise ValueError("El apellido es obligatorio")
        if len(nombre) > 100 or len(apellido) > 100:
            raise ValueError("Nombre o apellido demasiado largo")

        if not nombre_usuario or not self._validar_nombre_usuario(nombre_usuario):
            raise ValueError(
                "El nombre de usuario debe tener entre 3-20 caracteres y solo contener letras, números y guiones bajos"
            )
        if self.obtener_usuario_por_nombre_usuario(nombre_usuario):
            raise ValueError("El nombre de usuario ya existe")

        if not email or not self._validar_email(email):
            raise ValueError("Email inválido")
        if self.obtener_usuario_por_email(email):
            raise ValueError("El email ya está registrado")

        if not contrasena:
            raise ValueError("La contraseña es obligatoria")
        es_valida, mensaje = PasswordManager.validate_password_strength(contrasena)
        if not es_valida:
            raise ValueError(f"Contraseña inválida: {mensaje}")

        if telefono and not self._validar_telefono(telefono):
            raise ValueError("Formato de teléfono inválido")

        usuario = Usuario(
            nombre=nombre.strip(),
            apellido=apellido.strip(),
            nombre_usuario=nombre_usuario.lower().strip(),
            email=email.lower().strip(),
            contrasena=PasswordManager.hash_password(
                contrasena
            ),  # 🔑 aquí guardamos el hash
            telefono=telefono.strip() if telefono else None,
            es_admin=es_admin,
        )
        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario

    # ------------------ OBTENER ------------------
    def obtener_usuario(self, usuario_id: UUID) -> Optional[Usuario]:
        return (
            self.db.query(Usuario)
            .filter(Usuario.id_usuario == usuario_id, Usuario.activo == True)
            .first()
        )

    def obtener_usuario_por_email(self, email: str) -> Optional[Usuario]:
        return (
            self.db.query(Usuario)
            .filter(Usuario.email == email.lower().strip(), Usuario.activo == True)
            .first()
        )

    def obtener_usuario_por_nombre_usuario(
        self, nombre_usuario: str
    ) -> Optional[Usuario]:
        return (
            self.db.query(Usuario)
            .filter(
                Usuario.nombre_usuario == nombre_usuario.lower().strip(),
                Usuario.activo == True,
            )
            .first()
        )

    def obtener_usuarios(self, skip: int = 0, limit: int = 100) -> List[Usuario]:
        return (
            self.db.query(Usuario)
            .filter(Usuario.activo == True)
            .offset(skip)
            .limit(limit)
            .all()
        )

    # ------------------ AUTENTICAR ------------------
    def autenticar_usuario(
        self, nombre_usuario: str, contrasena: str
    ) -> Optional[Usuario]:
        usuario = self.obtener_usuario_por_nombre_usuario(nombre_usuario)
        if not usuario:
            usuario = self.obtener_usuario_por_email(nombre_usuario)
        if not usuario or not usuario.activo:
            return None
        if PasswordManager.verify_password(contrasena, usuario.contrasena):
            return usuario
        return None

    # ------------------ ACTUALIZAR ------------------
    def actualizar_usuario(self, usuario_id: UUID, **kwargs) -> Optional[Usuario]:
        usuario = self.obtener_usuario(usuario_id)
        if not usuario:
            return None

        if "email" in kwargs:
            email = kwargs["email"]
            if not self._validar_email(email):
                raise ValueError("Email inválido")
            existente = self.obtener_usuario_por_email(email)
            if existente and existente.id_usuario != usuario_id:
                raise ValueError("El email ya está registrado")
            kwargs["email"] = email.lower().strip()

        if "telefono" in kwargs and kwargs["telefono"]:
            if not self._validar_telefono(kwargs["telefono"]):
                raise ValueError("Formato de teléfono inválido")
            kwargs["telefono"] = kwargs["telefono"].strip()

        if "nombre_usuario" in kwargs:
            nombre_usuario = kwargs["nombre_usuario"]
            if not self._validar_nombre_usuario(nombre_usuario):
                raise ValueError("Nombre de usuario inválido")
            existente = self.obtener_usuario_por_nombre_usuario(nombre_usuario)
            if existente and existente.id_usuario != usuario_id:
                raise ValueError("El nombre de usuario ya está en uso")
            kwargs["nombre_usuario"] = nombre_usuario.lower().strip()

        if "contrasena" in kwargs:
            contrasena = kwargs["contrasena"]
            es_valida, mensaje = PasswordManager.validate_password_strength(contrasena)
            if not es_valida:
                raise ValueError(f"Contraseña inválida: {mensaje}")
            kwargs["contrasena"] = PasswordManager.hash_password(contrasena)

        for key, value in kwargs.items():
            if hasattr(usuario, key):
                setattr(usuario, key, value)

        self.db.commit()
        self.db.refresh(usuario)
        return usuario

    # ------------------ ELIMINAR ------------------
    def eliminar_usuario(self, usuario_id: UUID) -> bool:
        usuario = self.obtener_usuario(usuario_id)
        if usuario:
            self.db.delete(usuario)
            self.db.commit()
            return True
        return False

    def desactivar_usuario(self, usuario_id: UUID) -> Optional[Usuario]:
        usuario = self.obtener_usuario(usuario_id)
        if not usuario:
            return None
        usuario.activo = False
        self.db.commit()
        self.db.refresh(usuario)
        return usuario

    # ------------------ EXTRA ------------------
    def obtener_usuarios_admin(self) -> List[Usuario]:
        return (
            self.db.query(Usuario)
            .filter(Usuario.es_admin == True, Usuario.activo == True)
            .all()
        )

    def es_admin(self, usuario_id: UUID) -> bool:
        usuario = self.obtener_usuario(usuario_id)
        return usuario.es_admin if usuario else False

    def obtener_admin_por_defecto(self) -> Optional[Usuario]:
        """
        Obtener el usuario admin por defecto
        """
        return (
            self.db.query(Usuario)
            .filter(
                Usuario.nombre_usuario == "admin",
                Usuario.es_admin == True,
                Usuario.activo == True,
            )
            .first()
        )
