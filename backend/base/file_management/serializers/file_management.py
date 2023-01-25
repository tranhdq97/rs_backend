from rest_framework import serializers

from base.common.constant import message
from base.common.constant.db_fields import CommonFields, FileManagementFields
from base.common.constant.master import MasterFileTypeID
from base.common.utils.exceptions import APIErr
from base.common.utils.serializer import ForeignKeyField
from base.file_management.models import FileManagement
from base.master.models import MasterFileType
from base.master.serializers.base_master import MasterBaseSlz


class FileManagementBaseSlz(serializers.ModelSerializer):
    class Meta:
        model = FileManagement
        fields = (
            CommonFields.ID,
            FileManagementFields.FILE,
        )

    def validate(self, attrs):
        extension_switcher = {
            MasterFileTypeID.IMAGE: ("jpeg", "jpg", "gif", "svg", "png", "tiff", "tif"),
            MasterFileTypeID.DOCUMENT: ("pdf", "doc", "docx", "html", "htm", "xls", "xlsx", "txt"),
            MasterFileTypeID.VIDEO: ("mp4", "avi", "mov", "flv"),
            MasterFileTypeID.PRESENTATION: ("ppt", "pptx", "odp", "key"),
            MasterFileTypeID.AUDIO: ("m4a", "mp3", "wav"),
        }
        file = attrs.get(FileManagementFields.FILE).name
        file_ext = file.split(".")[-1]
        valid_extensions = extension_switcher.get(attrs.get(FileManagementFields.TYPE_ID))
        if valid_extensions and file_ext not in valid_extensions:
            raise APIErr(message.NOT_MATCHED_FILE_TYPE)

        return attrs


class FileManagementCreateSlz(FileManagementBaseSlz):
    type_id = ForeignKeyField(model=MasterFileType, required=False)

    class Meta:
        model = FileManagementBaseSlz.Meta.model
        fields = FileManagementBaseSlz.Meta.fields + (
            FileManagementFields.NAME,
            FileManagementFields.DESC,
            FileManagementFields.TYPE_ID,
        )


class FileManagementListSlz(FileManagementBaseSlz):
    type_id = ForeignKeyField(model=MasterFileType)

    class Meta:
        model = FileManagementBaseSlz.Meta.model
        fields = FileManagementBaseSlz.Meta.fields + (
            FileManagementFields.NAME,
            FileManagementFields.TYPE_ID,
        )


class FileManagementRetrieveSlz(FileManagementBaseSlz):
    type = MasterBaseSlz()

    class Meta:
        model = FileManagementBaseSlz.Meta.model
        fields = FileManagementBaseSlz.Meta.fields + (
            FileManagementFields.NAME,
            FileManagementFields.DESC,
            FileManagementFields.TYPE,
        ) + (
             CommonFields.CREATED_AT,
             CommonFields.UPDATED_AT,
         )


class FileManagementUpdateSlz(FileManagementBaseSlz):
    type_id = ForeignKeyField(MasterFileType, required=False)

    class Meta:
        model = FileManagementBaseSlz.Meta.model
        fields = FileManagementBaseSlz.Meta.fields + (
            FileManagementFields.NAME,
            FileManagementFields.DESC,
            FileManagementFields.TYPE_ID,
        )
        extra_kwargs = {
            FileManagementFields.FILE: {"read_only": True},
        }
