# TP1-Joaquin-Hidalgo
Análisis y Metodología de Sistemas

SmartGastro - Sistema de Gestión para Foodtrucks.
Descripción del Proyecto.
SmartGastro es una solución tecnológica diseñada para la asociación de dueños de Foodtrucks que buscan profesionalizar su operativa. El sistema permite abandonar el seguimiento manual en papel o Excel para centralizar la gestión de inventario y ventas en una plataforma robusta. 
Este prototipo inicial funciona mediante una interfaz de consola en Python, aplicando paradigmas de Programación Orientada a Objetos (POO). 

Funcionalidades Principales.
El sistema ofrece un motor lógico interactivo con las siguientes capacidades:  
Gestión de Inventario: Permite el alta de productos definiendo nombre, precio y stock inicial.  
Control de Ventas: Registro de transacciones con actualización automática de existencias.  
Validación de Stock: El sistema impide realizar ventas si no hay disponibilidad suficiente del producto, protegiendo la integridad del negocio.  
Visualización en Tiempo Real: Reporte consolidado del estado actual del inventario.

Tecnologías y Conceptos Aplicados.
Para el desarrollo de este motor core se utilizaron conceptos avanzados de ingeniería de software vistos en la materia:  
Lenguaje: Python 3.14.
Encapsulamiento: Uso de atributos privados (__atributo) y métodos de acceso (Getters/Setters) para asegurar que el stock no sea modificado sin validaciones previas.  
Modularización: Estructura basada en clases (Producto, Inventario) para facilitar la escalabilidad futura hacia entornos web.  
Gestión Ágil: El desarrollo fue planificado siguiendo metodologías Kanban y criterios INVEST para las historias de usuario. 

-----------------------------------------------------------------------------------------------------
Instrucciones de Ejecución.
Para correr el sistema en tu entorno local, seguí estos pasos:

Clonar el repositorio:
git clone https://github.com//SmartGastro-TP1.git

Abrir el proyecto:
Cargá la carpeta en tu IDE de preferencia.

Ejecutar el script:
Corré el archivo main.py.
python main.py

Uso:
Navegá por las opciones del menú interactivo ingresando los números correspondientes en la terminal.
-----------------------------------------------------------------------------------------------------
