# 🍽️ Sistema de Gestión de Restaurante – API REST con FastAPI + SQLAlchemy

Este proyecto implementa una **API RESTful completa** para la gestión de un restaurante, desarrollada con **FastAPI**, **SQLAlchemy** y **PostgreSQL** (Neon.tech como servicio de base de datos).
Incluye módulos para manejar **usuarios, categorías, menús, mesas, restaurantes y reservas**, con endpoints CRUD y autenticación básica.

---

## 🚀 Tecnologías principales

- **Python 3.10+**
- **FastAPI** (Framework backend)
- **SQLAlchemy ORM**
- **Pydantic v2** (Modelos y validación de datos)
- **Uvicorn** (Servidor ASGI)
- **PostgreSQL (Neon.tech)** (Base de datos)
- **dotenv** (Manejo de variables de entorno)
- **CORS Middleware** (para conexión con frontend)

---

## 📁 Estructura del proyecto

```
project/
│
├── api/
│   ├── endpoints/
│   │   ├── usuarios.py           # Endpoints de usuarios
│   │   ├── categorias.py         # Endpoints de categorías
│   │   ├── menu.py               # Endpoints de menús
│   │   ├── mesas.py              # Endpoints de mesas
│   │   ├── restaurantes.py       # Endpoints de restaurantes
│   │   └── reservas.py           # Endpoints de reservas
│   │
│   ├── schemas/
│   │   ├── usuario_schema.py     # Schemas Pydantic para usuarios
│   │   ├── categoria_schema.py   # Schemas Pydantic para categorías
│   │   ├── menu_schema.py        # Schemas Pydantic para menús
│   │   ├── mesa_schema.py        # Schemas Pydantic para mesas
│   │   ├── restaurante_schema.py # Schemas Pydantic para restaurantes
│   │   └── reserva_schema.py     # Schemas Pydantic para reservas
│
├── crud/
│   ├── usuario_crud.py           # Lógica CRUD para usuarios
│   ├── categoria_crud.py         # Lógica CRUD para categorías
│   ├── menu_crud.py              # Lógica CRUD para menús
│   ├── mesa_crud.py              # Lógica CRUD para mesas
│   ├── restaurante_crud.py       # Lógica CRUD para restaurantes
│   └── reserva_crud.py           # Lógica CRUD para reservas
│
├── database/
│   ├── config.py                 # Configuración y conexión con la BD
│   └── models/
│       ├── usuario.py
│       ├── categoria.py
│       ├── menu.py
│       ├── mesa.py
│       ├── restaurante.py
│       └── reserva.py
│
├── main.py                       # Punto de entrada principal
├── requirements.txt              # Dependencias del proyecto
└── README.md                     # Este archivo
```

---

## ⚙️ Instalación y ejecución del proyecto

### 🧩 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
```

---

### 🐍 2. Crear y activar un entorno virtual

#### En Windows (PowerShell):
```bash
python -m venv venv
venv\Scripts\activate
```

#### En macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 📦 3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

---

### 🗃️ 4. Configurar variables de entorno

Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:

```bash
DATABASE_URL=postgresql://neondb_owner:npg_T8YDJWb9ovOL@ep-floral-bar-adafmaz6-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require
```

> ⚠️ **Importante:**
> - No compartas esta URL en repositorios públicos.
> - Puedes usar `os.getenv("DATABASE_URL")` dentro de tu configuración en `database/config.py`.

---

### 🧠 5. Crear las tablas en la base de datos

Ejecuta este comando en la consola de Python dentro del proyecto:

```bash
python
```

Luego, dentro del intérprete:

```python
from database.config import Base, engine
Base.metadata.create_all(bind=engine)
exit()
```

Esto generará todas las tablas necesarias en la base de datos de Neon.tech.

---

### 🚀 6. Ejecutar el servidor FastAPI

```bash
uvicorn main:app --reload
```

Verás algo como:

```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

---

## 🌐 Documentación interactiva

Una vez el servidor esté corriendo, abre tu navegador en:

