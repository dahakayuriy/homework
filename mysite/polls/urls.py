from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path("child/", views.return_simple_html, name="child"),
    path("signup/", views.SignUpView.as_view(), name="signup"),

    path("", views.index, name="index"),
]
