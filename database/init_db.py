"""
Script para inicializar la base de datos
"""

from database.config import create_tables, engine
from database.models.all_models import *

def init_database():
    """
    Inicializar la base de datos creando todas las tablas
    """
    try:
        print("Creando tablas en la base de datos...")
        create_tables()
        print("✅ Tablas creadas exitosamente!")
        return True
    except Exception as e:
        print(f"❌ Error al crear las tablas: {e}")
        return False

def test_connection():
    """
    Probar la conexión a la base de datos
    """
    try:
        with engine.connect() as connection:
            result = connection.execute("SELECT 1")
            print("✅ Conexión a la base de datos exitosa!")
            return True
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return False

if __name__ == "__main__":
    print("=== INICIALIZACIÓN DE BASE DE DATOS ===")
    
    # Probar conexión
    if test_connection():
        # Crear tablas
        init_database()
    else:
        print("No se pudo conectar a la base de datos. Verifica tu configuración.")
