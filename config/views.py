from django.http import JsonResponse, HttpResponse

def index(request):
    return HttpResponse("<h1>Django Main Page</h1>")

def hello(request):
    return JsonResponse({
        "message": "Hello Django!",
        "success": True
    })