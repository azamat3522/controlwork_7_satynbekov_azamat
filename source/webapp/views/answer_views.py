from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View

from webapp.models import Answer, Poll


class AnswerIndexView(View):


    def get(self, request, *args, **kwargs):
        pass

    def post(self):
        pass
