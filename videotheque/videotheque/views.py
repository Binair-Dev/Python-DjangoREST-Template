from django.http import HttpResponse

# Create your views here.
def index_view(request):
    return HttpResponse("Bienvenue sur ma vidéotheque")