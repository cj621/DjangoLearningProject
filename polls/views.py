# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
# from django.template import loader

from django.views import generic



# def index(request):
# 	latest_question_list = Question.objects.order_by('-pub_date')[:5] #order_by('-') indicate descending
# 	template = loader.get_template('polls/index.html')
# 	context = {
# 		'latest_question_list' : latest_question_list,
# 	}
# 	return render(request, 'polls/index.html', context)

# 	# output = ', '.join([q.question_text for q in latest_question_list])
# 	# return HttpResponse(output)

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		return Question.objects.order_by('-pub_date')

# -------------------------------------------------#

### Details of the each individual question
# def detail(request, question_id):
# 	# try:
# 	question = get_object_or_404(Question, pk=question_id)
# 	# except Question.DoesNotExist:
# 	# 	raise Http404("Question does not exist")
# 	return render(request, 'polls/detail.html', {'question': question})
    
#     # return HttpResponse("You're looking at question %s." % question_id)

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'


#--------------------------------------------------#

## Poll results for questions
# def results(request, question_id):
#     question = get_object_or_404(Question, pk = question_id)
#     return render(request, 'polls/results.html', {'question' : question})

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'


#--------------------------------------------------#

##method for voting
def vote(request, question_id):
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