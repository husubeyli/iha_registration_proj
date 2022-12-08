from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView



app_name = 'accounts'

urlpatterns = [
    path('login',auth_views.LoginView.as_view(template_name="accounts/login.html",redirect_authenticated_user = True),name='login'),
    path('login_ajax/', views.SignUp.as_view(), name='login_ajax'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.SignUpView.as_view(), name='register')
]