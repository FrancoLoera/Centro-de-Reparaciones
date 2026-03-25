from django.urls import path
from django.shortcuts import redirect
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from django.contrib.auth.views import LogoutView
from .views import login_redirect_view, dashboard_tecnico, dashboard_admin

urlpatterns = [
    path("redirect/", login_redirect_view, name="login_redirect"),
    path("", lambda request: redirect("login")),
    path(
        "logout/",
        LogoutView.as_view(next_page="login"),
        name="logout"
    ),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html",
            authentication_form=LoginForm,
            redirect_authenticated_user=True
        ),
        name="login"
    ),
    path("panel-tecnico/", dashboard_tecnico, name="dashboard_tecnico"),
    path("panel-admin/", dashboard_admin, name="dashboard_admin"),
]