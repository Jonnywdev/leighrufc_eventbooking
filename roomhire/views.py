from django.shortcuts import redirect, render, HttpResponse

# Create your views here.


def index(request):
    """ A view to return index page """
    return render(request, 'roomhire/index.html')


def book(request):
    """ A view to retur the booking form page"""
    return render(request, 'roomhire/book.html')


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
