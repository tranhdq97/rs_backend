from django.db import models

from base.common.constant.app_label import ModelAppLabel
from base.common.constant.db_fields import MenuFields
from base.common.constant.db_table import DBTable
from base.common.models.base import Creator, Editor, DateTimeModel
from base.file_management.models import FileManagement
from base.master.models import MasterMenuType


class Menu(DateTimeModel, Creator, Editor):
    name = models.CharField(max_length=256)
    type = models.ForeignKey(MasterMenuType, on_delete=models.RESTRICT, related_name=DBTable.MENU)
    price = models.IntegerField()
    is_available = models.BooleanField(default=True)
    desc = models.TextField(null=True, blank=True)
    photo = models.ForeignKey(FileManagement, on_delete=models.RESTRICT, related_name=DBTable.MENU, null=True)

    class Meta:
        unique_together = ((MenuFields.NAME, MenuFields.TYPE_ID),)
        db_table = DBTable.MENU
        app_label = ModelAppLabel.MENU
