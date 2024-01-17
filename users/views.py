from django.contrib.auth.views import LoginView, PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from config import settings
from users.forms import UserRegisterForm, UserProfileForm, UserAuthForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        new_user = form.save()
        send_mail(
            subject='Поздравляем с успешной регистрацией!',
            message='Добро пожаловать на нашу платформу!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email, ]
        )

        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class AuthView(LoginView):
    model = User
    form_class = UserAuthForm
    success_url = reverse_lazy('')


def generate_new_password(request):
    new_password = User.objects.make_random_password()
    print(new_password)
    send_mail(
        subject='Вы поменяли пароль',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email],
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('users:login'))


class UserPasswordResetView(PasswordResetView):
    template_name = 'users/password_reset.html'