- **Swagger UI:** 👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** 👉 [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧠 Endpoints principales

### 👤 Usuarios
| Método | Endpoint | Descripción |
|--------|-----------|-------------|
| `POST` | `/usuarios/` | Crear usuario |
| `GET` | `/usuarios/` | Listar usuarios |
| `GET` | `/usuarios/{id}` | Obtener usuario |
| `PUT` | `/usuarios/{id}` | Actualizar usuario |
| `DELETE` | `/usuarios/{id}` | Eliminar usuario |
| `POST` | `/usuarios/login` | Iniciar sesión |

---

### 🏷️ Categorías
| Método | Endpoint | Descripción |
|--------|-----------|-------------|
| `POST` | `/categorias/` | Crear categoría |
| `GET` | `/categorias/` | Listar categorías |
| `GET` | `/categorias/{id}` | Obtener categoría |
| `PUT` | `/categorias/{id}` | Actualizar categoría |
| `DELETE` | `/categorias/{id}` | Eliminar categoría |

---

### 🍽️ Menús
| Método | Endpoint | Descripción |
|--------|-----------|-------------|
| `POST` | `/menus/` | Crear menú |
| `GET` | `/menus/` | Listar menús |
| `GET` | `/menus/{id}` | Obtener menú |
| `PUT` | `/menus/{id}` | Actualizar menú |
| `DELETE` | `/menus/{id}` | Eliminar menú |

---

### 🪑 Mesas
| Método | Endpoint | Descripción |
|--------|-----------|-------------|
| `POST` | `/mesas/` | Crear mesa |
| `GET` | `/mesas/` | Listar mesas |
| `GET` | `/mesas/{id}` | Obtener mesa |
| `PUT` | `/mesas/{id}` | Actualizar mesa |
| `DELETE` | `/mesas/{id}` | Eliminar mesa |

---

### 🏠 Restaurantes
| Método | Endpoint | Descripción |
|--------|-----------|-------------|
| `POST` | `/restaurantes/` | Crear restaurante |
| `GET` | `/restaurantes/` | Listar restaurantes |
| `GET` | `/restaurantes/{id}` | Obtener restaurante |
| `PUT` | `/restaurantes/{id}` | Actualizar restaurante |
| `DELETE` | `/restaurantes/{id}` | Eliminar restaurante |

---

### 📅 Reservas
| Método | Endpoint | Descripción |
|--------|-----------|-------------|
| `POST` | `/reservas/` | Crear reserva |
| `GET` | `/reservas/` | Listar reservas |
| `GET` | `/reservas/{id}` | Obtener reserva |
| `PUT` | `/reservas/{id}` | Actualizar reserva |
| `DELETE` | `/reservas/{id}` | Eliminar reserva |

---

## 🧪 Ejemplo de prueba rápida (`curl`)

```bash
curl -X POST "http://127.0.0.1:8000/usuarios/" ^
  -H "Content-Type: application/json" ^
  -d "{
    \"nombre\": \"Laura\",
    \"apellido\": \"Rojas\",
    \"nombre_usuario\": \"lauraro\",
    \"email\": \"laura@example.com\",
    \"telefono\": \"+573142223344\",
    \"es_admin\": false,
    \"contrasena\": \"ClaveSegura2025!\"
  }"
```

---

## 💡 Ejemplo de crear una reserva

```json
POST /reservas/
{
  "nombre_completo": "Juan Pérez",
  "telefono": "3001234567",
  "email": "juan@example.com",
  "fecha_reserva": "2025-10-15T19:00:00",
  "hora_reserva": "19:00",
  "numero_personas": 4,
  "metodo_pago": "tarjeta credito",
  "estado": "pendiente",
  "observaciones": "Mesa cerca a la ventana",
  "usuario_id": "b6c3e4d8-1f6b-4e1a-88cb-9b6a0a7f9a44",
  "restaurante_id": "cf5a742e-8573-42c8-9478-7db2f749bfa1",
  "mesa_id": "2bb73d92-187a-4204-bfe7-890c9a3a420a"
}
```

---

## 🔍 Health check

Verifica el estado del servidor y conexión con la base de datos:

```
GET /health
```

**Respuesta esperada:**
```json
{
  "status": "OK",
  "database": "conectada"
}
```

---

## 👩‍💻 Desarrolladores

- **Juan David Hincapié Puerta**
- **David Usuga**
- **Yulieth Marcela Quintero**

---

## 📜 Licencia

Este proyecto está bajo la licencia **MIT**.
Puedes usarlo, modificarlo y distribuirlo libremente, citando a los autores.
