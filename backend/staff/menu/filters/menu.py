from base.common.constant.db_fields import CommonFields, MenuFields


class MenuListQueryFields:
    SEARCH_FIELDS = (
        MenuFields.NAME,
    )
    ORDER_FIELDS = (
        CommonFields.ID,
        MenuFields.PRICE,
        MenuFields.NAME,
    )
    ORDER_DEFAULT_FIELD = f"{MenuFields.NAME}"
    FILTERSET_FIELDS = (MenuFields.NAME, MenuFields.TYPE_ID)
