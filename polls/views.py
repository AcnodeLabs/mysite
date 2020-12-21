from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template import loader

from .models import Question

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/wp/index.html')
	context = {
		'latest_question_list': latest_question_list,
	}
	return HttpResponse(template.render(context, request))

def detail(request, question_id):
	return HttpResponse("You are looking at question %s" % question_id)

def results(request, question_id):
	return HttpResponse("Results of Question %s." % question_id)

def vote(request, question_id):
	return HttpResponse("You are voting for Question %s" % question_id)


