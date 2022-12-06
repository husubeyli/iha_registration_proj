from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
import json
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


from accounts.forms import UserRegistrationForm


def sign_in(request):
    logout(request)
    resp = {"status": 'failed', 'msg': ''}
    username = ''
    password = ''

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                resp['status'] = 'success'
            else:
                resp['msg'] = "Incorrect username or password"
        else:
            resp['msg'] = "Incorrect username or password"
    return HttpResponse(json.dumps(resp), content_type='application/json')


# Logout
def logout_user(request):
    logout(request)
    return redirect('/')


# def sign_up(request):
#     user = request.user
#     context = {}
#     if user.is_authenticated:
#         return redirect('home-page')
#     context['page_title'] = "Register User"
#     if request.method=='POST':
#         data = request.POST
#         form = UserRegistrationForm(data)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             loginUser = authenticate(username= username, password = pwd)
#             login(request, loginUser)
#             return redirect('home-page')
#         else:
#             context['reg_form'] = form
#     return render(request, 'accounts/register.html', context)

# def sign_up(response):
#     if response.method == "POST":
#         form = UserRegistrationForm(response.POST)
#         print('formdayi')
#         if form.is_valid():
#             print('form valid oldu')
#             form.save()

#         return redirect("/accounts/register")
#     else:
#         form = UserRegistrationForm()

#     return render(response, "accounts/register.html", {"form": form})


class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')
    form_class = UserRegistrationForm
    success_message = "Your profile was created successfully"