# Animar un personaje desde una imagen

1. Guarda tu imagen en `entrada/` (por ejemplo, `entrada/personaje.png`).
2. Dile al asistente qué personaje debe aislar y cómo quieres que se mueva. Puedes escribir las instrucciones directamente en el chat.
3. El asistente quitará el fondo, creará la animación y guardará los archivos finales en `historial/`.

Ejemplo de petición: «Usa `entrada/personaje.png`. Quita el fondo, conserva la ropa y los accesorios, haz que respire y parpadee, y crea un bucle suave».

`historial/` conserva los GIF y PNG animados terminados. Los archivos intermedios, como las hojas de fotogramas, se borran al acabar. La imagen de entrada se conserva intacta.

El ejemplo de Spiffo está en `spiffo-reference.png`; sus animaciones están en `historial/`. `build_gif.py` recompone **solo ese ejemplo** a partir de su hoja de fotogramas y la elimina al terminar; para ejecutarlo se necesita Pillow (`pip install Pillow`).
