from django.shortcuts import redirect, render
from .models import RequestForm
from .forms import EventRequest

# Create your views here.


def index(request):
    """ A view to return index page """
    return render(request, 'roomhire/index.html')


def upload(request):
    if request.POST:
        form = EventRequest(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    return render(request, 'roomhire/book.html', {'form': EventRequest})
