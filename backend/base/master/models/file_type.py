from base.common.constant.app_label import ModelAppLabel
from base.common.constant.db_table import DBTable
from base.common.models.base import MasterBaseModel


class MasterFileType(MasterBaseModel):
    class Meta:
        db_table = DBTable.MASTER_FILE_TYPE
        app_label = ModelAppLabel.MASTER
