from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from base.auth.permissions.permission import IsApproved, IsSuperStaff, IsManager
from base.common.constant import message
from base.common.constant.view_action import BaseViewAction
from base.common.custom.pagination import CustomPagination
from base.common.utils.exceptions import PermissionDenied, APIErr
from base.customer.models import Customer
from staff.customer.filters.customer import CustomerListQueryFields
from staff.customer.serializers.customer import CustomerListSlz, CustomerRetrieveSlz, CustomerCreateSlz


class CustomerViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                      mixins.DestroyModelMixin, GenericViewSet):
    permission_classes = (AllowAny,)
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    serializer_class = CustomerListSlz
    queryset = Customer.objects.all()
    search_fields = CustomerListQueryFields.SEARCH_FIELDS
    ordering_fields = CustomerListQueryFields.ORDER_FIELDS
    ordering = CustomerListQueryFields.ORDER_DEFAULT_FIELD
    filterset_fields = CustomerListQueryFields.FILTERSET_FIELDS

    def get_serializer_class(self):
        slz_switcher = {
            BaseViewAction.LIST: CustomerListSlz,
            BaseViewAction.RETRIEVE: CustomerRetrieveSlz,
            BaseViewAction.CREATE: CustomerCreateSlz,
        }
        slz = slz_switcher.get(self.action, self.serializer_class)
        if slz is None:
            raise APIErr(message.NO_SERIALIZER_MATCHED)

        return slz

    def get_permissions(self):
        perm_switcher = {
            BaseViewAction.LIST: (IsApproved,),
            BaseViewAction.RETRIEVE: (IsApproved,),
            BaseViewAction.CREATE: (IsApproved,),
            BaseViewAction.DESTROY: (IsSuperStaff | IsManager,),
        }
        self.permission_classes = perm_switcher.get(self.action, self.permission_classes)
        if self.permission_classes is None:
            raise PermissionDenied()

        return super().get_permissions()
