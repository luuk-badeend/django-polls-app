from django.shortcuts import render
from django.http import HttpResponse

from .models import Question


def index(request):
    return HttpResponse("Hello World!")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s" % question_id)


def results(request, question_id):
    response = "You're looking at the results."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on questions" % question_id)


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)
