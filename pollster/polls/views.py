
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

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
    return render(request, 'polls/detail.html', {'question': question})

#Get questions and display results
def results(request, question_id):
    #looks in db for what we're asking for, if not return 404
    question = get_object_or_404(Question, pk=question_id)
    #template is polls/results.html, pass in question data
    return render(request, 'polls/results.html', {'question': question})


#Vote for a question choice
def vote(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))