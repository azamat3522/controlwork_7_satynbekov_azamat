from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

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