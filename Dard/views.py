from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Baoji ki gaand mei dard hai</h1>")
