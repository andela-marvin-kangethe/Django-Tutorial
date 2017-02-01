from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Question
# Create your views here.


def index(request):
	latest_question_list = Question.objects.all()
	context = {'latest_question_list':latest_question_list}
	return render(request, 'polls/index.html', context)

def details(request, question_id):
	try:
		current_question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404('Requested object does not exist.')
	context={"current_question":current_question}	
	return render(request, 'polls/details.html', context)	

def results(request, question_id):
	return HttpResponse('Results id number {}'.format(question_id))	

def vote(request, question_id):
	return HttpResponse('Vote id number {}'.format(question_id))