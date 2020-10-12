from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, ListView

from .forms import MessageCreationForm
from .models import Message


class NewMessageView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageCreationForm
    template_name = 'user/create_message.html'

    def get_success_url(self):
        return reverse('sent-list', kwargs={'username': self.request.user.username})

    def get_initial(self):
        initial = super(NewMessageView, self).get_initial()
        initial['sender'] = self.request.user
        return initial

    def form_valid(self, form):
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = self.request.user
        return super(NewMessageView, self).form_valid(form)


class SentDashboard(LoginRequiredMixin, ListView):
    model = Message
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'user/sent_messages.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Message.objects.filter(sender=self.request.user).select_related('recipient')\
                .order_by('recipient_id').distinct('recipient')
        else:
            return Message.objects.none()


class SentView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'user/message.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Message.objects.filter(sender=self.request.user, recipient__username=self.kwargs['to'])
        else:
            return Message.objects.none()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SentView, self).get_context_data(object_list=object_list, **kwargs)
        context['sent'] = True
        context['received'] = False
        context['recipient'] = self.kwargs['to']
        return context


class ReceivedDashboard(LoginRequiredMixin, ListView):
    model = Message
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'user/received_messages.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Message.objects.filter(recipient=self.request.user).select_related('sender')\
                .order_by('sender_id').distinct('sender')
        else:
            return Message.objects.none()


class ReceivedView(LoginRequiredMixin, ListView):
    model = Message
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'user/message.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Message.objects.filter(recipient=self.request.user, sender__username=self.kwargs['from'])
        else:
            return Message.objects.none()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ReceivedView, self).get_context_data(object_list=object_list, **kwargs)
        context['sent'] = False
        context['received'] = True
        context['sender'] = self.kwargs['from']
        return context
