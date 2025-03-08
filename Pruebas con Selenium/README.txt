DOCUMENTACION DE PRUEBAS AUTOMATIZADAS CON SELENIUM

1. DESCRIPCION GENERAL
Este documento describe las pruebas automatizadas realizadas en el sitio web Demo Blaze utilizando Selenium con Python y pytest. Se realizaron tres pruebas principales:
- Inicio de sesión
- Agregar producto al carrito
- Completar una compra

2. CONFIGURACION DEL ENTORNO
Para replicar las pruebas, sigue estos pasos:

2.1 INSTALACION DE DEPENDENCIAS
Asegúrate de tener Python instalado y luego ejecuta:
 pip install selenium pytest

Descarga e instala el WebDriver correspondiente a tu navegador. Para Chrome, puedes obtenerlo desde:
 https://sites.google.com/chromium.org/driver/

Agrega el WebDriver al PATH del sistema o especifica su ubicación en el código.

3. DISEÑO DE PRUEBAS

3.1 INICIO DE SESION
OBJETIVO: Verificar que un usuario pueda iniciar sesión correctamente.
PASOS:
1. Abrir la página principal de Demo Blaze.
2. Hacer clic en "Log in".
3. Ingresar credenciales válidas.
4. Confirmar que el mensaje de bienvenida se muestra.
RESULTADO ESPERADO: Se muestra el mensaje "Welcome [nombre de usuario]".

3.2 AGREGAR PRODUCTO AL CARRITO
OBJETIVO: Validar que un producto puede agregarse al carrito.
PASOS:
1. Seleccionar un producto de la lista.
2. Hacer clic en "Add to cart".
3. Ir al carrito y verificar que el producto esté presente.
RESULTADO ESPERADO: El producto aparece en la lista del carrito.

3.3 COMPLETAR UNA COMPRA
OBJETIVO: Simular la compra de un producto desde el carrito.
PASOS:
1. Navegar al carrito.
2. Hacer clic en "Place Order".
3. Llenar el formulario de compra.
4. Confirmar la compra.
RESULTADO ESPERADO: Se muestra un mensaje confirmando la compra.

4. EJECUCION DE LAS PRUEBAS
Para ejecutar todas las pruebas:
 pytest --html=report.html
Esto generará un informe en formato HTML con los resultados.

5. CONSIDERACIONES FINALES
- Se recomienda utilizar esperas explícitas (WebDriverWait) para mejorar la estabilidad de las pruebas.
- Para futuras mejoras, se podría implementar Page Object Model (POM) para organizar mejor el código.

Para cualquier duda o mejora, contáctanos o revisa la documentación oficial de Selenium en:
 https://www.selenium.dev/documentation/

