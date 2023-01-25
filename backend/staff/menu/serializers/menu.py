from rest_framework import serializers

from base.common.constant.db_fields import CommonFields, MenuFields
from base.common.utils.serializer import ForeignKeyField
from base.file_management.models import FileManagement
from base.file_management.serializers.file_management import FileManagementRetrieveSlz
from base.master.models import MasterMenuType
from base.master.serializers.base_master import MasterBaseSlz
from base.menu.models import Menu


class MenuBaseSlz(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = (CommonFields.ID, MenuFields.NAME, MenuFields.PRICE)


class MenuCreateSlz(MenuBaseSlz):
    type_id = ForeignKeyField(model=MasterMenuType)
    photo_id = ForeignKeyField(model=FileManagement, required=False)

    class Meta:
        model = MenuBaseSlz.Meta.model
        fields = MenuBaseSlz.Meta.fields + (
            MenuFields.DESC,
            MenuFields.TYPE_ID,
            MenuFields.PHOTO_ID,
        )


class MenuUpdateSlz(MenuBaseSlz):
    type_id = ForeignKeyField(model=MasterMenuType, required=False)
    photo_id = ForeignKeyField(model=FileManagement, required=False)

    class Meta:
        model = MenuBaseSlz.Meta.model
        fields = MenuBaseSlz.Meta.fields + (
            MenuFields.DESC,
            MenuFields.IS_AVAILABLE,
            MenuFields.TYPE_ID,
            MenuFields.PHOTO_ID,
        )
        extra_kwargs = {
            MenuFields.NAME: {"required": False},
            MenuFields.PRICE: {"required": False},
        }


class MenuRetrieveSlz(MenuBaseSlz):
    type = MasterBaseSlz()
    photo = FileManagementRetrieveSlz()

    class Meta:
        model = MenuBaseSlz.Meta.model
        fields = MenuBaseSlz.Meta.fields + (
            MenuFields.DESC,
            MenuFields.IS_AVAILABLE,
            MenuFields.TYPE,
            MenuFields.PHOTO,
        )


class MenuListSlz(MenuBaseSlz):
    type = MasterBaseSlz()
    photo = FileManagementRetrieveSlz()

    class Meta:
        model = MenuBaseSlz.Meta.model
        fields = MenuBaseSlz.Meta.fields + (
            MenuFields.IS_AVAILABLE,
            MenuFields.TYPE,
            MenuFields.PHOTO,
        )
