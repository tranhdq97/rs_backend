from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from base.auth.permissions.permission import IsSuperStaff, IsManager
from base.common.constant.view_action import BaseViewAction
from base.common.custom.pagination import CustomPagination
from base.common.utils.exceptions import PermissionDenied
from base.table.models import Table
from staff.table.filters.table import TableListQueryFields
from staff.table.serializers.table import TableListSlz, TableRetrieveSlz, TableCreateSlz, TableUpdateSlz


class TableViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin, GenericViewSet):
    permission_classes = (AllowAny,)
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    serializer_class = TableListSlz
    queryset = Table.objects.all()
    search_fields = TableListQueryFields.SEARCH_FIELDS
    ordering_fields = TableListQueryFields.ORDER_FIELDS
    ordering = TableListQueryFields.ORDER_DEFAULT_FIELD
    filterset_fields = TableListQueryFields.FILTERSET_FIELDS

    def get_serializer_class(self):
        slz_switcher = {
            BaseViewAction.LIST: TableListSlz,
            BaseViewAction.RETRIEVE: TableRetrieveSlz,
            BaseViewAction.CREATE: TableCreateSlz,
            BaseViewAction.UPDATE: TableUpdateSlz,
        }
        slz = slz_switcher.get(self.action, self.serializer_class)
        return slz

    def get_permissions(self):
        perm_switcher = {
            BaseViewAction.LIST: (AllowAny,),
            BaseViewAction.RETRIEVE: (AllowAny,),
            BaseViewAction.CREATE: (IsManager | IsSuperStaff,),
            BaseViewAction.UPDATE: (IsManager | IsSuperStaff,),
            BaseViewAction.DESTROY: (IsSuperStaff,),
        }
        self.permission_classes = perm_switcher.get(self.action, self.permission_classes)
        if self.permission_classes is None:
            raise PermissionDenied()

        return super().get_permissions()
