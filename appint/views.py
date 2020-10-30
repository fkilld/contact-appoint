from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Appointment
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            'Question from ' + name + ' Email: ' + email,
            message,
            email,
            ['somethingnew4200w@gmail.com']
        )
        return render(request, 'contact.html', {'name': name})
    else:
        # return the page
        return render(request, 'contact.html', {})


def appointment(request):
    if request.method == 'POST':
        namef = request.POST['namef']
        gender = request.POST['gender']
        mobile = request.POST['mobile']
        day = request.POST['day']
        month = request.POST['month']
        year = request.POST['year']
        address = request.POST['address']
        # address2 = request.POST['address2']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zipcode']
        # country = request.POST['country']
        email = request.POST['email']
        textarea = request.POST['textarea']

        appointment = Appointment(namef=namef, gender=gender, mobile=mobile, day=day, month=month, year=year,
                                  address=address,
                                  city=city, state=state,
                                  zipcode=zipcode,  email=email, textarea=textarea)

        appointment.save()
        # messages.success(request, 'your appointment has been submitted, we will get back to you shortly.')
        return render(request, 'appointment.html',{'namef': namef})
    else:
        # return the page
        return render(request, 'appointment.html', {})

# name
# "gender"
# "mobile"
# "day"
# "month"
# "year"
# "address"
# "address2"
# "city"
# "state"
# "zipcode"
# "country"
# "email"
# "textarea"
