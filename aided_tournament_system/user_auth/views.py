from allauth.account.views import EmailView, LoginView, LogoutView, SignupView
from competition.choices import CompetitionTypeChoices
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView
from participant.models import Player, Referee
from participant.services.get_ratings import get_rating_for_player
from user_auth.forms import UserUpdateForm
from user_auth.models import User


class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'account/update.html'
    success_url = reverse_lazy('user_detail')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs['user'] = User.objects.get(id=self.request.user.id)
        return super().get_context_data(**kwargs)


class UserInfoView(TemplateView):
    template_name = 'account/detail.html'

    def get_context_data(self, **kwargs):
        kwargs['user'] = User.objects.get(id=self.request.user.id)
        try:
            kwargs['player'] = Player.objects.get(
                user_id=self.request.user.id
            )
            kwargs['beach_rating'] = get_rating_for_player(
                kwargs['player'],
                CompetitionTypeChoices.BEACH_VOLLEY.value)
            kwargs['park_rating'] = get_rating_for_player(
                kwargs['player'],
                CompetitionTypeChoices.PARK_VOLLEY.value)
        except Player.DoesNotExist:
            pass
        try:
            kwargs['referee'] = Referee.objects.get(
                user_id=self.request.user.id
            )
        except Referee.DoesNotExist:
            pass
        return super().get_context_data(**kwargs)


class UserLoginView(LoginView):
    template_name = 'account/login.html'
    success_url = 'user_detail'


class UserLogoutView(LogoutView):
    template_name = 'account/logout.html'
    success_url = '/user/detail/'


class UserRegisterView(SignupView):
    template_name = 'account/signup.html'
    success_url = '/user/detail/'


class UserChangeEmailView(EmailView):
    template_name = 'account/email.html'
    success_url = '/user/detail/'
