from rest_framework import serializers

from base.common.constant.db_fields import CommonFields, OrderFields
from base.common.utils.serializer import ForeignKeyField
from base.customer.models import Customer
from base.order.models import Order
from base.table.models import Table
from staff.customer.serializers.customer import CustomerRetrieveSlz, CustomerListSlz
from staff.staff.serializers.staff import StaffRetrieveSlz
from staff.table.serializers.table import TableRetrieveSlz, TableListSlz


class OrderBaseSlz(serializers.ModelSerializer):
    created_by = StaffRetrieveSlz(read_only=True)

    class Meta:
        model = Order
        fields = (CommonFields.ID, CommonFields.CREATED_AT, CommonFields.UPDATED_AT, CommonFields.CREATED_BY,)


class OrderCreateSlz(OrderBaseSlz):
    table_id = ForeignKeyField(Table)
    customer_id = ForeignKeyField(Customer, required=False)

    class Meta:
        model = OrderBaseSlz.Meta.model
        fields = OrderBaseSlz.Meta.fields + (
            OrderFields.NUM_PEOPLE, OrderFields.TABLE_ID, OrderFields.CUSTOMER_ID
        )


class OrderUpdateSlz(OrderBaseSlz):
    table_id = ForeignKeyField(Table, required=False)
    customer_id = ForeignKeyField(Customer, required=False)

    class Meta:
        model = OrderBaseSlz.Meta.model
        fields = OrderBaseSlz.Meta.fields + (
            OrderFields.PAID_AT, OrderFields.NUM_PEOPLE, OrderFields.TABLE_ID, OrderFields.CUSTOMER_ID
        )
        extra_kwargs = {
            OrderFields.NUM_PEOPLE: {"required": False}
        }


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
