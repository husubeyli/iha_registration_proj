import json
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic


from accounts.forms import UserRegistrationForm



class SignUp(generic.View):
    def post(self, request, *args, **kwargs):
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


class LogoutView(generic.View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)

# class LogoutView(generic.Log)

class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:login')
    form_class = UserRegistrationForm
    success_message = "Your profile was created successfully"
