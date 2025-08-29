# Sistema de Reservas para Restaurante

Este proyecto implementa un sistema completo de gestión de reservas para un restaurante utilizando Python con Programación Orientada a Objetos (POO).

## Características del Proyecto

### Conceptos de POO Implementados

1. **Herencia**: La clase `SistemaReservas` hereda de `Restaurante`
2. **Polimorfismo**: Sobrescritura de métodos como `validar_reservas()` y `agregar_reserva()`
3. **Sobrecarga de Métodos**: Múltiples versiones del método `agregar_reserva()`
4. **Encapsulamiento**: Uso de métodos privados como `_validar_datos_reserva()`

### Funcionalidades del Sistema

- **Realizar Reservas**: Crear nuevas reservas con validación de datos
- **Validar Reservas**: Mostrar todas las reservas existentes
- **Eliminar Reservas**: Eliminar reservas por posición
- **Modificar Reservas**: Editar datos de reservas existentes
- **Estadísticas**: Mostrar información estadística de las reservas
- **Horarios Disponibles**: Ver horarios disponibles para reservas

## Estructura del Proyecto

```
Restaurante_SW/
├── reserva.py              # Clase Reserva
├── restaurante.py          # Clase base Restaurante
├── sistema_reservas.py     # Clase SistemaReservas (hereda de Restaurante)
├── main.py                 # Programa principal con menú interactivo
└── README.md               # Este archivo
```

## Clases del Sistema

### Clase Reserva
- Maneja los datos individuales de cada reserva
- Incluye ID único, nombre, hora y método de pago
- Método para modificar datos de la reserva

### Clase Restaurante
- Clase base que maneja operaciones básicas de reservas
- Validación de datos de entrada
- Gestión del array de reservas

### Clase SistemaReservas
- Hereda de Restaurante
- Implementa funcionalidades adicionales
- Sobrescribe métodos de la clase padre
- Maneja horarios disponibles y estadísticas

## Cómo Ejecutar

1. Asegúrate de tener Python instalado en tu sistema
2. Navega al directorio del proyecto
3. Ejecuta el archivo principal:

```bash
python main.py
```

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

### Datos de Reserva

- **Nombre completo**: Solo texto (string)
- **Hora**: Número entero de 9 a 22 (9 AM a 10 PM)
- **Método de pago**: 
  - efectivo
  - transferencia
  - tarjeta credito

### Validaciones

- El nombre no puede estar vacío
- La hora debe estar entre 9 y 22
- Solo se aceptan los métodos de pago especificados
- Las reservas se identifican por posición en el array y por ID único

## Notas Técnicas

- **Persistencia**: Los datos se mantienen solo en memoria durante la ejecución
- **Manejo de Errores**: Validaciones básicas sin uso de try-catch
- **Interfaz**: Menú por consola con navegación numérica
- **Identificación**: Cada reserva tiene un ID único y una posición en el array

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

## Autor

Sistema desarrollado como proyecto de demostración de conceptos de POO en Python.
