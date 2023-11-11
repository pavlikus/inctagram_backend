from typing import Self

from django.core.files.storage import FileSystemStorage
from sorl.thumbnail import delete
from sorl.thumbnail.images import ImageFile


class OverwriteStorage(FileSystemStorage):
    def get_available_name(self: Self, name: str) -> str:
        return name

    def _save(self: Self, name: str, content: any) -> Self:
        if self.exists(name):
            image = ImageFile(name)
            delete(image)
        return super()._save(name, content)
