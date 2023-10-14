from django.urls import path

from . import views

from django.contrib.auth.views import LogoutView   #LoginView,

from .forms import LoginForm
from .views import RegisterView#, LoginView

app_name = "users"

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),

    path('signin/', views.signin, name='signin'),

    path('logout/', views.logoutuser, name='logoutuser'),
]
