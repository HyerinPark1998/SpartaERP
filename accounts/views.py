from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .form import SignupForm
from .models import UserModel
from django.contrib.auth.decorators import login_required


# Create your views here.
def sign_up(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'accounts/signup.html')
    elif request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')  # 수정한 부분

            UserModel.objects.create_user(username=username, password=password)
            return redirect('/log-in')
        else:
            return HttpResponse('회원 가입 실패! 바르게 입력해 주세요. \n뒤로 가기 버튼을 이용해주세요.')

def log_in(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'accounts/login.html')
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/inventory')
        else:
            return redirect('/log-in')

@login_required
def log_out(request):
    logout(request)
    return redirect('/')
