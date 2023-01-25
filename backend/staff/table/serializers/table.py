from rest_framework import serializers

from base.common.constant.db_fields import CommonFields, TableFields
from base.table.models import Table


class TableBaseSlz(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = (CommonFields.ID, TableFields.NAME)


class TableCreateSlz(TableBaseSlz):
    class Meta:
        model = TableBaseSlz.Meta.model
        fields = TableBaseSlz.Meta.fields


class TableUpdateSlz(TableBaseSlz):
    class Meta:
        model = TableBaseSlz.Meta.model
        fields = TableBaseSlz.Meta.fields + (TableFields.IS_AVAILABLE,)
        extra_kwargs = {
            TableFields.NAME: {"required": False}
        }


class TableRetrieveSlz(TableBaseSlz):
    class Meta:
        model = TableBaseSlz.Meta.model
        fields = TableBaseSlz.Meta.fields + (TableFields.IS_AVAILABLE,)


class TableListSlz(TableBaseSlz):
    class Meta:
        model = TableBaseSlz.Meta.model
        fields = TableBaseSlz.Meta.fields + (TableFields.IS_AVAILABLE,)
