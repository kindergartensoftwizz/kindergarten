from django import forms
from kidsapp.models import contact,registration, subscribe
'''from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm'''
#create your models here.


class contactform(forms.ModelForm):
	name=forms.CharField(max_length=200)
	email=forms.CharField(max_length=200)
	phone=forms.CharField(max_length=200)
	subject=forms.CharField(max_length=200)
	message=forms.CharField(max_length=200)
	
	
	class Meta:
		model=contact
		fields="__all__"
		
class registrationform(forms.ModelForm):
	firstname=forms.CharField(max_length=200)
	lastname=forms.CharField(max_length=200)
	email=forms.CharField(max_length=200)
	address=forms.CharField(max_length=200)
	course=forms.CharField(max_length=200)
	gender=forms.CharField(max_length=200)
	dob=forms.CharField(max_length=200)
	mobile=forms.CharField(max_length=200)
	pic = forms.ImageField()
	
	
	class Meta:
		model=registration
		fields= "__all__"

	
		
		

class subscribeform(forms.ModelForm):
    email=forms.CharField(max_length=200)
	
    class Meta:
        model=subscribe
        fields="__all__"
	