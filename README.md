# Animar un personaje desde una imagen

1. Guarda tu imagen en `entrada/` (por ejemplo, `entrada/personaje.png`).
2. Dile al asistente qué personaje debe aislar y cómo quieres que se mueva. Puedes escribir las instrucciones directamente en el chat.
3. El asistente quitará el fondo, creará la animación y guardará en `salida/` el GIF, el PNG animado si es posible y la hoja de fotogramas.

Ejemplo de petición: «Usa `entrada/personaje.png`. Quita el fondo, conserva la ropa y los accesorios, haz que respire y parpadee, y crea un bucle suave».

Los archivos `spiffo-reference.png`, `spiffo-expressive-frames-v2.png`, `spiffo.gif` y `spiffo-animado-transparente.png` son un ejemplo ya terminado. La imagen de referencia se conserva intacta. `build_gif.py` recompone **solo ese ejemplo** a partir de su hoja de fotogramas; para ejecutarlo se necesita Pillow (`pip install Pillow`).
