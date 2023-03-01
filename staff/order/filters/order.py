from django_filters import FilterSet

from base.common.constant.db_fields import CommonFields, OrderFields, TableFields, UserFields, ProfileFields
from base.common.filters.common import NumberInFilter
from base.order.models import Order


class OrderListQueryFields:
    SEARCH_FIELDS = (
        "__".join([OrderFields.TABLE, TableFields.NAME]),
        "__".join([OrderFields.CUSTOMER, UserFields.PROFILE, ProfileFields.PHONE_NUMBER]),
    )
    ORDER_FIELDS = (
        "__".join([OrderFields.TABLE, TableFields.NAME]),
        CommonFields.ID,
    )
    ORDER_DEFAULT_FIELD = f"{CommonFields.ID}"
    FILTERSET_FIELDS = (
        OrderFields.TABLE_ID,
        "__".join([OrderFields.TABLE, TableFields.NAME]),
        "__".join([OrderFields.CUSTOMER, UserFields.PROFILE, ProfileFields.PHONE_NUMBER]),
    )


class OrderFilter(FilterSet):
    table_id__in = NumberInFilter(field_name=OrderFields.TABLE_ID, lookup_expr="in")

    class Meta:
        model = Order
        fields = ()
