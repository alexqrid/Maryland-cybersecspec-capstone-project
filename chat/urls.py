from django.urls import path
from .views import *

urlpatterns = [
    path('create/', NewMessageView.as_view(), name='create'),
    path('<str:username>/sent/', SentDashboard.as_view(), name='sent-list'),
    path('<str:username>/sent/<str:to>', SentView.as_view(), name='sent'),
    path('<str:username>/received/', ReceivedDashboard.as_view(), name='received-list'),
    path('<str:username>/received/<str:from>', ReceivedView.as_view(), name='received'),


]
