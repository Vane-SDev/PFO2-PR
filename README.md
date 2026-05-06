# Sistema de Gestión de Tareas - API REST

Este proyecto es una API REST desarrollada en Flask para la gestión de usuarios y tareas, utilizando SQLite como motor de base de datos y hashes para la protección de credenciales.

## Nota sobre el despliegue en GitHub Pages
Cumpliendo con los requisitos de la PFO, la cara visible del proyecto se encuentra alojada en GitHub Pages. Dado que GitHub Pages es un entorno de alojamiento exclusivamente estático que no soporta la ejecución de motores WSGI (Flask) ni bases de datos dinámicas (SQLite), se ha desplegado allí la interfaz de documentación. El motor backend (la API) debe ejecutarse en el entorno local del evaluador siguiendo las instrucciones a continuación.

## Requisitos Previos
- Python 3.8 o superior.

## Instalación y Ejecución

1. Clonar el repositorio.
2. Crear y activar un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
3. Instalar las dependencias necesarias:
   ```bash
   pip install Flask
   ```
4. Ejecutar el servidor:
   ```bash
   python servidor.py
   ```
El servidor se iniciará en `http://127.0.0.1:5000`.

## Endpoints de la API

### 1. Registro de Usuario (`POST /registro`)
Registra un nuevo usuario en la base de datos con contraseña hasheada.
- **Body esperado (JSON):** `{"usuario": "admin", "contraseña": "123"}`
- **Respuesta Exitosa:** `201 Created`

### 2. Inicio de Sesión (`POST /login`)
Verifica las credenciales del usuario contra la base de datos.
- **Body esperado (JSON):** `{"usuario": "admin", "contraseña": "123"}`
- **Respuesta Exitosa:** `200 OK`

### 3. Tareas (`GET /tareas`)
Devuelve la interfaz HTML de bienvenida al sistema.
- **Respuesta Exitosa:** `200 OK`

---

## 📚 Respuestas Conceptuales de la PFO

**1. ¿Por qué hashear contraseñas?**
Almacenar contraseñas en texto plano representa una vulnerabilidad crítica. Si un atacante compromete la base de datos, obtiene acceso inmediato a las cuentas. El hashing transforma la contraseña mediante un algoritmo unidireccional en una cadena de caracteres irreversible. Durante el login, el sistema aplica la misma función a la contraseña ingresada y compara los hashes, protegiendo las credenciales originales incluso ante filtraciones.

**2. Ventajas de usar SQLite:**
- **Configuración cero (Serverless):** No requiere instalar, configurar ni mantener un motor de base de datos externo.
- **Portabilidad absoluta:** Toda la base de datos y sus tablas se almacenan en un único archivo físico en el disco (`tareas.db`), lo que facilita enormemente las copias de seguridad y la transferencia del proyecto.
- **Integración nativa:** Python incluye el módulo `sqlite3` en su biblioteca estándar, permitiendo gestionar la persistencia de datos sin instalar dependencias adicionales.