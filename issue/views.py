from django.urls import reverse_lazy
from django.shortcuts import render, reverse
from django.views.generic import ListView, CreateView
from issue.models import Issue
from issue.forms import IssueForm

class IssueListView(ListView):
    model = Issue


class IssueCreateView(CreateView):
    model = Issue
    form_class = IssueForm
    success_url = reverse_lazy('issue-list')


