from base.common.constant.db_fields import CommonFields, OrderFields, OrderItemFields, MenuFields


class OrderItemListQueryFields:
    SEARCH_FIELDS = ()
    ORDER_FIELDS = (
        "__".join([OrderItemFields.MENU, MenuFields.NAME]),
        CommonFields.ID,
    )
    ORDER_DEFAULT_FIELD = "__".join([OrderItemFields.MENU, MenuFields.NAME])
    FILTERSET_FIELDS = (
        OrderItemFields.ORDER_ID,
        "__".join([OrderItemFields.ORDER, OrderFields.CUSTOMER_ID])
    )
