from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from config import settings
from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, AuthView, generate_new_password, UserPasswordResetView, \
    ConfirmEmailView

app_name = UsersConfig.name

urlpatterns = [
    path('', AuthView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('genpassword/', generate_new_password, name='generate_new_password'),
    path('password_reset/', UserPasswordResetView.as_view(), name='password_reset'),
    path('registration_successful/<str:uuid>', ConfirmEmailView.as_view(), name='registration_successful'),
]
