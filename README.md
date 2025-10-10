# 🧠 Sistema de Gestión API – FastAPI + SQLAlchemy

Este proyecto implementa una **API REST** para gestionar usuarios y categorías, utilizando **FastAPI**, **SQLAlchemy** y **PostgreSQL** (Neon.tech como servicio de base de datos).

Incluye endpoints para **crear, listar, actualizar y eliminar usuarios y categorías**, además de autenticación básica de usuarios.

---

## 🚀 Tecnologías principales

- **Python 3.10+**
- **FastAPI** (Framework backend)
- **SQLAlchemy ORM**
- **Pydantic v2** (modelos y validación)
- **Uvicorn** (servidor ASGI)
- **PostgreSQL (Neon.tech)** (base de datos)
- **dotenv** (manejo de variables de entorno)

---

## 📁 Estructura del proyecto

```
project/
│
├── api/
│   ├── routes/
│   │   ├── usuarios.py           # Endpoints de usuarios
│   │   ├── categorias.py         # Endpoints de categorías
│   │   └── __init__.py
│   ├── schemas/
│   │   ├── usuario_schema.py     # Esquemas Pydantic para usuarios
│   │   └── categoria_schema.py   # Esquemas Pydantic para categorías
│
├── crud/
│   ├── usuario_crud.py           # Lógica CRUD para usuarios
│   ├── categoria_crud.py         # Lógica CRUD para categorías
│
├── database/
│   ├── config.py                 # Configuración y conexión con la BD
│   ├── models.py                 # Modelos SQLAlchemy
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
> - Puedes usar una variable de entorno local (`os.getenv("DATABASE_URL")`) en tu configuración de conexión.

---

### 🧠 5. Crear las tablas en la base de datos

Ejecuta este comando en una consola de Python dentro del proyecto:

```bash
python
```

Luego dentro del intérprete:

```python
from database.config import Base, engine
Base.metadata.create_all(bind=engine)
exit()
```

Esto generará las tablas necesarias en tu base de datos Neon.

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

## 🌐 Endpoints principales

Una vez el servidor esté corriendo, puedes abrir tu navegador en:

👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

Ahí encontrarás la **documentación interactiva Swagger UI** generada automáticamente.

### 🔸 Usuarios
- `POST /usuarios/` → Crear usuario
- `GET /usuarios/` → Listar usuarios
- `GET /usuarios/{id}` → Obtener usuario por ID
- `PUT /usuarios/{id}` → Actualizar usuario
- `DELETE /usuarios/{id}` → Eliminar usuario
- `POST /usuarios/login` → Iniciar sesión

### 🔸 Categorías
- `POST /categorias/` → Crear categoría
- `GET /categorias/` → Listar categorías
- `GET /categorias/{id}` → Obtener categoría por ID
- `PUT /categorias/{id}` → Actualizar categoría
- `DELETE /categorias/{id}` → Eliminar categoría

---

## 🧪 Ejemplo de prueba rápida con `curl`

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

## 👩‍💻 Desarrolladores

- **Juan David Hincapié Puerta**
- **David Usuga**
- **Yulieth Marcela Quintero**

---

## 📜 Licencia

Este proyecto está bajo la licencia MIT.
Puedes usarlo, modificarlo y distribuirlo libremente, citando a los autores.
