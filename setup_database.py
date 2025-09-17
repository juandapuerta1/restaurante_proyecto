"""
Script de configuración automática para la base de datos
"""

import os
import shutil
from pathlib import Path

def setup_database():
    """
    Configurar la base de datos automáticamente
    """
    print("🚀 Configurando base de datos para el proyecto de restaurante...")
    
    # 1. Crear archivo .env si no existe
    env_file = Path(".env")
    env_example = Path("env_example.txt")
    
    if not env_file.exists() and env_example.exists():
        shutil.copy(env_example, env_file)
        print("✅ Archivo .env creado desde env_example.txt")
    elif env_file.exists():
        print("✅ Archivo .env ya existe")
    else:
        print("❌ No se encontró env_example.txt")
        return False
    
    # 2. Verificar que las dependencias estén instaladas
    try:
        import sqlalchemy
        import psycopg2
        from dotenv import load_dotenv
        print("✅ Dependencias encontradas")
    except ImportError as e:
        print(f"❌ Faltan dependencias: {e}")
        print("Ejecuta: pip install -r requirements.txt")
        return False
    
    # 3. Probar conexión a la base de datos
    try:
        from database.config import test_connection
        if test_connection():
            print("✅ Conexión a Neon exitosa")
        else:
            print("❌ No se pudo conectar a Neon")
            return False
    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return False
    
    # 4. Crear tablas
    try:
        from database.init_db import init_database
        if init_database():
            print("✅ Tablas creadas exitosamente")
        else:
            print("❌ Error al crear tablas")
            return False
    except Exception as e:
        print(f"❌ Error al inicializar base de datos: {e}")
        return False
    
    print("\n🎉 ¡Configuración completada exitosamente!")
    print("\nPróximos pasos:")
    print("1. Ejecuta: python ejemplo_uso_db.py")
    print("2. Revisa el archivo README_DATABASE.md para más información")
    
    return True

if __name__ == "__main__":
    setup_database()
