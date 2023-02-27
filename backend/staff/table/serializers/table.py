from rest_framework import serializers

from base.common.constant.db_fields import CommonFields, TableFields
from base.table.models import Table


class TableBaseSlz(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = (CommonFields.ID, TableFields.NAME, TableFields.IS_AVAILABLE,)


class TableCreateSlz(TableBaseSlz):
    class Meta:
        model = TableBaseSlz.Meta.model
        fields = TableBaseSlz.Meta.fields
        extra_kwargs = {
            TableFields.IS_AVAILABLE: {"read_only": True}
        }


class TableUpdateSlz(TableBaseSlz):
    class Meta:
        model = TableBaseSlz.Meta.model
        fields = TableBaseSlz.Meta.fields
        extra_kwargs = {
            TableFields.NAME: {"required": False}
        }


class TableRetrieveSlz(TableBaseSlz):
    class Meta:
        model = TableBaseSlz.Meta.model
        fields = TableBaseSlz.Meta.fields


class TableListSlz(TableBaseSlz):
    class Meta:
        model = TableBaseSlz.Meta.model
        fields = TableBaseSlz.Meta.fields
