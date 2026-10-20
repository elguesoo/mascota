"""Build transparent Spiffo animations from the generated frame sheet."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parent
SHEET = ROOT / "spiffo-expressive-frames-v2.png"
HISTORY = ROOT / "historial"
GIF_OUTPUT = HISTORY / "spiffo.gif"
APNG_OUTPUT = HISTORY / "spiffo-animado-transparente.png"


def main() -> None:
    with Image.open(SHEET) as source:
        sheet = source.convert("RGBA")
    if sheet.size != (1536, 1024):
        raise ValueError(f"Unexpected frame sheet size: {sheet.size}")

    HISTORY.mkdir(exist_ok=True)

    frames = []
    for index in range(8):
        left = (index % 4) * 384
        top = (index // 4) * 512
        frame = sheet.crop((left, top, left + 384, top + 512))
        visible = frame.getchannel("A").point(lambda alpha: 255 if alpha > 128 else 0).getbbox()
        if visible is None:
            raise ValueError(f"Frame {index} is empty")

        # Keep the feet in place while the body moves between poses.
        aligned = Image.new("RGBA", frame.size, (0, 0, 0, 0))
        aligned.alpha_composite(frame, (0, 480 - visible[3]))
        frames.append(aligned)

    durations = [310, 200, 210, 190, 150, 230, 230, 300]

    frames[0].save(
        APNG_OUTPUT,
        save_all=True,
        append_images=frames[1:],
        duration=durations,
        loop=0,
        disposal=0,
        blend=0,
    )

    gif_frames = []
    for frame in frames:
        indexed = frame.quantize(colors=255, method=Image.Quantize.FASTOCTREE)
        transparent = frame.getchannel("A").point(lambda alpha: 255 if alpha < 128 else 0)
        indexed.paste(255, mask=transparent)
        indexed.info["transparency"] = 255
        gif_frames.append(indexed)

    gif_frames[0].save(
        GIF_OUTPUT,
        save_all=True,
        append_images=gif_frames[1:],
        duration=durations,
        loop=0,
        disposal=2,
        transparency=255,
        optimize=False,
    )
    SHEET.unlink()
    print(GIF_OUTPUT)
    print(APNG_OUTPUT)
    print(f"Deleted intermediate: {SHEET}")


if __name__ == "__main__":
    main()
