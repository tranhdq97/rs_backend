from django.db import models
from django.db.models import ForeignKey

from base.common.constant.app_label import ModelAppLabel
from base.common.constant.db_table import DBTable
from base.common.models.base import DateTimeModel, Creator, Editor
from base.menu.models import Menu
from base.order.models.order import Order


class OrderItem(DateTimeModel, Creator, Editor):
    order = models.ForeignKey(Order, on_delete=models.RESTRICT, related_name=DBTable.ORDER_ITEM)
    menu = ForeignKey(Menu, on_delete=models.RESTRICT, related_name=DBTable.MENU)
    quantity = models.IntegerField()
    served_quantity = models.IntegerField(default=0)
    served_at = models.DateTimeField(null=True)

    class Meta:
        db_table = DBTable.ORDER_ITEM
        app_label = ModelAppLabel.ORDER_ITEM
