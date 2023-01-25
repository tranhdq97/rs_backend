from base.common.constant.db_fields import CommonFields, TableFields


class TableListQueryFields:
    SEARCH_FIELDS = (
        TableFields.NAME,
    )
    ORDER_FIELDS = (
        CommonFields.ID,
        TableFields.NAME,
    )
    ORDER_DEFAULT_FIELD = f"{TableFields.NAME}"
    FILTERSET_FIELDS = (TableFields.NAME, TableFields.IS_AVAILABLE)
