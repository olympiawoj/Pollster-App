from django.shortcuts import render

# Create your views here.
from .models import Question, Choice


#Get questions and display them
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)



#Show specific questions and choices
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    #If question id doesn't exist, raise an http 404
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    #pass in question as a dict and load details
    return render(request, 'polls/results.html', {'question': question})

#Get questions and display results
def results(result, question_id):
    #looks in db for what we're asking for, if not return 404
    question = get_object_or_404(Question, pk=question_id)
    #template is polls/results.html, pass in question data
    return render(request, 'polls/results.html', {'question': question})