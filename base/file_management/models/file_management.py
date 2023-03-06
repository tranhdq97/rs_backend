from io import BytesIO

from PIL import Image
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models

from base.common.constant.app_label import ModelAppLabel
from base.common.constant.db_table import DBTable
from base.common.constant.master import MasterFileTypeID
from base.common.custom.storages import MediaStorage
from base.common.models.base import DateTimeModel
from base.common.utils.strings import get_file_field_directory, get_thumbnail_directory
from base.common.utils.validators import FileSizeValidator
from base.master.models import MasterFileType


class FileManagement(DateTimeModel):
    UPLOAD_SIZE_LIMIT = 200  # 200MB

    name = models.CharField(max_length=256, null=True)
    thumbnail = models.ImageField(upload_to=get_thumbnail_directory, max_length=500, null=True,
                                  storage=MediaStorage if settings.USE_S3 else FileSystemStorage)
    desc = models.TextField(null=True)
    file = models.FileField(upload_to=get_file_field_directory, validators=[FileSizeValidator(UPLOAD_SIZE_LIMIT)],
                            storage=MediaStorage if settings.USE_S3 else FileSystemStorage)
    type = models.ForeignKey(MasterFileType, on_delete=models.RESTRICT, related_name=DBTable.FILE_MANAGEMENT,
                             default=MasterFileTypeID.ANY)

    class Meta:
        db_table = DBTable.FILE_MANAGEMENT
        app_label = ModelAppLabel.FILE_MANAGEMENT

    def _create_thumbnail(self, file):
        try:
            img = Image.open(file)
        except IOError:
            self.thumbnail = None
        else:
            img.thumbnail((settings.THUMBNAIL_SIZE, settings.THUMBNAIL_SIZE))
            img_file = BytesIO()
            img.save(img_file, img.format)
            self.thumbnail.save(
                file.name,
                InMemoryUploadedFile(img_file, file.name, file.name, file.content_type, img.size, file.charset),
                save=False
            )

    def save(self, *args, **kwargs):
        self._create_thumbnail(self.file.file)
        super().save(*args, **kwargs)
