# Sistema de Restaurante con Base de Datos Neon

Este proyecto ha sido actualizado para usar una base de datos PostgreSQL en Neon, permitiendo persistencia de datos y operaciones más robustas.

## 🚀 Configuración Inicial

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Configurar variables de entorno

1. Copia el archivo `env_example.txt` y renómbralo a `.env`
2. El archivo `.env` ya contiene tu URL de conexión a Neon:

```env
DATABASE_URL=postgresql://neondb_owner:npg_T8YDJWb9ovOL@ep-floral-bar-adafmaz6-pooler.c-2.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require
```

### 3. Inicializar la base de datos

```bash
python database/init_db.py
```

## 📊 Estructura de la Base de Datos

El sistema incluye 6 entidades principales:

### 1. **Usuario**
- Información de usuarios del sistema
- Campos: id, nombre, apellido, email, teléfono, es_admin, activo

### 2. **Restaurante**
- Información del restaurante
- Campos: id, nombre, dirección, teléfono, email, capacidad, horarios, activo

### 3. **Mesa**
- Mesas del restaurante
- Campos: id, número, capacidad, ubicación, activa

### 4. **Reserva**
- Reservas de clientes
- Campos: id, nombre, teléfono, email, fecha, hora, personas, método_pago, estado

### 5. **Categoria**
- Categorías de platos
- Campos: id, nombre, descripción, activa

### 6. **Menu**
- Platos del menú
- Campos: id, nombre, descripción, precio, disponible, tiempo_preparación, ingredientes

## 🔧 Uso

### Ejecutar ejemplo completo

```bash
python ejemplo_uso_db.py
```

Este script:
- Crea todas las tablas
- Inserta datos de ejemplo
- Muestra cómo consultar los datos

### Usar en tu código

```python
from database.config import get_db
from database.models.all_models import *

# Obtener sesión de base de datos
db = next(get_db())

# Crear una nueva reserva
nueva_reserva = Reserva(
    nombre_completo="María García",
    telefono="+1234567890",
    email="maria@email.com",
    fecha_reserva=datetime.now(),
    hora_reserva="20:00",
    numero_personas=4,
    metodo_pago="tarjeta credito",
    estado="pendiente",
    restaurante_id=restaurante_id,
    mesa_id=mesa_id
)

db.add(nueva_reserva)
db.commit()
```

## 📁 Estructura de Archivos

```
Restaurante_SW/
├── database/
│   ├── __init__.py
│   ├── config.py              # Configuración de conexión
│   ├── init_db.py             # Script de inicialización
│   └── models/
│       ├── __init__.py
│       ├── all_models.py      # Importa todos los modelos
│       ├── usuario.py
│       ├── restaurante.py
│       ├── mesa.py
│       ├── reserva.py
│       ├── categoria.py
│       └── menu.py
├── .env                       # Variables de entorno (crear desde env_example.txt)
├── env_example.txt           # Ejemplo de variables de entorno
├── requirements.txt          # Dependencias
├── ejemplo_uso_db.py        # Ejemplo de uso
└── README_DATABASE.md       # Este archivo
```

## 🔗 Relaciones entre Entidades

- **Usuario** → **Restaurante** (1:N) - Un usuario puede administrar varios restaurantes
- **Restaurante** → **Mesa** (1:N) - Un restaurante tiene muchas mesas
- **Restaurante** → **Reserva** (1:N) - Un restaurante tiene muchas reservas
- **Restaurante** → **Menu** (1:N) - Un restaurante tiene muchos platos
- **Usuario** → **Reserva** (1:N) - Un usuario puede hacer muchas reservas
- **Mesa** → **Reserva** (1:N) - Una mesa puede tener muchas reservas
- **Categoria** → **Menu** (1:N) - Una categoría tiene muchos platos

## ⚡ Características

- ✅ Conexión segura con SSL a Neon
- ✅ Pool de conexiones para mejor rendimiento
- ✅ UUIDs como claves primarias
- ✅ Timestamps automáticos de creación y edición
- ✅ Relaciones bien definidas entre entidades
- ✅ Validaciones de datos
- ✅ Campos de auditoría

## 🛠️ Próximos Pasos

1. Ejecuta `python database/init_db.py` para crear las tablas
2. Ejecuta `python ejemplo_uso_db.py` para probar el sistema
3. Integra la base de datos en tu aplicación principal
4. Añade validaciones adicionales según tus necesidades
