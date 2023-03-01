from django.db import models

from base.common.constant.app_label import ModelAppLabel
from base.common.constant.db_table import DBTable
from base.common.models.base import DateTimeModel, Creator, Editor


class Table(DateTimeModel, Creator, Editor):
    name = models.CharField(max_length=32)
    is_available = models.BooleanField(default=True)

    class Meta:
        db_table = DBTable.TABLE
        app_label = ModelAppLabel.TABLE
