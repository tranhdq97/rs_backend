from django.db import transaction
from rest_framework import serializers

from base.common.constant.db_fields import CommonFields, UserFields
from base.customer.models.customer import Customer
from base.profile.models import Profile
from staff.profile.serializers.profile import ProfileRetrieveSlz, ProfileForUserListSlz, ProfileCreateSlz, \
    ProfileUpdateSlz


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


class CustomerUpdateSlz(CustomerBaseSlz):
    profile = ProfileUpdateSlz(required=True)

    class Meta:
        model = CustomerBaseSlz.Meta.model
        fields = CustomerBaseSlz.Meta.fields + (UserFields.PROFILE,)

    def update(self, instance, validated_data):
        with transaction.atomic():
            profile_data = validated_data.get(UserFields.PROFILE, {})
            for key, value in profile_data.items():
                setattr(instance.profile, key, value)

            instance.profile.save()
            instance.save()
            return instance


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
