from rest_framework import serializers

from base.common.constant.db_fields import CommonFields, UserFields
from base.common.utils.serializer import ForeignKeyField
from base.customer.models.customer import Customer
from base.profile.models import Profile
from staff.profile.serializers.profile import ProfileRetrieveSlz, ProfileForUserListSlz


class CustomerBaseSlz(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (CommonFields.ID,)


class CustomerCreateSlz(CustomerBaseSlz):
    profile_id = ForeignKeyField(Profile, required=False)

    class Meta:
        model = CustomerBaseSlz.Meta.model
        fields = CustomerBaseSlz.Meta.fields + (UserFields.PROFILE_ID,)


class CustomerRetrieveSlz(CustomerBaseSlz):
    profile = ProfileRetrieveSlz()

    class Meta:
        model = CustomerBaseSlz.Meta.model
        fields = CustomerBaseSlz.Meta.fields + (UserFields.PROFILE,)


class CustomerListSlz(CustomerBaseSlz):
    profile = ProfileForUserListSlz()

    class Meta:
        model = CustomerBaseSlz.Meta.model
        fields = CustomerBaseSlz.Meta.fields + (UserFields.PROFILE,)
