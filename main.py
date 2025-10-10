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
    docs_url="/docs",  # Swagger UI en /docs
    redoc_url="/redoc",  # ReDoc en /redoc
    lifespan=lifespan,
)

# Configurar CORS (permitir peticiones desde el frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especifica los dominios permitidos
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
            "restaurantes": "/restaurantes (próximamente)",
            "mesas": "/mesas (próximamente)",
            "reservas": "/reservas (próximamente)",
            "menu": "/menu (próximamente)",
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


# Incluir routers de endpoints
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

# Cuando crees los demás endpoints, los incluyes así:
# try:
#     from api.endpoints import restaurantes
#     app.include_router(restaurantes.router)
# except Exception as e:
#     print(f"⚠️ No se pudo cargar router de restaurantes: {e}")


# Configuración de Uvicorn para ejecutar la aplicación
if __name__ == "__main__":
    uvicorn.run(
        "main:app",  # Archivo:variable
        host="0.0.0.0",  # Escuchar en todas las interfaces
        port=8000,  # Puerto
        reload=True,  # Auto-reload en desarrollo (cambios en código)
        log_level="info",
    )
