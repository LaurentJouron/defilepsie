from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome on Défilepsie. Website in progress.")
