# Sistema de Gestión de Concesionarios de Automóviles
## Descripción
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

## Instalación y Configuración

### Requisitos Previos

- Python 3.8 o superior
- pip (generalmente incluido con Python)

### Instalación en Linux

1. **Instalar dependencias del sistema** (si no están instaladas):
   ```bash
   sudo apt install python3-venv python3-tk
   ```
   
2. **Crear entorno virtual**:
   ```bash
   python3 -m venv .venv
   ```

3. **Activar entorno virtual**:
   ```bash
   source .venv/bin/activate
   ```

4. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

### Instalación en Windows

1. **Verificar que Python esté instalado**:
   ```cmd
   python --version
   ```
   

2. **Crear entorno virtual**:
   ```cmd
   python -m venv .venv
   ```
   
   O si tienes múltiples versiones de Python:
   ```cmd
   py -3 -m venv .venv
   ```

3. **Activar entorno virtual**:
   
   ```cmd
   .venv\Scripts\activate.bat
   ```

4. **Instalar dependencias**:
   ```cmd
   pip install -r requirements.txt
   ```

## Ejecución del programa

**Importante:** Asegúrate de tener el entorno virtual activado antes de ejecutar el programa.

### En Linux

1. **Activar el entorno virtual** (si no está activado):
   ```bash
   source .venv/bin/activate
   ```

2. **Ejecutar el programa**:
   ```bash
   python -m src.app
   ```
   
   O ejecutando directamente el archivo:
   ```bash
   python src/app.py
   ```

3. **Desactivar el entorno virtual** (cuando termines):
   ```bash
   deactivate
   ```

### En Windows

1. **Activar el entorno virtual** (si no está activado):
   
   ```cmd
   .venv\Scripts\activate.bat
   ```

2. **Ejecutar el programa**:
   ```cmd
   python -m src.app
   ```
   
   O ejecutando directamente el archivo:
   ```cmd
   python src/app.py
   ```

3. **Desactivar el entorno virtual** (cuando termines):
   ```cmd
   deactivate
   ```
