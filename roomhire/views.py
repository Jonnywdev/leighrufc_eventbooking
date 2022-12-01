from django.shortcuts import redirect, render, HttpResponse, get_object_or_404

from django.http import HttpResponseRedirect
from .forms import RoomHireForm
from .models import RoomHire

# Create your views here.


def index(request):
    """ A view to return index page """
    return render(request, 'roomhire/index.html')


def book(request):
    """ A view to retur the booking form page"""
    submitted = False
    if request.method == 'POST':
        form = RoomHireForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'roomhire/success.html')

    else:
        form = RoomHireForm
        if submitted in request.GET:
            submitted = True

    context = {
        'form': form,
        'submitted': submitted,
        }

    return render(request, 'roomhire/book.html', context)


def success(request):
    if request.method == "POST":
        full_name = request.POST['full_name']
        email_address = request.POST['email_address']
        phone_number = request.POST['phone_number']
        event_type = request.POST['event_type']
        date_of_event = request.POST['date_of_event']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        num_people = request.POST['num_people']
        other_details = request.POST['other_details']

        return render(request, 'roomhire/success.html', {
            'full_name': full_name,
            'email_address': email_address,
            'phone_number': phone_number,
            'event_type': event_type,
            'date_of_event': date_of_event,
            'start_time': start_time,
            'end_time': end_time,
            'num_people': num_people,
            'other_details': other_details,
         })

    else:
        return render(request, 'roomhire/index.html')


def all_events(request):
    queryset = RoomHire.objects.order_by("-created_on")

    # paginate_by = 6
    event_list = RoomHire.objects.all()
    return render(request, 'roomhire/events.html', {'event_list': event_list})


def dashboard(request):
    return render(request, 'roomhire/dashboard.html', {})


def confirm_e(request):
    return render(request, 'roomhire/confirmed_events.html', {})


def calendar(request):
    return render(request, 'roomhire/calendar.html', {})


def upcomingevents(request):
    return render(request, 'roomhire/ourupcomingevents.html', {})


def info(request):
    return render(request, 'roomhire/info.html', {})


def clubinfo(request):
    return render(request, 'roomhire/club-info.html', {})


def balloons(request):
    return render(request, 'roomhire/balloon.html', {})


def lbd(request):
    return render(request, 'roomhire/food.html', {})


def manageusers(request):
    return render(request, 'roomhire/manage-users.html', {})


def goadmin(request):
    return render(request, 'roomhire/admin.py', {})


def update_booking(request, roomhire_id):

    roomhire = RoomHire.objects.get(pk=roomhire_id)

    context = {
        'roomhire': 'roomhire',
    }

    return render(request, 'roomhire/update_details.html', context)
