from django.contrib.auth.views import LoginView, PasswordResetView
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.utils.http import urlsafe_base64_decode
from django.views import View
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
        host = "http://127.0.0.1:8000"
        if form.is_valid():
            new_user = form.save()
            send_mail(
                subject='Завершение регистрации',
                message=f"Для завершения регистрации, пожалуйста перейдите по ссылке:"
                        f"\n{host}{reverse('users:registration_successful', kwargs={'uuid': new_user.uuid})}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[new_user.email, ]
            )

        return super().form_valid(form)


class ConfirmEmailView(View):

    # def get_user(uuid):
    #     try:
    #         uid = urlsafe_base64_decode(uuid).decode()
    #         user = User.objects.get(pk=uid)
    #     except (TypeError, ValueError, OverflowError):
    #         user = None
    #     return user

    def get(self, request, uuid):
        # user = self.get_user(uidb64)
        user = User.objects.get(uuid=uuid)
        # if user is not None and user.user_token == user_token:
        user.is_active = True
        user.is_staff = True
        user.save()
        user.is_active = True
        user.save()
        return render(request, 'users/registration_successful.html')


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
    success_url = reverse_lazy('users:login')
