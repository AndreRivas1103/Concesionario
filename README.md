# Sistema de Gestión de Concesionarios de Automóviles
##Descripción
Este sistema permite gestionar solicitudes de pruebas de manejo y compra de vehículos en un concesionario de automóviles.

## Características
### Registro de Usuario:
El usuario ingresa su número de identificación y se le pregunta si desea programar una prueba de manejo o comprar un vehículo.

### Prueba de Manejo:
Se muestra un calendario con las fechas y horas disponibles para las pruebas de manejo.
El usuario selecciona una fecha y hora.
El sistema verifica la disponibilidad de vehículos para esa fecha y hora.
Si hay disponibilidad, el usuario ingresa su nombre, número de identificación y se le indica que se dirija al concesionario más cercano.

### Compra de Vehículo
El usuario selecciona el tipo de vehículo que desea (automóvil deportivo, camioneta, sedán).
Selecciona el tipo de llanta (deportiva, de invierno, de calle tradicional).
Selecciona el color del vehículo (negro, azul, etc.).
Selecciona la cilindrada del motor (1500, 2000, 2500).
Selecciona el color interior del vehículo.
Si desea algún extra, se le indica que se dirija al concesionario.
Ingresar sus datos personales (nombre, teléfono, cédula).
Seleccionar el método de pago (cheque, efectivo, transferencia, tarjeta).
El sistema revisa el inventario de vehículos disponibles para la venta y verifica si el vehículo seleccionado se encuentra disponible.
Si el vehículo se encuentra disponible, se genera la orden de compra y se le indica al usuario que se dirija al concesionario.

# Instalar paquetes
Para instalar los paquetes, se debe ejecutar el siguiente comando.
```
pip install -r requirements.txt
```

## Guía de ejecución del programa

Para ejecutar el programa, siga el siguiente comando.

```
python -m src.app
```
