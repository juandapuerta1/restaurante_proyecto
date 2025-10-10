"""
Endpoints para gestión de Usuarios
"""

from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from api.schemas.usuario_schema import (
    UsuarioCreate,
    UsuarioResponse,
    UsuarioUpdate,
    UsuarioLogin,
)
from crud.usuario_crud import UsuarioCRUD
from database.config import get_db

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


@router.post("/", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    """
    Crear un nuevo usuario
    """
    try:
        crud = UsuarioCRUD(db)
        nuevo_usuario = crud.crear_usuario(
            nombre=usuario.nombre,
            apellido=usuario.apellido,
            nombre_usuario=usuario.nombre_usuario,
            email=usuario.email,
            contrasena=usuario.contrasena,
            telefono=usuario.telefono,
            es_admin=usuario.es_admin,
        )
        return nuevo_usuario
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al crear usuario: {str(e)}",
        )


@router.get("/", response_model=List[UsuarioResponse])
def listar_usuarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Listar todos los usuarios activos
    """
    try:
        crud = UsuarioCRUD(db)
        usuarios = crud.obtener_usuarios(skip=skip, limit=limit)
        return usuarios
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al listar usuarios: {str(e)}",
        )


@router.get("/{usuario_id}", response_model=UsuarioResponse)
def obtener_usuario(usuario_id: UUID, db: Session = Depends(get_db)):
    """
    Obtener un usuario por ID
    """
    try:
        crud = UsuarioCRUD(db)
        usuario = crud.obtener_usuario(usuario_id)
        if not usuario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado"
            )
        return usuario
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener usuario: {str(e)}",
        )


@router.get("/email/{email}", response_model=UsuarioResponse)
def obtener_usuario_por_email(email: str, db: Session = Depends(get_db)):
    """
    Obtener un usuario por email
    """
    try:
        crud = UsuarioCRUD(db)
        usuario = crud.obtener_usuario_por_email(email)
        if not usuario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado"
            )
        return usuario
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al obtener usuario: {str(e)}",
        )


@router.put("/{usuario_id}", response_model=UsuarioResponse)
def actualizar_usuario(
    usuario_id: UUID, usuario: UsuarioUpdate, db: Session = Depends(get_db)
):
    """
    Actualizar un usuario existente
    """
    try:
        crud = UsuarioCRUD(db)

        # Convertir el modelo a diccionario y eliminar campos None
        datos_actualizacion = usuario.model_dump(exclude_unset=True)

        if not datos_actualizacion:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No se proporcionaron datos para actualizar",
            )

        usuario_actualizado = crud.actualizar_usuario(usuario_id, **datos_actualizacion)

        if not usuario_actualizado:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado"
            )

        return usuario_actualizado
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al actualizar usuario: {str(e)}",
        )


@router.delete("/{usuario_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_usuario(usuario_id: UUID, db: Session = Depends(get_db)):
    """
    Eliminar un usuario
    """
    try:
        crud = UsuarioCRUD(db)
        if not crud.eliminar_usuario(usuario_id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado"
            )
        return None
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al eliminar usuario: {str(e)}",
        )


@router.post("/login", response_model=UsuarioResponse)
def login(credenciales: UsuarioLogin, db: Session = Depends(get_db)):
    """
    Autenticar un usuario
    """
    try:
        crud = UsuarioCRUD(db)
        usuario = crud.autenticar_usuario(
            credenciales.nombre_usuario, credenciales.contrasena
        )

        if not usuario:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Credenciales incorrectas",
            )

        return usuario
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al autenticar: {str(e)}",
        )
