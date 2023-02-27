from rest_framework import serializers

from base.common.constant.db_fields import CommonFields, OrderFields
from base.common.utils.serializer import ForeignKeyField
from base.customer.models import Customer
from base.order.models import Order
from base.table.models import Table
from staff.customer.serializers.customer import CustomerRetrieveSlz, CustomerListSlz
from staff.staff.serializers.staff import StaffRetrieveSlz
from staff.table.serializers.table import TableRetrieveSlz, TableListSlz
from django.db import transaction

class OrderBaseSlz(serializers.ModelSerializer):
    created_by = StaffRetrieveSlz(read_only=True)

    class Meta:
        model = Order
        fields = (CommonFields.ID, CommonFields.CREATED_AT, CommonFields.UPDATED_AT, CommonFields.CREATED_BY,)


class OrderCreateSlz(OrderBaseSlz):
    table_id = ForeignKeyField(Table, write_only=True)
    customer_id = ForeignKeyField(Customer, required=False, write_only=True)
    table = TableRetrieveSlz(read_only=True)
    customer = CustomerRetrieveSlz(read_only=True)

    class Meta:
        model = OrderBaseSlz.Meta.model
        fields = OrderBaseSlz.Meta.fields + (
            OrderFields.NUM_PEOPLE, OrderFields.TABLE_ID, OrderFields.CUSTOMER_ID, OrderFields.TABLE,
            OrderFields.CUSTOMER
        )


class OrderUpdateSlz(OrderBaseSlz):
    table_id = ForeignKeyField(Table, required=False, write_only=True)
    customer_id = ForeignKeyField(Customer, required=False, write_only=True)
    table = TableRetrieveSlz(read_only=True)
    customer = CustomerRetrieveSlz(read_only=True)

    class Meta:
        model = OrderBaseSlz.Meta.model
        fields = OrderBaseSlz.Meta.fields + (
            OrderFields.PAID_AT, OrderFields.NUM_PEOPLE, OrderFields.TABLE_ID, OrderFields.CUSTOMER_ID,
            OrderFields.TABLE, OrderFields.CUSTOMER
        )
        extra_kwargs = {
            OrderFields.NUM_PEOPLE: {"required": False}
        }

    def update(self, instance, validated_data):
        if validated_data.get(OrderFields.PAID_AT):
            with transaction.atomic():
                order_items = instance.order_item.all()
                for order_item in order_items:
                    order_item.menu.num_ordered += order_item.served_quantity
                    order_item.menu.save()
        return super().update(instance, validated_data)


class OrderRetrieveSlz(OrderBaseSlz):
    table = TableRetrieveSlz()
    customer = CustomerRetrieveSlz()

    class Meta:
        model = OrderBaseSlz.Meta.model
        fields = OrderBaseSlz.Meta.fields + (
            OrderFields.PAID_AT, OrderFields.NUM_PEOPLE, OrderFields.TABLE, OrderFields.CUSTOMER
        )


class OrderListSlz(OrderBaseSlz):
    table = TableListSlz()
    customer = CustomerListSlz()

    class Meta:
        model = OrderBaseSlz.Meta.model
        fields = OrderBaseSlz.Meta.fields + (
            OrderFields.PAID_AT, OrderFields.NUM_PEOPLE, OrderFields.TABLE, OrderFields.CUSTOMER
        )
