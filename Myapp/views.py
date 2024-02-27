from urllib import request

from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def appointment(request):
    return render(request, 'appointment.html')
def contact(request):
    return render(request, 'contact.html')
def facility(request):
    return render(request, 'facility.html')
def classes(request):
    return render(request, 'classes.html')
def team(request):
    return render(request, 'team.html')
def testimonial(request):
    return render(request, 'testimonial.html')
def call_to_action(request):
    return render(request, 'call-to-action.html')
def error(request):
    return render(request, '404.html')

# Create your views here.
