from django.urls import path

from base.common.constant.view_action import BaseViewAction
from staff.order_item.views.viewset import OrderItemViewSet

urlpatterns = [
    path("create", OrderItemViewSet.as_view({"post": BaseViewAction.CREATE})),
    path("list", OrderItemViewSet.as_view({"get": BaseViewAction.LIST})),
    path("<int:pk>/detail", OrderItemViewSet.as_view({"get": BaseViewAction.RETRIEVE})),
    path("<int:pk>/delete", OrderItemViewSet.as_view({"delete": BaseViewAction.DESTROY})),
    path("<int:pk>/update", OrderItemViewSet.as_view({"put": BaseViewAction.UPDATE})),
]
