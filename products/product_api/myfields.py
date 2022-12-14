
import io
from datetime import datetime

from PIL import Image
from django.core.files.base import ContentFile
from django.db import models
from django.db.models.fields.files import ImageFieldFile


class WEBPFieldFile(ImageFieldFile):

    def save(self, name, content, save=True):
        time_value = str(datetime.now()).replace(':', '.')

        if name.split(".")[-1] in ["jpeg", "jpg", "png"]:
            content.file.seek(0)
            image = Image.open(content.file)
            image_bytes = io.BytesIO()
            image.save(fp=image_bytes, format="WEBP")
            image_content_file = ContentFile(content=image_bytes.getvalue())
            webp_name = f"{''.join(name.split('.')[:-1])}{time_value}.webp"
            super().save(webp_name, image_content_file, save)

        name = f"{''.join(name.split('.')[:-1])}{time_value}.{name.split('.')[-1]}"
        super().save(name, content, save)


class WEBPField(models.ImageField):
    attr_class = WEBPFieldFile
