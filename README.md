# Animate a character from an image

1. Place your image in `entrada/` (for example, `entrada/character.png`).
2. Tell the assistant which character to isolate and how you want it to move. You can give the instructions directly in chat.
3. The assistant will remove the background, create the animation, and save the finished files in `historial/`.

Example request: “Use `entrada/character.png`. Remove the background, keep the clothing and accessories, make the character breathe and blink, and create a smooth loop.”

`historial/` stores the finished animations. Intermediate files, such as frame sheets, are removed when the work is complete. The input image is kept unchanged.

The repository includes an example animation at [`historial/spiffo.gif`](historial/spiffo.gif). The original Spiffo reference image is not included. `build_gif.py` can rebuild the example only when its intermediate frame sheet, `spiffo-expressive-frames-v2.png`, is present in the project root; the script deletes that sheet after building the GIF. Pillow is required (`pip install Pillow`).
