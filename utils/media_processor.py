import os
from io import BytesIO
from PIL import Image


def resize_image(data: bytes, max_width: int = 1200, max_height: int = 1200,
                                  quality: int = 85) -> bytes:
                                        img = Image.open(BytesIO(data))

    if img.width <= max_width and img.height <= max_height:
              return data

    ratio = min(max_width / img.width, max_height / img.height)
    new_size = (int(img.width * ratio), int(img.height * ratio))
    img = img.resize(new_size, Image.LANCZOS)

    buf = BytesIO()
    fm
