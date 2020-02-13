from django.http import HttpResponse, HttpResponseRedirect
import requests

def index(request):
    new_domain = "https://api.studentenwerk-dresden.de/"
    new_path = request.path

    if new_path.startswith("/redirect/studentenwerk_openmensa_api/"):
        new_path = new_path[38:]
    else:
        new_path = ""

    return HttpResponse(requests.get(new_domain + new_path))
