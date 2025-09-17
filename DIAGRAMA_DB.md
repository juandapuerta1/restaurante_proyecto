# Diagrama de Base de Datos

## Estructura de Entidades

```
Usuario (1) ──────── (N) Restaurante
   │                      │
   │                      │
   │                      ├── (N) Mesa
   │                      ├── (N) Reserva
   │                      └── (N) Menu
   │
   └── (N) Reserva

Categoria (1) ──────── (N) Menu
```

## Relaciones Detalladas

- **Usuario** → **Restaurante**: Un usuario puede administrar varios restaurantes
- **Restaurante** → **Mesa**: Un restaurante tiene muchas mesas
- **Restaurante** → **Reserva**: Un restaurante recibe muchas reservas
- **Restaurante** → **Menu**: Un restaurante ofrece muchos platos
- **Usuario** → **Reserva**: Un usuario puede hacer muchas reservas
- **Mesa** → **Reserva**: Una mesa puede tener muchas reservas
- **Categoria** → **Menu**: Una categoría contiene muchos platos
