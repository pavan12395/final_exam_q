from django.db import models
from django import forms

# Create your models here.
class QuestionModel(models.Model):
    text=models.CharField(max_length=20)
    timestamp=models.DateField()
    class Meta:
        ordering=('text',)

class AnswerModel(models.Model):
    q_text=models.CharField(max_length=20)
    choice_text=models.CharField(max_length=20,choices=(('difficult','difficult'),('easy','easy')))
    votes=models.IntegerField()
    class Meta:
        ordering=('votes',)

class AnswerModelForm(forms.ModelForm):
    class Meta:
        model=AnswerModel
        exclude=('q_text','votes',)