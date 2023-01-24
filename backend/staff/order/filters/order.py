from base.common.constant.db_fields import CommonFields, OrderFields, TableFields, UserFields, ProfileFields


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
