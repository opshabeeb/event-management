from django.shortcuts import render,redirect
from .models import Event
from .forms import Bookingform
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def booking(request):
    form=Bookingform()
    if request.POST:
        form=Bookingform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    dict_form={
        'form':form
    }
    return render(request,'booking.html',dict_form)

def contact(request):
    return render(request,'contact.html')
def event(request):
    eve=Event.objects.all()
    context={
        'eve':eve
    }
    return render(request,'event.html',context)