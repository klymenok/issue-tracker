from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
from user.models import User


class UserListView(LoginRequiredMixin, ListView):
    login_url = 'login'
    queryset = User.objects.exclude(is_superuser=True)


@csrf_exempt
def login_view(request):
    if request.method == 'GET':
        return render(request, 'user/user_login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse('user-list'))
        else:
            return HttpResponse('Invalid credentials', status=400)
    else:
        return HttpResponse(status=405)
