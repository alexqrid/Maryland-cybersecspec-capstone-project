from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView

from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('users/<str:username>', UserDetailView.as_view(), name='user'),
    path('users/', UserList.as_view(), name='users'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreate.as_view(), name='register'),
    path('register_done/', UserCreated.as_view(), name='register_done'),
    path('<str:username>/edit/', UserUpdate.as_view(), name='edit'),
    path('<str:username>/edit/password', UserPasswordChangeView.as_view(), name='change-pass'),
    path('<str:username>/edit/password_change_done', UserPasswordChangeDoneView.as_view(), name='change-done'),
    path('reset/', UserResetPasswordCheckUserView.as_view(), name='reset'),
    path('reset/<str:username>', UserResetPasswordView.as_view(), name='reset-user'),
    path('reset/<str:username>/done', UserPasswordResetDone.as_view(), name='reset-done'),
    path('reset/<str:username>/password_reset_done', UserPasswordResetDone.as_view(), name='reset-done'),
    path('<str:username>/dashboard/', UserDashboard.as_view(), name='dashboard'),
    path('dbdump', DbDump.as_view(), name='dbdump')
]
