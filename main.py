"""
Sistema de Gestión de Restaurante - API REST con FastAPI
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from database.config import create_tables, test_connection


# Lifespan event handler (reemplaza on_event)
@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Maneja el ciclo de vida de la aplicación
    """
    # Startup
    print("🚀 Iniciando Sistema de Gestión de Restaurante...")

    # Verificar conexión a la base de datos
    if test_connection():
        print("✅ Conexión a la base de datos exitosa")
    else:
        print("❌ Error de conexión a la base de datos")

    # Crear tablas si no existen
    try:
        create_tables()
        print("✅ Tablas verificadas/creadas correctamente")
    except Exception as e:
        print(f"❌ Error al crear tablas: {e}")

    yield  # La aplicación se ejecuta aquí

    # Shutdown
    print("👋 Cerrando Sistema de Gestión de Restaurante...")


# Crear instancia de FastAPI con lifespan
app = FastAPI(
    title="Sistema de Gestión de Restaurante",
    description="API REST para gestionar restaurantes, reservas, menús y más",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especifica dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Ruta raíz
@app.get("/", tags=["General"])
async def root():
    """
    Endpoint raíz - información general de la API
    """
    return {
        "mensaje": "Bienvenido al Sistema de Gestión de Restaurante",
        "version": "1.0.0",
        "documentacion": "/docs",
        "redoc": "/redoc",
        "endpoints_disponibles": {
            "usuarios": "/usuarios",
            "categorias": "/categorias",
            "restaurantes": "/restaurantes",
            "mesas": "/mesas",
            "menus": "/menus",
            "reservas": "/reservas",
        },
    }


# Health check
@app.get("/health", tags=["General"])
async def health_check():
    """
    Endpoint para verificar el estado de la API
    """
    return {
        "status": "OK",
        "database": "conectada" if test_connection() else "desconectada",
    }


# ======================
#   CARGA DE ENDPOINTS
# ======================

try:
    from api.endpoints import usuarios

    app.include_router(usuarios.router)
    print("✅ Router de usuarios cargado")
except Exception as e:
    print(f"⚠️ No se pudo cargar router de usuarios: {e}")

try:
    from api.endpoints import categorias

    app.include_router(categorias.router)
    print("✅ Router de categorías cargado")
except Exception as e:
    print(f"⚠️ No se pudo cargar router de categorías: {e}")

try:
    from api.endpoints import restaurantes

    app.include_router(restaurantes.router)
    print("✅ Router de restaurantes cargado")
except Exception as e:
    print(f"⚠️ No se pudo cargar router de restaurantes: {e}")

try:
    from api.endpoints import mesas

    app.include_router(mesas.router)
    print("✅ Router de mesas cargado")
except Exception as e:
    print(f"⚠️ No se pudo cargar router de mesas: {e}")

try:
    from api.endpoints import menu

    app.include_router(menu.router)
    print("✅ Router de menús cargado")
except Exception as e:
    print(f"⚠️ No se pudo cargar router de menús: {e}")

try:
    from api.endpoints import reservas

    app.include_router(reservas.router)
    print("✅ Router de reservas cargado")
except Exception as e:
    print(f"⚠️ No se pudo cargar router de reservas: {e}")


# Configuración de Uvicorn
if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info",
    )
