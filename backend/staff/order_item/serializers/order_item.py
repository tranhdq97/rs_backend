from rest_framework import serializers

from base.common.constant import message
from base.common.constant.db_fields import CommonFields, OrderItemFields
from base.common.utils.exceptions import APIErr
from base.common.utils.serializer import ForeignKeyField
from base.menu.models import Menu
from base.order.models import Order
from base.order_item.models import OrderItem
from staff.menu.serializers.menu import MenuRetrieveSlz, MenuListSlz
from staff.order.serializers.order import OrderRetrieveSlz, OrderListSlz
from staff.staff.serializers.staff import StaffRetrieveSlz


class OrderItemBaseSlz(serializers.ModelSerializer):
    created_by = StaffRetrieveSlz(read_only=True)

    def validate(self, attrs):
        quantity = self.instance.quantity
        served_quantity = attrs.get(OrderItemFields.SERVED_QUANTITY)
        if quantity is not None and quantity < 1:
            raise APIErr(message.INVALID_INPUT)
        if quantity is not None and served_quantity is not None and (served_quantity < 1 or served_quantity > quantity):
            raise APIErr(message.INVALID_INPUT)

        return attrs

    class Meta:
        model = OrderItem
        fields = (CommonFields.ID, CommonFields.CREATED_AT, CommonFields.UPDATED_AT, CommonFields.CREATED_BY,
                  OrderItemFields.QUANTITY, OrderItemFields.SERVED_QUANTITY, OrderItemFields.SERVED_AT)


class OrderItemCreateSlz(OrderItemBaseSlz):
    order_id = ForeignKeyField(Order)
    menu_id = ForeignKeyField(Menu)

    class Meta:
        model = OrderItemBaseSlz.Meta.model
        fields = OrderItemBaseSlz.Meta.fields + (OrderItemFields.ORDER_ID, OrderItemFields.MENU_ID)
        extra_kwargs = {
            OrderItemFields.SERVED_QUANTITY: {"read_only": True},
            OrderItemFields.SERVED_AT: {"read_only": True},
        }


class OrderItemUpdateSlz(OrderItemBaseSlz):
    order_id = ForeignKeyField(Order, required=False)
    menu_id = ForeignKeyField(Menu, required=False)

    class Meta:
        model = OrderItemBaseSlz.Meta.model
        fields = OrderItemBaseSlz.Meta.fields + (OrderItemFields.ORDER_ID, OrderItemFields.MENU_ID)
        extra_kwargs = {
            OrderItemFields.QUANTITY: {"required": False},
            OrderItemFields.SERVED_QUANTITY: {"required": False},
            OrderItemFields.SERVED_AT: {"required": False},
        }


class OrderItemRetrieveSlz(OrderItemBaseSlz):
    order = OrderRetrieveSlz()
    menu = MenuRetrieveSlz()

    class Meta:
        model = OrderItemBaseSlz.Meta.model
        fields = OrderItemBaseSlz.Meta.fields + (OrderItemFields.ORDER, OrderItemFields.MENU)


class OrderItemListSlz(OrderItemBaseSlz):
    order = OrderListSlz()
    menu = MenuListSlz()

    class Meta:
        model = OrderItemBaseSlz.Meta.model
        fields = OrderItemBaseSlz.Meta.fields + (OrderItemFields.ORDER, OrderItemFields.MENU)