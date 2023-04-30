from django.urls import path
from user.views import UserListView

urlpatterns = [
    path('list', UserListView.as_view(), name='user-list')
]
