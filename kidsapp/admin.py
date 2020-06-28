from django.contrib import admin
from kidsapp.models import facility, subscribe, contact, registration, event
# Register your models here.

@admin.register(facility)
class facilityadmin(admin.ModelAdmin):
	pass
    
@admin.register(event)
class eventadmin(admin.ModelAdmin):
	pass    

@admin.register(subscribe)
class subscribeadmin(admin.ModelAdmin):
	list_display=('email',)
    
    
@admin.register(contact)
class contactadmin(admin.ModelAdmin):
	list_display=('name','email','phone','subject','message',)


@admin.register(registration)
class registrationadmin(admin.ModelAdmin):
	list_display=('firstname','lastname','email','address','course','gender','dob','mobile','pic',)
    