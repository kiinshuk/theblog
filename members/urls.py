from django.urls import path
# from . import views
from .views import UserRegisterView, UserEditView,EditProfilePageView ,PasswordsChangeView, ShowProfilePageView
from django.contrib.auth import views as auth_views


app_name = 'members'

urlpatterns = [
    # path('', views.home, name="home"),
    path('register/', UserRegisterView.as_view(), name="register"),
    path('edit_settings/', UserEditView.as_view(), name="edit_settings"),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html' )),
    path('password/',PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('profile/<int:pk>/', ShowProfilePageView.as_view(), name='show_profile'),
    path('edit_profile_page/<int:pk>/', EditProfilePageView.as_view(), name='edit_profile_page'),
]
