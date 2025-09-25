# Sistema de Gestión de Restaurante

Sistema completo de gestión de restaurante desarrollado con Python, SQLAlchemy ORM y PostgreSQL (Neon). Incluye autenticación de usuarios, gestión de reservas, mesas, menús y categorías.

## 🚀 Características Principales

- **Autenticación segura** con hash de contraseñas
- **Base de datos PostgreSQL** con Neon
- **ORM SQLAlchemy** para manejo de datos
- **UUIDs** como identificadores primarios
- **Interfaz de consola** interactiva
- **Operaciones CRUD** completas
- **Validaciones robustas** de datos

## 👥 Desarrolladores

- **Juan David Hincapie Puerta**
- **David Usuga**
- **Yulieth Marcela Quintero**

## 📁 Estructura del Proyecto

```
restaurante_proyecto-5/
├── auth/
│   └── security.py              # Gestión segura de contraseñas
├── crud/
│   ├── usuario_crud.py          # Operaciones CRUD para usuarios
│   ├── restaurante_crud.py      # Operaciones CRUD para restaurantes
│   ├── mesa_crud.py             # Operaciones CRUD para mesas
│   ├── reserva_crud.py          # Operaciones CRUD para reservas
│   ├── categoria_crud.py        # Operaciones CRUD para categorías
│   └── menu_crud.py             # Operaciones CRUD para menús
├── database/
│   ├── config.py                # Configuración de base de datos
│   ├── init_db.py               # Inicialización de BD
│   └── models/
│       ├── usuario.py           # Modelo Usuario
│       ├── restaurante.py       # Modelo Restaurante
│       ├── mesa.py              # Modelo Mesa
│       ├── reserva.py           # Modelo Reserva
│       ├── categoria.py         # Modelo Categoría
│       └── menu.py              # Modelo Menú
├── main.py                      # Sistema principal con autenticación
├── requirements.txt             # Dependencias del proyecto
├── .env                         # Variables de entorno (crear desde env_example.txt)
├── .gitignore                   # Archivos a ignorar en Git
└── README.md                    # Este archivo
```

## 🗄️ Base de Datos

### Entidades Implementadas

1. **Usuario** - Gestión de usuarios del sistema
2. **Restaurante** - Información de restaurantes
3. **Mesa** - Mesas disponibles en el restaurante
4. **Reserva** - Reservas de clientes
5. **Categoría** - Categorías de menú
6. **Menú** - Items del menú del restaurante

### Características de la Base de Datos

- **UUIDs** como identificadores primarios
- **Columnas de auditoría**: `fecha_creacion`, `fecha_edicion`
- **Relaciones** entre entidades con claves foráneas
- **Validaciones** a nivel de base de datos

## 🛠️ Instalación y Configuración

### Prerrequisitos

- Python 3.8 o superior
- Cuenta en Neon (PostgreSQL)
- Git

### Pasos de Instalación

1. **Clonar el repositorio**
   ```bash
   git clone <url-del-repositorio>
   cd restaurante_proyecto-5
   ```

2. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar variables de entorno**
   ```bash
   # Copiar el archivo de ejemplo
   cp env_example.txt .env
   
   # Editar .env con tu URL de Neon
   # DATABASE_URL=postgresql://usuario:password@host:port/database
   ```

4. **Inicializar la base de datos**
   ```bash
   python -c "from database.config import create_tables; create_tables()"
   ```

## 🚀 Cómo Ejecutar

```bash
python main.py
```

## 📋 Funcionalidades del Sistema

### Sistema de Autenticación

- **Login** con nombre de usuario o email
- **Validación** de credenciales
- **Gestión de sesiones**
- **Contraseñas seguras** con hash

### Gestión de Usuarios

- ✅ **Crear usuarios** con validaciones
- ✅ **Listar usuarios** registrados
- ✅ **Buscar usuarios** por email o nombre
- ✅ **Actualizar usuarios** existentes
- ✅ **Eliminar usuarios** del sistema
- ✅ **Crear administrador** por defecto

### Lógica de Negocio

- **Validaciones robustas** de datos de entrada
- **Manejo de errores** apropiado
- **Operaciones CRUD** completas
- **Relaciones** entre entidades

## 🎯 Uso del Sistema

### Menú Principal

```
==================================================
        SISTEMA DE GESTION DE RESTAURANTE
==================================================
Usuario: [Nombre del Usuario]
Email: [email@ejemplo.com]
Administrador
==================================================
1. Gestión de Usuarios
0. Cerrar Sesión
==================================================
```

### Gestión de Usuarios

```
--- GESTIÓN DE USUARIOS ---
1. Crear Usuario
2. Listar Usuarios
3. Buscar Usuario por Email
4. Buscar Usuario por Nombre de Usuario
5. Actualizar Usuario
6. Eliminar Usuario
7. Crear Usuario Administrador por Defecto
0. Volver al menú principal
```

## 🔧 Tecnologías Utilizadas

- **Python 3.12**
- **SQLAlchemy 2.0.23** - ORM
- **PostgreSQL** - Base de datos (Neon)
- **psycopg** - Driver de PostgreSQL
- **python-dotenv** - Variables de entorno

## 📊 Arquitectura del Sistema

### Patrón de Diseño

- **CRUD Pattern** - Operaciones de base de datos
- **Repository Pattern** - Separación de lógica de datos
- **MVC Pattern** - Separación de responsabilidades

### Seguridad

- **Hash de contraseñas** con salt
- **Validación de entrada** robusta
- **Manejo seguro** de sesiones
- **Conexiones SSL** a la base de datos

## 🧪 Validaciones Implementadas

### Usuarios

- Email válido y único
- Nombre de usuario único
- Contraseña segura (8+ caracteres, mayúsculas, minúsculas, números, símbolos)
- Teléfono con formato válido
- Campos obligatorios

### Base de Datos

- **UUIDs** únicos
- **Claves foráneas** válidas
- **Restricciones** de integridad
- **Índices** para rendimiento

## 📝 Notas Técnicas

- **Persistencia**: Datos almacenados en PostgreSQL (Neon)
- **Manejo de Errores**: Validaciones completas con mensajes informativos
- **Interfaz**: Menú por consola con navegación intuitiva
- **Identificación**: UUIDs únicos para todas las entidades
- **Auditoría**: Fechas de creación y edición automáticas

## 🔮 Funcionalidades Futuras

- Gestión completa de reservas
- Sistema de menús y categorías
- Gestión de mesas
- Reportes y estadísticas
- Interfaz web (opcional)

## 📄 Licencia

Proyecto desarrollado para fines académicos.

---

**Desarrollado con ❤️ por el equipo de desarrollo**