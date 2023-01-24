from rest_framework import serializers

from base.common.constant import message
from base.common.constant.constant import RegexPattern
from base.common.constant.db_fields import CommonFields, UserFields
from base.common.utils.exceptions import APIErr
from base.common.utils.serializer import ForeignKeyField
from base.common.utils.strings import check_regex
from base.master.models import MasterStaffType
from base.master.serializers.base_master import MasterBaseSlz
from base.profile.models import Profile
from base.staff.models.staff import Staff
from staff.profile.serializers.profile import ProfileRetrieveSlz, ProfileForUserListSlz


class StaffBaseSlz(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = (CommonFields.ID, UserFields.EMAIL)


class StaffRetrieveSlz(StaffBaseSlz):
    type = MasterBaseSlz()
    profile = ProfileRetrieveSlz()

    class Meta:
        model = StaffBaseSlz.Meta.model
        fields = StaffBaseSlz.Meta.fields + (UserFields.PROFILE, UserFields.TYPE) + (CommonFields.UPDATED_AT,)


class StaffListSlz(StaffBaseSlz):
    type = MasterBaseSlz()
    profile = ProfileForUserListSlz()

    class Meta:
        model = StaffBaseSlz.Meta.model
        fields = StaffBaseSlz.Meta.fields + (UserFields.PROFILE, UserFields.TYPE)


class StaffUpdateSlz(StaffBaseSlz):
    type_id = ForeignKeyField(MasterStaffType)

    class Meta:
        model = StaffBaseSlz.Meta.model
        fields = StaffBaseSlz.Meta.fields + (UserFields.TYPE_ID,)
        extra_kwargs = {
            UserFields.EMAIL: { "read_only": True }
        }


class StaffCreateSlz(StaffBaseSlz):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    profile_id = ForeignKeyField(Profile, required=False)

    class Meta:
        model = StaffBaseSlz.Meta.model
        fields = StaffBaseSlz.Meta.fields + (
            UserFields.EMAIL,
            UserFields.PASSWORD,
            UserFields.PROFILE_ID,
        )

    def validate(self, attrs):
        email = attrs.get(UserFields.EMAIL)
        password = attrs.get(UserFields.PASSWORD)
        if not email:
            raise APIErr(message.MUST_HAVE_EMAIL)

        if self.Meta.model.objects.filter(email=email).exists():
            raise APIErr(message.ALREADY_EXISTS)

        if not check_regex(RegexPattern.PASSWORD, password):
            raise APIErr(message.PASSWORD_INAPPROPRIATE)

        if email == password:
            raise APIErr(message.PASSWORD_MUST_DIFFER_EMAIL)

        return attrs

    def create(self, validated_data):
        return self.Meta.model.objects.create_user(**validated_data)
