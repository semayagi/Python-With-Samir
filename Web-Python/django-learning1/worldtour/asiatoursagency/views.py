from django.shortcuts import render
from .models import Tour
# from django.http import HttpResponse

# Default: get
def index(request):
    tours = Tour.objects.all()
    context = {'tours': tours}
    return render(request, 'tours/index.html', context) # Now we have proper HTML page
    # return HttpResponse("Asia Tours Agency") - we aren't happy with this
