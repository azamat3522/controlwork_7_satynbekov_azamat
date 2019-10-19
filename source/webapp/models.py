from django.db import models


class Poll(models.Model):
    question = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_archived = None

    def __str__(self):
        return self.question


class Choice(models.Model):
    text = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Текст варианта')
    poll = models.ForeignKey('webapp.Poll', related_name='choice', on_delete=models.CASCADE, verbose_name='опрос')

    def __str__(self):
        return self.text

