UserManager: Gestión de Usuarios con Pruebas Unitarias

- Descripción

Este proyecto implementa una clase UserManager en Python para gestionar usuarios, permitiendo su creación, eliminación y validación de credenciales. Además, incluye pruebas unitarias con pytest para garantizar la funcionalidad y robustez del sistema.

- Estructura del Proyecto

project_root/
│── src/
│   ├── user_manager.py  # Implementación de la clase UserManager
│
│── tests/
│   ├── test_user_manager.py  # Pruebas unitarias con pytest
│
│── venv/  # Entorno virtual de Python (opcional)
│
│── README.md  # Documentación del proyecto

- Instalación y Configuración

1. Clonar el repositorio
git clone <URL_DEL_REPOSITORIO>
cd project_root

2. Crear y activar un entorno virtual (opcional, pero recomendado)

python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

3. Instalar las dependencias

pip install -r requirements.txt

- Uso de UserManager

> Métodos principales

add_user(username, email, password): Agrega un usuario validando formato de correo y seguridad de contraseña.

remove_user(username): Elimina un usuario si existe.

get_users(): Retorna todos los usuarios registrados.

> Pruebas Unitarias

Para ejecutar las pruebas unitarias con pytest, usa el siguiente comando:

pytest tests/

> Casos de Prueba Implementados

Las pruebas están parametrizadas para cubrir diferentes escenarios:

Registro de usuario exitoso: Verifica que un usuario válido se agregue correctamente.
Correo inválido: Prueba con varios formatos incorrectos de correo electrónico.
Contraseña débil: Evalúa contraseñas que no cumplen con los requisitos de seguridad.
Eliminación de usuario existente: Confirma que un usuario registrado puede ser eliminado.
Intento de eliminación de usuario inexistente: Verifica el manejo adecuado de errores al eliminar un usuario no registrado.