"""
Sistema de Gestión de Restaurante - Solo Usuarios
"""

import getpass
from typing import Optional

from auth.security import PasswordManager
from crud.usuario_crud import UsuarioCRUD
from database.config import SessionLocal, create_tables
from database.models.usuario import Usuario


class SistemaRestaurante:
    """Sistema principal con autenticación y gestión de usuarios"""

    def __init__(self):
        self.db = SessionLocal()
        self.usuario_crud = UsuarioCRUD(self.db)
        self.usuario_actual: Optional[Usuario] = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.close()

    # =================== LOGIN ===================
    def mostrar_pantalla_login(self) -> bool:
        """Pantalla de login y autenticación"""
        print("\n" + "=" * 50)
        print("        SISTEMA DE GESTION DE RESTAURANTE")
        print("=" * 50)
        print("INICIAR SESION")
        print("=" * 50)

        intentos = 0
        max_intentos = 3

        while intentos < max_intentos:
            try:
                print(f"\nIntento {intentos + 1} de {max_intentos}")
                nombre_usuario = input("Nombre de usuario o email: ").strip()
                if not nombre_usuario:
                    print("ERROR: El nombre de usuario es obligatorio")
                    intentos += 1
                    continue

                contrasena = getpass.getpass("Contraseña: ")
                if not contrasena:
                    print("ERROR: La contraseña es obligatoria")
                    intentos += 1
                    continue

                usuario = self.usuario_crud.autenticar_usuario(
                    nombre_usuario, contrasena
                )
                if usuario:
                    self.usuario_actual = usuario
                    print(f"\nEXITO: ¡Bienvenido, {usuario.nombre}!")
                    if usuario.es_admin:
                        print("INFO: Tienes privilegios de administrador")
                    return True
                else:
                    print("ERROR: Credenciales incorrectas o usuario inactivo")
                    intentos += 1

            except KeyboardInterrupt:
                print("\nOperación cancelada por el usuario")
                return False
            except Exception as e:
                print(f"ERROR durante el login: {e}")
                intentos += 1

        print(
            f"\nERROR: Máximo de intentos ({max_intentos}) excedido. Acceso denegado."
        )
        return False

    # =================== MENÚ PRINCIPAL ===================
    def mostrar_menu_principal_autenticado(self) -> None:
        """Menú principal después del login"""
        print("\n" + "=" * 50)
        print("    SISTEMA DE GESTION DE RESTAURANTE")
        print("=" * 50)
        print(f"Usuario: {self.usuario_actual.nombre}")
        print(f"Email: {self.usuario_actual.email}")
        if self.usuario_actual.es_admin:
            print("Administrador")
        print("=" * 50)
        print("1. Gestión de Usuarios")
        print("0. Cerrar Sesión")
        print("=" * 50)

    # =================== MENÚ USUARIOS ===================
    def mostrar_menu_usuarios(self) -> None:
        """Submenú de gestión de usuarios"""
        while True:
            print("\n--- GESTIÓN DE USUARIOS ---")
            print("1. Crear Usuario")
            print("2. Listar Usuarios")
            print("3. Buscar Usuario por Email")
            print("4. Buscar Usuario por Nombre de Usuario")
            print("5. Actualizar Usuario")
            print("6. Eliminar Usuario")
            print("7. Crear Usuario Administrador por Defecto")
            print("0. Volver al menú principal")

            opcion = input("\nSeleccione una opción: ").strip()
            if opcion == "1":
                self.crear_usuario()
            elif opcion == "2":
                self.listar_usuarios()
            elif opcion == "3":
                self.buscar_usuario_por_email()
            elif opcion == "4":
                self.buscar_usuario_por_nombre_usuario()
            elif opcion == "5":
                self.actualizar_usuario()
            elif opcion == "6":
                self.eliminar_usuario()
            elif opcion == "7":
                self.crear_usuario_admin()
            elif opcion == "0":
                break
            else:
                print("ERROR: Opción inválida. Intente nuevamente.")

    # =================== FUNCIONES CRUD ===================
    def crear_usuario(self) -> None:
        try:
            print("\n--- CREAR USUARIO ---")
            nombre = input("Nombre completo: ").strip()
            apellido = input("Apellido: ").strip()
            nombre_usuario = input("Nombre de usuario: ").strip()
            email = input("Email: ").strip()
            contrasena = getpass.getpass("Contraseña: ")
            telefono = input("Teléfono (opcional): ").strip() or None
            es_admin = input("¿Es administrador? (s/n): ").strip().lower() == "s"

            usuario = self.usuario_crud.crear_usuario(
                nombre=nombre,
                apellido=apellido,
                nombre_usuario=nombre_usuario,
                email=email,
                contrasena=contrasena,
                telefono=telefono,
                es_admin=es_admin,
            )
            print(f"EXITO: Usuario creado exitosamente: {usuario}")
        except Exception as e:
            print(f"ERROR inesperado: {e}")

    def listar_usuarios(self) -> None:
        try:
            usuarios = self.usuario_crud.obtener_usuarios()
            if not usuarios:
                print("INFO: No hay usuarios registrados.")
                return

            print(f"\n--- USUARIOS ({len(usuarios)}) ---")
            for i, usuario in enumerate(usuarios, 1):
                admin_text = " (ADMIN)" if usuario.es_admin else ""
                activo_text = "Activo" if usuario.activo else "Inactivo"
                print(
                    f"{i}. {usuario.nombre} ({usuario.nombre_usuario}) - {usuario.email} - {activo_text}{admin_text}"
                )
        except Exception as e:
            print(f"ERROR: {e}")

    def buscar_usuario_por_email(self) -> None:
        try:
            email = input("\nIngrese el email a buscar: ").strip()
            usuario = self.usuario_crud.obtener_usuario_por_email(email)
            if usuario:
                admin_text = " (ADMIN)" if usuario.es_admin else ""
                activo_text = "Activo" if usuario.activo else "Inactivo"
                print(f"EXITO: Usuario encontrado:")
                print(f"   Nombre: {usuario.nombre}")
                print(f"   Apellido: {usuario.apellido}")
                print(f"   Nombre de usuario: {usuario.nombre_usuario}")
                print(f"   Email: {usuario.email}")
                print(f"   Telefono: {usuario.telefono or 'No especificado'}")
                print(f"   Estado: {activo_text}{admin_text}")
            else:
                print("ERROR: Usuario no encontrado.")
        except Exception as e:
            print(f"ERROR: {e}")

    def buscar_usuario_por_nombre_usuario(self) -> None:
        try:
            nombre_usuario = input("\nIngrese el nombre de usuario a buscar: ").strip()
            usuario = self.usuario_crud.obtener_usuario_por_nombre_usuario(
                nombre_usuario
            )
            if usuario:
                admin_text = " (ADMIN)" if usuario.es_admin else ""
                activo_text = "Activo" if usuario.activo else "Inactivo"
                print(f"EXITO: Usuario encontrado:")
                print(f"   Nombre: {usuario.nombre}")
                print(f"   Apellido: {usuario.apellido}")
                print(f"   Nombre de usuario: {usuario.nombre_usuario}")
                print(f"   Email: {usuario.email}")
                print(f"   Telefono: {usuario.telefono or 'No especificado'}")
                print(f"   Estado: {activo_text}{admin_text}")
            else:
                print("ERROR: Usuario no encontrado.")
        except Exception as e:
            print(f"ERROR: {e}")

    def actualizar_usuario(self) -> None:
        try:
            email = input("\nIngrese el email del usuario a actualizar: ").strip()
            usuario = self.usuario_crud.obtener_usuario_por_email(email)
            if not usuario:
                print("ERROR: Usuario no encontrado.")
                return

            print(f"\nActualizando usuario: {usuario.nombre}")
            print("Deje en blanco para mantener el valor actual")

            nuevo_nombre = input(f"Nombre actual ({usuario.nombre}): ").strip()
            nuevo_apellido = input(f"Apellido actual ({usuario.apellido}): ").strip()
            nuevo_nombre_usuario = input(
                f"Nombre de usuario actual ({usuario.nombre_usuario}): "
            ).strip()
            nuevo_email = input(f"Email actual ({usuario.email}): ").strip()
            nuevo_telefono = input(
                f"Teléfono actual ({usuario.telefono or 'No especificado'}): "
            ).strip()

            cambios = {}
            if nuevo_nombre:
                cambios["nombre"] = nuevo_nombre
            if nuevo_apellido:  # agregado
                cambios["apellido"] = nuevo_apellido
            if nuevo_nombre_usuario:
                cambios["nombre_usuario"] = nuevo_nombre_usuario
            if nuevo_email:
                cambios["email"] = nuevo_email
            if nuevo_telefono:
                cambios["telefono"] = nuevo_telefono

            if cambios:
                usuario_actualizado = self.usuario_crud.actualizar_usuario(
                    usuario.id, **cambios
                )
                print(f"EXITO: Usuario actualizado: {usuario_actualizado}")
            else:
                print("INFO: No se realizaron cambios.")
        except Exception as e:
            print(f"ERROR: {e}")

    def eliminar_usuario(self) -> None:
        try:
            email = input("\nIngrese el email del usuario a eliminar: ").strip()
            usuario = self.usuario_crud.obtener_usuario_por_email(email)
            if not usuario:
                print("ERROR: Usuario no encontrado.")
                return

            confirmacion = (
                input(f"¿Está seguro de eliminar a {usuario.nombre}? (s/n): ")
                .strip()
                .lower()
            )
            if confirmacion == "s":
                if self.usuario_crud.eliminar_usuario(usuario.id):
                    print("EXITO: Usuario eliminado exitosamente.")
                else:
                    print("ERROR: Error al eliminar el usuario.")
            else:
                print("INFO: Operación cancelada.")
        except Exception as e:
            print(f"ERROR: {e}")

    def crear_usuario_admin(self) -> None:
        try:
            admin = self.usuario_crud.obtener_admin_por_defecto()
            if admin:
                print("INFO: Ya existe un usuario administrador por defecto.")
                return

            contrasena_admin = PasswordManager.generate_secure_password(12)
            admin = self.usuario_crud.crear_usuario(
                nombre="Administrador del Sistema",
                nombre_usuario="admin",
                email="admin@system.com",
                contrasena=contrasena_admin,
                es_admin=True,
            )
            print(f"EXITO: Usuario administrador creado: {admin}")
            print(f"INFO: Contraseña temporal: {contrasena_admin}")
            print("ADVERTENCIA: Cambie esta contraseña en su primer inicio de sesión")
        except Exception as e:
            print(f"ERROR: {e}")

    # =================== EJECUTAR SISTEMA ===================
    def ejecutar(self) -> None:
        create_tables()
        if not self.mostrar_pantalla_login():
            print("Acceso denegado. Hasta luego!")
            return

        while True:
            self.mostrar_menu_principal_autenticado()
            opcion = input("\nSeleccione una opción: ").strip()
            if opcion == "1":
                self.mostrar_menu_usuarios()
            elif opcion == "0":
                print("\n¡Hasta luego!")
                break
            else:
                print("ERROR: Opción inválida. Intente nuevamente.")


def main():
    with SistemaRestaurante() as sistema:
        sistema.ejecutar()


if __name__ == "__main__":
    main()
