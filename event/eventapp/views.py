from django.shortcuts import get_object_or_404, render,redirect
from .models import Event
from .forms import Bookingform
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def index(request):
    eve=Event.objects.all()
    context={
        'eve':eve
    }
    return render(request,'index.html',context)

def about(request):
    cards_info = [
        {'no':'01', 'name': 'Certified Experience', 'description': 'Benefit from our certified expertise and extensive experience in delivering exceptional solutions tailored to your needs.'},
        {'no':'02', 'name': 'Great Suport', 'description': 'Experience exceptional support tailored to your needs, ensuring a seamless journey toward your goals'},
        {'no':'03', 'name': 'Competitive Price', 'description': 'Unlock unbeatable value with our competitive pricing, offering top-quality solutions at cost-effective rates'},
        {'no':'04', 'name': 'We Got The Tools ', 'description': 'Empowered with cutting-edge tools and technologies, we re equipped to tackle any challenge with precision and efficiency'},
        {'no':'05', 'name': 'Success Guarantee', 'description': 'Rest assured with our success guarantee, providing assurance that we''ll go above and beyond to ensure your objectives are achieved.'},
        {'no':'06', 'name': 'Experienced Team', 'description': 'Rely on our seasoned team of professionals, whose wealth of experience ensures top-tier solutions tailored to your needs'},
        
       
    ]
    context={
        'cards_info':cards_info
    }
    return render(request,'about.html',context)

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
    card=[
        {'no':'01', 'name': 'Initial Inquiry', 'description': 'Within the ''Initial Inquiry'' phase of our event management process, we engage with prospective clients or partners, gathering crucial event details and objectives'},
        {'no':'02', 'name': 'Pre-Production', 'description': 'Pre-production involves meticulous planning and coordination to ensure a seamless event. It includes tasks like venue selection, vendor sourcing, and timeline development'},
        {'no':'03', 'name': 'Walktrough', 'description': 'The walkthrough stage entails a detailed inspection of the event venue to identify logistical considerations and optimize event flow for seamless execution.'},
        {'no':'04', 'name': 'Quote', 'description': 'The quote stage involves providing clients with a detailed breakdown of costs and services tailored to their event requirements.'},
        {'no':'05', 'name': 'Production', 'description': 'Rest assured with our success guarantee, providing assurance that we''ll go above and beyond to ensure your objectives are achieved.'},
        {'no':'06', 'name': 'Production', 'description': 'Rely on our seasoned team of professionals, whose wealth of experience ensures top-tier solutions tailored to your needs'},
        
    ]
    context={
        'eve':eve,
        'card':card
    }
    return render(request,'event.html',context)

@login_required(login_url="login")
def editevent(request,id):
    Data=Event.objects.get(id=id)
    return render(request,'editevent.html',{'Data':Data})

def formupdate(request,id):
    if request.method=='POST':
        add=Event.objects.get(id=id)
        add.image=request.FILES.get('image')
        add.name=request.POST['name']
        add.description=request.POST['description']
        add.save()
        return redirect('event')