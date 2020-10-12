from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.shortcuts import get_object_or_404, redirect

from django.urls import reverse

from .forms import UserCreationForm, UserUpdateForm, PasswordChangeForm, PasswordResetForm, CheckUserForm
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, FormView

from .models import User
from message.utils import dbdump


class IndexView(TemplateView):
    template_name = "user/index.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard', username=request.user.username)
        return super(IndexView, self).dispatch(request, *args, **kwargs)


class LoginView(LoginView):
    template_name = 'user/login.html'
    form_class = AuthenticationForm
    success_url = '/dashboard/'
    redirect_authenticated_user = True

    def get_success_url(self):
        return f"/{self.request.user.username}/dashboard"


class LogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'user/logout.html'


class UserCreate(CreateView):
    model = User
    template_name = 'user/register.html'
    form_class = UserCreationForm
    success_url = '/register_done/'


class UserCreated(TemplateView):
    template_name = 'user/register_done.html'


class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'user/edit.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_success_url(self):
        return reverse('user', kwargs={'username': self.object.username})

    def get_initial(self):
        initial = super(UserUpdate, self).get_initial()
        initial['username'] = self.object.username
        initial['first_name'] = self.object.first_name
        initial['last_name'] = self.object.last_name
        initial['secret_question'] = self.object.secret_question
        initial['secret_answer'] = ""

        return initial


class UserResetPasswordCheckUserView(FormView):
    form_class = CheckUserForm
    template_name = "user/check_user_before_reset_pass.html"

    def form_valid(self, form):
        username = form.cleaned_data['username']
        user = get_object_or_404(User, username=username)
        self.kwargs['user'] = user.username
        return super(UserResetPasswordCheckUserView, self).form_valid(form)

    def get_success_url(self):
        return reverse('reset-user', kwargs={'username': self.kwargs['user']})


class UserResetPasswordView(FormView):
    form_class = PasswordResetForm
    template_name = "user/password_reset.html"

    def get_form_kwargs(self):
        kwargs = super(UserResetPasswordView, self).get_form_kwargs()
        # update the kwargs for the form init method with yours
        self.kwargs['user'] = User.objects.get(username=self.kwargs['username'])
        kwargs.update(self.kwargs)  # self.kwargs contains all url conf params
        return kwargs

    def get_initial(self):
        initial = super(UserResetPasswordView, self).get_initial()
        user = get_object_or_404(User, username=self.kwargs['username'])
        initial['username'] = user.username
        initial['secret_question'] = user.get_secret_question_display()
        initial['secret_answer'] = ''
        return initial

    def get_success_url(self):
        return reverse('reset-done', kwargs={"username": self.kwargs['username']})

    def form_valid(self, form):
        """If the form is valid, redirect to the supplied URL."""
        self.kwargs['user'].set_password(form.cleaned_data['new_password1'])
        self.kwargs['user'].save()
        return super(UserResetPasswordView, self).form_valid(form)


class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangeForm
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'user/password_change.html'

    def get_success_url(self):
        return reverse('change-done', kwargs={'username': self.request.user.username})

    def get_context_data(self, **kwargs):
        context = super(UserPasswordChangeView, self).get_context_data(**kwargs)
        context.update({'user': self.request.user.username})
        return context


class UserPasswordChangeDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'user/password_change_done.html'


class UserPasswordResetDone(TemplateView):
    template_name = 'user/password_reset_done.html'


class UserDashboard(LoginRequiredMixin, TemplateView):
    template_name = 'user/dashboard.html'

    def get_context_data(self, **kwargs):
        return {'user': self.request.user.username}


class UserList(LoginRequiredMixin, ListView):
    template_name = 'user/user_list.html'
    model = User


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return User.objects.filter(username=self.request.user)
        else:
            return User.objects.none()

    def get_success_url(self):
        return reverse('user', kwargs={'user': self.object.username})


class DbDump(LoginRequiredMixin, TemplateView):
    template_name = 'user/dbdump.html'

    def get_context_data(self, **kwargs):
        context = super(DbDump, self).get_context_data(**kwargs)
        context['users'], context['messages'] = dbdump()
        return context
