"""
Ejemplo de uso de la base de datos con Neon
"""

from auth.security import PasswordManager
from sqlalchemy import text
from database.config import get_db, create_tables
from database.models.all_models import *
from sqlalchemy.orm import Session
from datetime import datetime, timedelta


def ejemplo_crear_datos():
    """
    Ejemplo de cómo crear datos en la base de datos
    """
    # Obtener sesión de base de datos
    db = next(get_db())

    try:
        # 1. Crear un usuario administrador
        admin = Usuario(
            nombre="Admin1",
            apellido="Sistema",
            email="admin1@restaurante.com",
            telefono="+1234567890",
            es_admin=True,
            nombre_usuario="admin123",  # usuario de prueba
            contrasena=PasswordManager.hash_password("adminpass2025"),
        )
        db.add(admin)
        db.commit()
        db.refresh(admin)
        print(f"✅ Usuario admin creado: {admin.id_usuario}")

        # 2. Crear un restaurante
        restaurante = Restaurante(
            nombre="Mi Restaurante",
            direccion="Calle Principal 123, Ciudad",
            telefono="+1234567890",
            email="info@mirestaurante.com",
            capacidad_maxima=50,
            horario_apertura="12:00",
            horario_cierre="22:00",
            usuario_admin_id=admin.id_usuario,
        )
        db.add(restaurante)
        db.commit()
        db.refresh(restaurante)
        print(f"✅ Restaurante creado: {restaurante.id_restaurante}")

        # 3. Crear mesas
        for i in range(1, 11):
            mesa = Mesa(
                numero_mesa=i,
                capacidad=4,
                ubicacion="Salón principal",
                restaurante_id=restaurante.id_restaurante,
            )
            db.add(mesa)
        db.commit()
        print("✅ 10 mesas creadas")

        # 4. Crear categorías
        categorias = [
            {"nombre": "Entradas", "descripcion": "Platos para comenzar"},
            {"nombre": "Platos Principales", "descripcion": "Platos fuertes"},
            {"nombre": "Postres", "descripcion": "Dulces y postres"},
            {"nombre": "Bebidas", "descripcion": "Refrescos y bebidas"},
        ]

        for cat_data in categorias:
            categoria = Categoria(**cat_data)
            db.add(categoria)
        db.commit()
        print("✅ Categorías creadas")

        # 5. Crear platos del menú
        platos = [
            {
                "nombre": "Ensalada César",
                "descripcion": "Lechuga romana, crutones, parmesano y aderezo césar",
                "precio": 12.50,
                "categoria_id": db.query(Categoria)
                .filter(Categoria.nombre == "Entradas")
                .first()
                .id_categoria,
                "restaurante_id": restaurante.id_restaurante,
                "tiempo_preparacion": 10,
            },
            {
                "nombre": "Pasta Carbonara",
                "descripcion": "Pasta con salsa de huevo, panceta y parmesano",
                "precio": 18.00,
                "categoria_id": db.query(Categoria)
                .filter(Categoria.nombre == "Platos Principales")
                .first()
                .id_categoria,
                "restaurante_id": restaurante.id_restaurante,
                "tiempo_preparacion": 20,
            },
            {
                "nombre": "Tiramisú",
                "descripcion": "Postre italiano con café y mascarpone",
                "precio": 8.50,
                "categoria_id": db.query(Categoria)
                .filter(Categoria.nombre == "Postres")
                .first()
                .id_categoria,
                "restaurante_id": restaurante.id_restaurante,
                "tiempo_preparacion": 15,
            },
        ]

        for plato_data in platos:
            plato = Menu(**plato_data)
            db.add(plato)
        db.commit()
        print("✅ Platos del menú creados")

        # 6. Crear una reserva de ejemplo
        reserva = Reserva(
            nombre_completo="Juan Pérez",
            telefono="+1234567890",
            email="juan@email.com",
            fecha_reserva=datetime.now() + timedelta(days=1),
            hora_reserva="19:30",
            numero_personas=2,
            metodo_pago="efectivo",
            estado="pendiente",
            restaurante_id=restaurante.id_restaurante,
            mesa_id=db.query(Mesa).first().id_mesa,
        )
        db.add(reserva)
        db.commit()
        db.refresh(reserva)
        print(f"✅ Reserva creada: {reserva.id_reserva}")

        print("\n🎉 ¡Datos de ejemplo creados exitosamente!")

    except Exception as e:
        print(f"❌ Error al crear datos: {e}")
        db.rollback()
    finally:
        db.close()


def ejemplo_consultar_datos():
    """
    Ejemplo de cómo consultar datos de la base de datos
    """
    db = next(get_db())

    try:
        # Consultar restaurantes
        restaurantes = db.query(Restaurante).all()
        print(f"\n📊 Restaurantes encontrados: {len(restaurantes)}")
        for r in restaurantes:
            print(f"  - {r.nombre} (Capacidad: {r.capacidad_maxima})")

        # Consultar reservas
        reservas = db.query(Reserva).all()
        print(f"\n📊 Reservas encontradas: {len(reservas)}")
        for r in reservas:
            print(f"  - {r.nombre_completo} - {r.fecha_reserva} a las {r.hora_reserva}")

        # Consultar menú
        menu = db.query(Menu).all()
        print(f"\n📊 Platos en el menú: {len(menu)}")
        for m in menu:
            print(f"  - {m.nombre} - ${m.precio}")

    except Exception as e:
        print(f"❌ Error al consultar datos: {e}")
    finally:
        db.close()


def agregar_campos_usuario():
    db = next(get_db())
    try:
        db.execute(
            text(
                """
            ALTER TABLE usuarios
            ADD COLUMN IF NOT EXISTS nombre_usuario VARCHAR(100) UNIQUE,
            ADD COLUMN IF NOT EXISTS contrasena VARCHAR(255);
        """
            )
        )
        db.commit()
        print("✅ Campos agregados correctamente")
    except Exception as e:
        print(f"❌ Error al agregar campos: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    print("=== EJEMPLO DE USO DE BASE DE DATOS ===")

    # Crear tablas si no existen
    print("Creando tablas...")
    create_tables()

    # Crear datos de ejemplo
    print("\nCreando datos de ejemplo...")
    ejemplo_crear_datos()

    # Consultar datos
    print("\nConsultando datos...")
    ejemplo_consultar_datos()

    agregar_campos_usuario()
