from django.db import models

from base.common.constant.app_label import ModelAppLabel
from base.common.constant.db_table import DBTable
from base.common.models.base import CustomBaseUserModel, Creator, Editor, BaseModel
from base.profile.models import Profile


class Customer(BaseModel, Creator, Editor):
    profile = models.OneToOneField(Profile, on_delete=models.RESTRICT, null=True, related_name=DBTable.CUSTOMER)

    @property
    def is_staff(self):
        return False

    def save(self, *args, **kwargs):
        super(Customer, self).save(*args, **kwargs)

    class Meta:
        db_table = DBTable.CUSTOMER
        app_label = ModelAppLabel.CUSTOMER
