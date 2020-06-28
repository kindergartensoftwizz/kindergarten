from django.shortcuts import render,redirect
from kidsapp.models import contact, registration, subscribe, facility, event
from kidsapp.forms import contactform ,registrationform, subscribeform
from django.contrib.auth.models import User
from django.views.generic import TemplateView, ListView

'''from django.shortcuts import render,redirect
from kidsapp.models import kinder  
from kidsapp.forms import kinderform  ok wa
from django.contrib.auth.models import User
from django.views.generic import TemplateView'''

# Create your views here.

class kindergartenview(TemplateView):
	template_name="kindergarten.html"
class aboutview(TemplateView):
	template_name="about.html"
class galleryview(TemplateView):
	template_name="gallery.html"
class eventsview(ListView):
    template_name="events.html"
    def get_queryset(self):
        return event.objects.all()
class servicesview(TemplateView):
	template_name="services.html"
class contactpageview(TemplateView):
	template_name="contact.html"
class registrationview(TemplateView):
	template_name="registration.html"
class programsview(TemplateView):
	template_name="programs.html"
class facilitiesview(ListView):
    template_name="facilities.html" 
    def get_queryset(self):
        return facility.objects.all()
	
def insert1(request):
	if request.method=='POST':
		form=contactform(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/contact/')
			except:
				pass
				
				
	else:
		form=contactform()
		
	return render(request,'contact.html',{'form':form})
	
def insert2(request):
	if request.method=='POST':
		form=registrationform(request.POST, request.FILES)
		if form.is_valid():
			try:
				form.save()
				return redirect('/paytm/')
			except:
				pass
				
				
	else:
		form=registrationform()
		
	return render(request,'registration.html',{'form':form})
    
def insertsubscribe(request):
	if request.method=='POST':
		form=subscribeform(request.POST)
		if form.is_valid():
			try:
				form.save()
				return redirect('/kindergarten/')
			except:
				pass
				
				
	else:
		form=subscribeform()
		
	return render(request,'base.html',{'form':form})    
	

	

		

	
