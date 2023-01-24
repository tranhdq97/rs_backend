from base.common.utils.utils import BaseEnum


class DBTable(str, BaseEnum):
    # Master tables
    MASTER = "master"
    MASTER_COUNTRY = "m_country"
    MASTER_CITY = "m_city"
    MASTER_DISTRICT = "m_district"
    MASTER_SEX = "m_sex"
    MASTER_STAFF_TYPE = "m_staff_type"
    MASTER_MENU_TYPE = "m_menu_type"
    MASTER_FILE_TYPE = "m_file_type"

    ADDRESS = "address"
    PROFILE = "profile"
    STAFF = "staff"
    CUSTOMER = "customer"
    TABLE = "table"
    FILE_MANAGEMENT = "file_management"
    ORDER = "order"
    ORDER_ITEM = "order_item"
    MENU = "menu"
