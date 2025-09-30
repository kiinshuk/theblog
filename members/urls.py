from django.urls import path
# from . import views
from .views import UserRegisterView

app_name = 'members'

urlpatterns = [
    # path('', views.home, name="home"),
    path('register/', UserRegisterView.as_view(), name="register"),
]
