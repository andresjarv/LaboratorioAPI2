# Taller 2: Gestión de Personal y Formación - ITM

## 1. Información General
* **Integrantes:** 
                   > - Diego Alejandro Giraldo Bolivar*
                   > - Julian David Velez Arango*
                   > - Jorge Andres Vidal Ramirez*
                   
* **Asignatura:** Aplicaciones y Servicios Web
* **Fecha:** Abril 2026

## 2. Descripción de la Arquitectura
El proyecto sigue una arquitectura modular por capas:
* **models**: Definición de tablas en SQLAlchemy.
* **schemas**: Validación de datos con Pydantic.
* **crud**: Lógica de interacción con la base de datos.
* **api**: Endpoints de la aplicación (routers).
* **db**: Configuración de la conexión y sesiones.

## 3. Modelo de Datos
Se implementaron dos entidades principales relacionadas:

### Entidad: Personal
Representa la información básica de los integrantes.
* *Campos clave:* id, nombre, apellido, documento (único), email.
* *Schema:* grupo_3

### Entidad: Formación
Registra la trayectoria académica de cada persona.
* *Relación:* Llave foránea id_personal vinculada a la tabla personal.
* *Integridad:* Se configuró eliminación en cascada para evitar registros huérfanos.

## 4. Validación de Datos (Schemas)
Se utiliza *Pydantic* para la validación y serialización de datos:

* *Contratos de Entrada:* Se definen esquemas Create y Update para restringir qué campos puede enviar el cliente (por ejemplo, el cliente no puede definir el id manualmente).
* *Contratos de Salida:* Los esquemas de respuesta formatean los objetos de base de datos a JSON, incluyendo relaciones anidadas (un objeto Personal incluye su lista de formaciones).
* *Tipado Fuerte:* Uso de EmailStr para garantizar la integridad de los correos electrónicos desde el nivel de aplicación.