# Animación de Spiffo

Este proyecto usa `spiffo-reference.png` como referencia visual. Es la imagen proporcionada por el usuario y debe conservarse intacta.

## Uso para nuevas imágenes

- El usuario coloca una imagen en `entrada/` y describe la animación en el chat. No hace falta que escriba código ni prepare la imagen.
- Identifica el personaje solicitado, elimina el fondo y los elementos ajenos, y conserva sus rasgos, estilo y accesorios según la petición.
- Anima el personaje de acuerdo con las instrucciones del usuario. Haz que el bucle vuelva con suavidad a la pose inicial.
- Guarda en `historial/` el GIF y, cuando sea posible, un PNG animado con transparencia de mejor calidad. Usa nombres relacionados con la imagen de entrada para distinguir trabajos y conservar las animaciones anteriores.
- Al terminar y verificar las exportaciones, elimina los archivos intermedios usados para crearlas, como hojas de fotogramas o máscaras. Conserva intacta la imagen de entrada.
- Comprueba visualmente la silueta, la transparencia, la continuidad del bucle y que los archivos exportados se reproduzcan. No alteres la imagen de entrada.

El encargo de Spiffo que sigue documenta el ejemplo incluido en la raíz. Sus archivos permanecen en la raíz para conservar los nombres originales.

## Encargo actual

Crear una animación de Spiffo con más vida a partir de esa referencia. Aislar al personaje sobre fondo transparente: no incluir zombis, lluvia, edificio, vehículo ni otros elementos del escenario. Mantener sus rasgos, el estilo de cómic, la mochila y el hacha que lleva en la imagen. Dar expresión al cuerpo mediante respiración, parpadeo, movimiento de orejas, cabeza y cola, y pequeños cambios de postura. El bucle debe volver con suavidad a la pose inicial.

## Archivos y entrega del ejemplo

- Guardar las exportaciones finales en `historial/` y borrar la hoja de fotogramas al terminar.
- Verificar visualmente el bucle, la continuidad de la silueta, la transparencia y la reproducción de las exportaciones.
- Entregar el GIF y, cuando exista, una versión PNG animada con transparencia de mejor calidad.
