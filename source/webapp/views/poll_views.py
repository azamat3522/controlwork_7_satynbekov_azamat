from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PollForm
from webapp.models import Poll


class PollIndexView(ListView):
    context_object_name = 'polls'
    model = Poll
    template_name = 'poll/poll_index.html'
    ordering = ['-created_at']
    paginate_by = 5
    paginate_orphans = 1


class PollView(DetailView):
    template_name = 'poll/poll.html'
    model = Poll
    context_object_name = 'poll'


class PollCreateView(CreateView):
    model = Poll
    template_name = 'poll/poll_create.html'
    form_class = PollForm

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollUpdateView(UpdateView):
    model = Poll
    template_name = 'poll/poll_update.html'
    context_object_name = 'poll'
    form_class = PollForm

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollDeleteView(DeleteView):
    model = Poll
    template_name = 'poll/poll_delete.html'
    context_object_name = 'poll'
    success_url = reverse_lazy('index')
