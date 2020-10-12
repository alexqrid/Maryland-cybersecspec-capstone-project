from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm
from .models import User


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'secret_question', 'secret_answer']

    def clean(self):
        cleaned_data = self.cleaned_data
        if cleaned_data.get('password') != cleaned_data.get('password_again'):
            self.add_error('password', "You have repeated password incorrectly")


class UserUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['secret_answer'].required = False

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'secret_question', 'secret_answer']

    def clean(self):
        if not self.cleaned_data.get("secret_answer"):
            self.cleaned_data['secret_answer'] = self.instance.secret_answer
        return super(UserUpdateForm, self).clean()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class PasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User


class PasswordResetForm(SetPasswordForm):
    username = forms.CharField(disabled=True)
    secret_question = forms.CharField(disabled=True)
    # https://stackoverflow.com/a/7730719/10503874
    secret_answer = forms.CharField()

    def __init__(self, user=None, username=None, *args, **kwargs):
        # we explicit define the foo keyword argument, cause otherwise kwargs will
        # contain it and passes it on to the super class, who fails cause it's not
        # aware of a foo keyword argument.
        super(PasswordResetForm, self).__init__(user, *args, **kwargs)

    def is_valid(self):
        answer = self.data['secret_answer']
        if self.user.secret_answer != answer:
            self.add_error('secret_answer', "Secret answer is incorrect")
        return super(PasswordResetForm, self).is_valid()


class CheckUserForm(forms.Form):
    username = forms.CharField(label="Username")
