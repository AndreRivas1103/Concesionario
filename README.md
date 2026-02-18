# Sistema de Gestión de Concesionarios de Automóviles

## Descripción

Aplicación de escritorio para la gestión integral de un concesionario de automóviles. Permite a los clientes registrarse, solicitar pruebas de manejo (test drive) y realizar pre-compra de vehículos, con interfaz gráfica desarrollada en Python (tkinter).

---

## Estructura del proyecto

```
Concesionario/
├── .gitignore
├── README.md
├── requirements.txt
├── docs/                    # Documentación adicional
├── src/
│   ├── __init__.py
│   ├── app.py               # Punto de entrada y lógica de la interfaz (tkinter)
│   ├── db/
│   │   └── database.py      # Acceso a datos y persistencia
│   ├── exceptions/
│   │   ├── base_exception.py
│   │   ├── db_exceptions.py
│   │   ├── date_exceptions.py
│   │   └── diver_test_exceptions.py
│   ├── models/
│   │   ├── car.py           # Modelo de vehículo
│   │   ├── driver_test.py   # Modelo de prueba de manejo
│   │   ├── purchase.py      # Modelo de pre-compra (tipos, sedes, métodos de pago)
│   │   └── user.py          # Modelo de usuario
│   ├── utils/
│   │   ├── color.py         # Utilidades de color (RGB)
│   │   └── utils_date.py
│   └── uml/                 # Diagramas UML del proyecto
└── .venv/                   # Entorno virtual (no se versiona)
```

---

## Características

### Registro de usuario

El cliente ingresa su **nombre** y **número de teléfono**. El sistema valida los datos, comprueba si ya existe el usuario y lo registra o recupera para continuar. Tras el registro, se muestra un menú para elegir entre **Prueba de manejo** o **Pre-compra**.

### Prueba de manejo (Test Drive)

Permite agendar una cita para probar un vehículo en el concesionario:

- **Calendario**: el usuario selecciona la fecha deseada mediante un selector de fechas.
- **Hora**: elección entre horarios disponibles (08:00 a 13:00).
- **Tipo de vehículo**: deportivo, camioneta o automóvil.
- Tras enviar la solicitud, el sistema confirma la cita y se indica al cliente que acuda al concesionario elegido, con al menos 15 minutos de anticipación.

### Compra de vehículo (Pre-compra)

Flujo de pre-compra para configurar el vehículo y la sede:

- **Tipo de vehículo**: Deportivo, Camioneta o Automóvil.
- **Tipo de llanta**: Deportivos, Invierno, Sencillos o Fibra de Carbono.
- **Cilindrada del motor**: 1000, 1500, 2000, 2500, 3000 o 3500 cc.
- **Color exterior**: código RGB (valores R, G, B entre 0 y 255).
- **Color interior**: mismo criterio de color.
- **Sede**: Medellín, Cali, Bogotá o Pereira.
- **Método de pago**: Cheque, Efectivo, Transferencia o Tarjetas.

Al enviar, se genera un resumen con los datos del cliente, vehículo elegido, método de pago y sede. La solicitud se envía al concesionario y se indica al cliente que en 48 horas puede acercarse a la sede seleccionada para recibir asesoría.

---

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
