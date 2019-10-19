from django.http import Http404
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import ChoiceForm, PollChoiceForm
from webapp.models import Choice, Poll


class ChoiceForPollCreateView(CreateView):
    template_name = 'choice/choice_create.html'
    form_class = PollChoiceForm
    model = Choice

    def form_valid(self, form):
        poll_pk = self.kwargs.get('pk')
        poll = get_object_or_404(Poll, pk=poll_pk)
        poll.choice.create(**form.cleaned_data)
        return redirect('poll_view', pk=poll_pk)


class ChoiceUpdateView(UpdateView):
    model = Choice
    template_name = 'choice/choice_update.html'
    context_object_name = 'choice'
    form_class = ChoiceForm

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})


class ChoiceDeleteView(DeleteView):
    model = Choice
    template_name = 'choice/choice_delete.html'
    context_object_name = 'choice'
    success_url = reverse_lazy('index')
