from rest_framework import serializers

from base.address.models import Address
from base.common.constant.db_fields import CommonFields, ProfileFields
from base.common.utils.serializer import ForeignKeyField
from base.file_management.models import FileManagement
from base.file_management.serializers.file_management import FileManagementRetrieveSlz
from base.master.models import MasterSex
from base.master.serializers.base_master import MasterBaseSlz
from base.profile.models import Profile
from staff.address.serializers.address import AddressRetrieveSlz, AddressListSlz


class ProfileBaseSlz(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (CommonFields.ID, ProfileFields.PHONE_NUMBER, ProfileFields.LAST_NAME, ProfileFields.FIRST_NAME)


class ProfileCreateSlz(ProfileBaseSlz):
    address_id = ForeignKeyField(Address)
    photo_id = ForeignKeyField(FileManagement)
    sex_id = ForeignKeyField(MasterSex)

    class Meta:
        model = ProfileBaseSlz.Meta.model
        fields = ProfileBaseSlz.Meta.fields + (
            ProfileFields.DOB, ProfileFields.ADDRESS_ID, ProfileFields.PHOTO_ID, ProfileFields.SEX_ID
        )


class ProfileRetrieveSlz(ProfileBaseSlz):
    address = AddressRetrieveSlz()
    photo = FileManagementRetrieveSlz()
    sex = MasterBaseSlz()

    class Meta:
        model = ProfileBaseSlz.Meta.model
        fields = ProfileBaseSlz.Meta.fields + (
            ProfileFields.DOB, ProfileFields.ADDRESS, ProfileFields.PHOTO, ProfileFields.SEX
        )


class ProfileForUserListSlz(ProfileBaseSlz):
    address = AddressListSlz()
    sex = MasterBaseSlz()

    class Meta:
        model = ProfileBaseSlz.Meta.model
        fields = ProfileBaseSlz.Meta.fields + (
            ProfileFields.DOB, ProfileFields.ADDRESS, ProfileFields.SEX
        )


class ProfileUpdateSlz(ProfileBaseSlz):
    photo_id = ForeignKeyField(FileManagement, required=False)
    sex_id = ForeignKeyField(MasterSex, required=False)

    class Meta:
        model = ProfileBaseSlz.Meta.model
        fields = ProfileBaseSlz.Meta.fields + (
            ProfileFields.DOB, ProfileFields.PHOTO_ID, ProfileFields.SEX_ID
        )
