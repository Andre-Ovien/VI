from django.urls import path
from . import views


urlpatterns = [
    path('api/user/register',views.RegisterUserView.as_view(), name="register")
]