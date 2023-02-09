from rest_framework import serializers
from django.db import transaction

from base.common.constant.db_fields import CommonFields, UserFields
from base.common.utils.serializer import ForeignKeyField
from base.customer.models.customer import Customer
from base.profile.models import Profile
from staff.profile.serializers.profile import ProfileRetrieveSlz, ProfileForUserListSlz, ProfileCreateSlz


class CustomerBaseSlz(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (CommonFields.ID,)


class CustomerCreateSlz(CustomerBaseSlz):
    profile = ProfileCreateSlz(required=True)

    class Meta:
        model = CustomerBaseSlz.Meta.model
        fields = CustomerBaseSlz.Meta.fields + (UserFields.PROFILE,)

    def create(self, validated_data):
        with transaction.atomic():
            profile = validated_data.get(UserFields.PROFILE)
            instance = Profile.objects.create(**profile)
            return Customer.objects.create(profile=instance)


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
