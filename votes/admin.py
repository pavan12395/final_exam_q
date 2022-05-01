from django.contrib import admin
import site
from votes.models import QuestionModel,AnswerModel
# Register your models here.
class QuestionModelAdmin(admin.ModelAdmin):
    list_display=('text','timestamp')

class AnswerModelAdmin(admin.ModelAdmin):
    list_display=('q_text','choice_text','votes')


admin.site.register(QuestionModel,QuestionModelAdmin)
admin.site.register(AnswerModel,AnswerModelAdmin)