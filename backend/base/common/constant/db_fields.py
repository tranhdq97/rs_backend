from base.common.utils.utils import BaseEnum


# --------------------------------------  Common
class CommonFields(str, BaseEnum):
    ID = "id"
    USER = "user"
    IS_DELETED = "is_deleted"
    CREATED_AT = "created_at"
    UPDATED_AT = "updated_at"
    CREATED_BY = "created_by"
    CREATED_BY_ID = "created_by_id"
    UPDATED_BY = "updated_by"
    UPDATED_BY_ID = "updated_by_id"


# --------------------------------------  Master
class MasterFields(str, BaseEnum):
    NAME = "name"
    PARENT = "parent"
    PARENT_ID = "parent_id"


class MasterCountryFields(str, BaseEnum):
    CODE = "code"


class MasterCityFields(str, BaseEnum):
    COUNTRY = "country"
    COUNTRY_ID = "country_id"


class MasterDistrictFields(str, BaseEnum):
    CITY = "city"
    CITY_ID = "city_id"
    ZIP_CODE = "zipcode"


# --------------------------------------  Others
class AddressFields(str, BaseEnum):
    DISTRICT = "district"
    DISTRICT_ID = "district_id"
    STREET = "street"


class ProfileFields(str, BaseEnum):
    FIRST_NAME = "first_name"
    LAST_NAME = "last_name"
    DOB = "dob"
    PHONE_NUMBER = "phone_number"
    SEX = "sex"
    SEX_ID = "sex_id"
    ADDRESS = "address"
    ADDRESS_ID = "address_id"
    PHOTO = "photo"
    PHOTO_ID = "photo_id"


class UserFields(str, BaseEnum):
    PROFILE = "profile"
    PROFILE_ID = "profile_id"
    TYPE = "type"
    TYPE_ID = "type_id"
    EMAIL = "email"
    PASSWORD = "password"
    NEW_PASSWORD = "new_password"
    IS_ACTIVATE = "is_activate"
    IS_LEAVE = "is_leave"
    IS_ADMIN = "is_admin"
    LAST_LOGIN = "last_login"


class FileManagementFields(str, BaseEnum):
    NAME = "name"
    DESC = "desc"
    FILE = "file"
    TYPE = "type"
    TYPE_ID = "type_id"
    IS_DELETED = "is_deleted"


class MenuFields(str, BaseEnum):
    NAME = "name"
    TYPE = "type"
    TYPE_ID = "type_id"
    PRICE = "price"
    IS_AVAILABLE = "is_available"
    PHOTO = "photo"
    PHOTO_ID = "photo_id"
    DESC = "desc"


class TableFields(str, BaseEnum):
    NAME = "name"
    IS_AVAILABLE = "is_available"


class OrderFields(str, BaseEnum):
    TABLE = "table"
    TABLE_ID = "table_id"
    CUSTOMER = "customer"
    CUSTOMER_ID = "customer_id"
    PAID_AT = "paid_at"
    NUM_PEOPLE = "num_people"


class OrderItemFields(str, BaseEnum):
    ORDER = "order"
    ORDER_ID = "order_id"
    MENU = "menu"
    MENU_ID = "menu_id"
    QUANTITY = "quantity"
    SERVED_QUANTITY = "served_quantity"
    SERVED_AT = "served_at"
