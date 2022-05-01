from django.shortcuts import render
from votes.models import AnswerModelForm, QuestionModel,AnswerModel
# Create your views here.
def home(request,id):
    question=QuestionModel.objects.all()[id-1]
    return render(request,'home.html',{'form':AnswerModelForm(),'question':question.text,'qid':id})

def result(req,id):
    if req.method=='POST':
        question=QuestionModel.objects.all()[id-1]
        form=AnswerModelForm(req.POST)
        answer=form.save(commit=False)
        answer.q_text=question.text
        answer.votes=1
        answer.save()
        Answers=AnswerModel.objects.all()
        easy_votes=0
        difficult_votes=0
        for ans in Answers:
            if ans.q_text==question.text:
                if ans.choice_text=='easy':
                    easy_votes+=1
                else:
                    difficult_votes+=1
        return render(req,'result.html',{'question':question.text,'easy':easy_votes,'difficult':difficult_votes,'qid':id})