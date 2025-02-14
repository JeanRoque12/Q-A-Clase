import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from user_manager import UserManager
import pytest

# Parametrización de la prueba para crear un usuario válido
@pytest.mark.parametrize(
    "username, email, password, expected_result",
    [
        ("juan", "juan@example.com", "Pass1234", "Usuario creado exitosamente"),
        ("maria", "maria@example.com", "Secure1234", "Usuario creado exitosamente"),
        ("pedro", "pedro@example.com", "Qwerty123", "Usuario creado exitosamente"),
    ]
)
def test_add_valid_user(username, email, password, expected_result):
    manager = UserManager()
    result = manager.add_user(username, email, password)
    assert result == expected_result

# Parametrización de la prueba para correo electrónico inválido
@pytest.mark.parametrize(
    "username, email, password",
    [
        ("maria", "maria@com", "Pass1234"),  # Email sin dominio
        ("juan", "juan@.com", "Secure1234"), # Email con punto antes del dominio
        ("pedro", "pedro@com", "Qwerty123"), # Email sin TLD (.com, .net, etc.)
    ]
)
def test_add_invalid_email(username, email, password):
    manager = UserManager()
    with pytest.raises(ValueError, match="Correo inválido"):
        manager.add_user(username, email, password)

# Parametrización de la prueba para contraseñas débiles
@pytest.mark.parametrize(
    "username, email, password",
    [
        ("carlos", "carlos@example.com", "12345"),          # Contraseña corta
        ("ana", "ana@example.com", "password"),             # Contraseña sin números
        ("luisa", "luisa@example.com", "abcdefg1"),         # Contraseña sin letras mayúsculas
    ]
)
def test_add_weak_password(username, email, password):
    manager = UserManager()
    with pytest.raises(ValueError, match="Contraseña insegura"):
        manager.add_user(username, email, password)

# Parametrización de la prueba para eliminar usuario existente
@pytest.mark.parametrize(
    "username, email, password, expected_result",
    [
        ("ana", "ana@example.com", "Secure123", "Usuario eliminado"),
        ("luisa", "luisa@example.com", "StrongPass1", "Usuario eliminado"),
        ("pedro", "pedro@example.com", "StrongPass123", "Usuario eliminado"),
    ]
)
def test_remove_existing_user(username, email, password, expected_result):
    manager = UserManager()
    manager.add_user(username, email, password)
    result = manager.remove_user(username)
    assert result == expected_result

# Parametrización de la prueba para eliminar usuario no existente
@pytest.mark.parametrize(
    "username",
    [
        "juan",    # Usuario no creado
        "maria",   # Usuario no creado
        "carlos",  # Usuario no creado
    ]
)
def test_remove_nonexistent_user(username):
    manager = UserManager()
    with pytest.raises(ValueError, match="Usuario no encontrado"):
        manager.remove_user(username)
