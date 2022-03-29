from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
# from django.template import loader second variant
from django.shortcuts import get_object_or_404, render
# from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

'''
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
def results(request, question_id):
    # response = "You're looking at the results of question %s." first variant
    # return HttpResponse(response % question_id) first variant
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id) first variant
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html') second variant
    context = {'latest_question_list': latest_question_list}
    # output = ', '.join([q.question_text for q in latest_question_list]) first variant
    # return HttpResponse(template.render(context, request)) second variant
    return render(request, 'polls/index.html', context)   # a shortcut render()

def detail(request, question_id):
    # try:
        # question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
        # raise Http404("Question does not exist")  raising a 404 error
    question = get_object_or_404(Question, pk=question_id)  # a shortcut get_object_or_404
    return render(request, 'polls/detail.html', {'question': question})
'''

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        # """Return the last five published questions."""
        # return Question.objects.order_by('-pub_date')[:5] first variant
        """
            Return the last five published questions (not including those set to be
            published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id) first variant
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
