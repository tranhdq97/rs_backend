from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from base.auth.permissions.permission import IsManager, IsSuperStaff
from base.common.constant.view_action import BaseViewAction
from base.common.utils.exceptions import PermissionDenied
from base.file_management.models import FileManagement
from base.file_management.serializers.file_management import (
    FileManagementCreateSlz,
    FileManagementListSlz,
    FileManagementRetrieveSlz,
    FileManagementUpdateSlz,
)
from storage.file_management.filters.file_management import FileManagementListQueryFields


class FileManagementViewSet(
    CreateModelMixin, RetrieveModelMixin, ListModelMixin, DestroyModelMixin, UpdateModelMixin, GenericViewSet
):
    serializer_class = FileManagementCreateSlz
    parser_classes = (
        MultiPartParser,
        FormParser,
    )
    queryset = FileManagement.objects.all()
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    search_fields = FileManagementListQueryFields.SEARCH_FIELDS
    ordering_fields = FileManagementListQueryFields.ORDER_FIELDS
    ordering = FileManagementListQueryFields.ORDER_DEFAULT_FIELD
    filterset_fields = FileManagementListQueryFields.FILTERSET_FIELDS

    def get_serializer_class(self):
        slz_switcher = {
            BaseViewAction.CREATE: FileManagementCreateSlz,
            BaseViewAction.LIST: FileManagementListSlz,
            BaseViewAction.RETRIEVE: FileManagementRetrieveSlz,
            BaseViewAction.UPDATE: FileManagementUpdateSlz,
        }
        return slz_switcher.get(self.action, self.serializer_class)

    def get_permissions(self):
        perm_switcher = {
            BaseViewAction.LIST: (IsSuperStaff | IsManager,),
            BaseViewAction.RETRIEVE: (AllowAny,),
            BaseViewAction.CREATE: (IsAuthenticated,),
            BaseViewAction.UPDATE: (IsAuthenticated,),
            BaseViewAction.DESTROY: (IsAuthenticated,),
        }
        self.permission_classes = perm_switcher.get(self.action, self.permission_classes)
        if self.permission_classes is None:
            raise PermissionDenied()

        return super().get_permissions()
