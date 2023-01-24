from base.common.constant.db_fields import CommonFields, UserFields, ProfileFields


class CustomerListQueryFields:
    SEARCH_FIELDS = (
        "__".join([UserFields.PROFILE, ProfileFields.PHONE_NUMBER]),
        "__".join([UserFields.PROFILE, ProfileFields.FIRST_NAME]),
        "__".join([UserFields.PROFILE, ProfileFields.LAST_NAME]),
    )
    ORDER_FIELDS = (
        CommonFields.ID,
        "__".join([UserFields.PROFILE, ProfileFields.FIRST_NAME]),
        "__".join([UserFields.PROFILE, ProfileFields.LAST_NAME])
    )
    ORDER_DEFAULT_FIELD = f"{CommonFields.ID}"
    FILTERSET_FIELDS = (
        "__".join([UserFields.PROFILE, ProfileFields.FIRST_NAME]),
        "__".join([UserFields.PROFILE, ProfileFields.LAST_NAME]),
        "__".join([UserFields.PROFILE, ProfileFields.PHONE_NUMBER]),
    )
