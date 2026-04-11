# Taller 2: Gestión de Personal y Formación - ITM

## 1. Información General
* **Integrantes:** Diego Alejandro Giraldo Bolivar
                   Julian David Velez Arango
                   Jorge Andres Vidal Ramirez 
* **Asignatura:** Aplicaciones y Servicios Web
* **Fecha:** Abril 2026

## 2. Descripción de la Arquitectura
El proyecto sigue una arquitectura modular por capas:
* **models**: Definición de tablas en SQLAlchemy.
* **schemas**: Validación de datos con Pydantic.
* **crud**: Lógica de interacción con la base de datos.
* **api**: Endpoints de la aplicación (routers).
* **db**: Configuración de la conexión y sesiones.