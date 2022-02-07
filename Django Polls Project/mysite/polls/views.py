from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World. You're at polls index.")

def details(request, question_id):
    return HttpResponse(f"You're looking at question: {question_id}")

def results(request, question_id):
    return HttpResponse(f"These are the results of question {question_id}")

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")


