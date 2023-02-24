from django.urls import path

from base.common.constant.view_action import BaseViewAction
from staff.customer.views.viewset import CustomerViewSet

urlpatterns = [
    path("list", CustomerViewSet.as_view({"get": BaseViewAction.LIST})),
    path("create", CustomerViewSet.as_view({"post": BaseViewAction.CREATE})),
    path("<int:pk>/detail", CustomerViewSet.as_view({"get": BaseViewAction.RETRIEVE})),
    path("<int:pk>/delete", CustomerViewSet.as_view({"delete": BaseViewAction.DESTROY})),
    path("<int:pk>/update", CustomerViewSet.as_view({"put": BaseViewAction.UPDATE})),
]
