from django.urls import path

from base.common.constant.view_action import BaseViewAction
from staff.menu.views.viewset import MenuViewSet

urlpatterns = [
    path("create", MenuViewSet.as_view({"post": BaseViewAction.CREATE})),
    path("list", MenuViewSet.as_view({"get": BaseViewAction.LIST})),
    path("<int:pk>/detail", MenuViewSet.as_view({"get": BaseViewAction.RETRIEVE})),
    path("<int:pk>/delete", MenuViewSet.as_view({"delete": BaseViewAction.DESTROY})),
    path("<int:pk>/update", MenuViewSet.as_view({"put": BaseViewAction.UPDATE})),
]
