## Desarrolladores

- **Juan David Hincapie Puerta**
- **David Usuga** 
- **Yulieth Marcela Quintero**


## Uso del Sistema
### Menú Principal
El sistema presenta un menú interactivo con las siguientes opciones:

1. **Realizar Reserva**: Crear una nueva reserva
2. **Validar Reservas**: Ver todas las reservas existentes
3. **Eliminar Reserva**: Eliminar una reserva por posición
4. **Modificar Reserva**: Editar datos de una reserva existente
5. **Mostrar Estadísticas**: Ver estadísticas de las reservas
6. **Mostrar Horarios Disponibles**: Ver horarios disponibles
0. **Salir**: Terminar el programa

## Ejemplo de Uso

```
=== SISTEMA DE RESERVAS - RESTAURANTE ===
1. Realizar Reserva
2. Validar Reservas
3. Eliminar Reserva
4. Modificar Reserva
5. Mostrar Estadísticas
6. Mostrar Horarios Disponibles
0. Salir
==================================================

Seleccione una opción: 1

--- REALIZAR RESERVA ---
Ingrese el nombre completo: Juan Pérez
Ingrese la hora (9-22): 19

Métodos de pago disponibles:
1. efectivo
2. transferencia
3. tarjeta credito
Ingrese el método de pago: efectivo

¡Reserva creada exitosamente!
ID de reserva: 1
```


## 🚀 Guía Rápida para Entender el Proyecto

### **Paso 1: Entender la Estructura (5 minutos)**
Mira estos archivos como si fueran personas trabajando en un restaurante:

- **`reserva.py`** = El mesero que toma la orden (guarda datos básicos)
- **`restaurante.py`** = El gerente que maneja todo (clase principal)
- **`sistema_reservas.py`** = El supervisor que agrega reglas especiales
- **`main.py`** = La recepción donde llegan los clientes (interfaz)

### **Paso 2: Entender el Flujo (3 minutos)**
1. Cliente llega → `main.py` (recepcionista)
2. Recepcionista llama → `sistema_reservas.py` (supervisor)
3. Supervisor verifica → `restaurante.py` (gerente)
4. Gerente crea → `reserva.py` (mesero guarda la orden)

### **Paso 3: Ejecutar y Probar (2 minutos)**

#### **Opción A: Git Bash (Recomendado)**
```bash
# 1. Abre Git Bash en la carpeta del proyecto
cd /TU RUTA/Restaurante_SW/restaurante_proyecto

# 2. Ejecuta el proyecto
python main.py
