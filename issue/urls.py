from django.urls import path
from issue.views import IssueListView, IssueCreateView

urlpatterns = [
    path('list', IssueListView.as_view(), name='issue-list'),
    path('create', IssueCreateView.as_view(), name='issue-create'),
]
