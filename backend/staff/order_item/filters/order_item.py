from django_filters import FilterSet, NumberFilter

from base.common.constant.db_fields import CommonFields, OrderFields, OrderItemFields, MenuFields
from base.common.filters.common import NumberInFilter
from base.order_item.models import OrderItem


class OrderItemListQueryFields:
    SEARCH_FIELDS = ()
    ORDER_FIELDS = (
        "__".join([OrderItemFields.MENU, MenuFields.NAME]),
        CommonFields.ID,
    )
    ORDER_DEFAULT_FIELD = "__".join([OrderItemFields.MENU, MenuFields.NAME])
    FILTERSET_FIELDS = (
        "__".join([OrderItemFields.ORDER, OrderFields.CUSTOMER_ID])
    )


class OrderItemFilter(FilterSet):
    order_id__in = NumberInFilter(field_name=OrderItemFields.ORDER_ID, lookup_expr="in")
    order__customer_id = NumberFilter(field_name="__".join([OrderItemFields.ORDER, OrderFields.CUSTOMER_ID]))

    class Meta:
        model = OrderItem
        fields = ()
