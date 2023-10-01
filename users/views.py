from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect, reverse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from config import settings
from users.forms import UserRegisterForm, UserProfileForm, UserPasswordForm
from django.views.generic import CreateView, UpdateView, TemplateView, View
from users.models import User
from users.token import email_verification_token
from django.core.mail import send_mail


class RegisterView(CreateView):
    """Регистрация пользователя"""
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:register_need_verify')

    def form_valid(self, form):
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            current_site = get_current_site(self.request)
            subject = "Активация аккаунта"
            body = render_to_string(
                'users/email_verification.html',
                {'domain': current_site,
                 'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                 'token': email_verification_token.make_token(user),
                 }
            )
            send_mail(
                subject=subject,
                html_message=body,
                message=user.email,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email]
            )
        return super().form_valid(form)


class RegistrationEmailSentView(TemplateView):
    """Смс о необходимости активации аккаунта"""
    template_name = 'users/email_registration_sent.html'


class ProfileView(UpdateView):
    """Редактирование профиля"""
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class ActivateView(View):
    """Активация аккаунта через почту"""
    @staticmethod
    def get_user_from_email_verification_token(uidb64, token: str):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = get_user_model().objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
            return None
        if user is not None and email_verification_token.check_token(user, token):
            return user
        else:
            return None

    def get(self, request, uidb64, token):
        user = self.get_user_from_email_verification_token(uidb64, token)
        if user is not None:
            user.is_active = True
            user.save()
            return redirect(reverse('users:verification_success'))
        return redirect(reverse('users:register'))


class VerificationSuccessView(TemplateView):
    """Верификация подтверждена"""
    template_name = 'users/email_verification_success.html'


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    """Отправка сгенерированного пароля на почту"""
    form_class = UserPasswordForm

    def form_valid(self, form):
        user = form.save()
        new_password = User.objects.make_random_password(12)
        user.set_password(new_password)
        user.save()
        send_mail(
            subject="Новый пароль",
            message=f'Ваш новый пароль: {new_password}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        return super().form_valid(form)
