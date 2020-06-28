from django.db import models

#create your models here.

class contact(models.Model):
	name=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	phone=models.CharField(max_length=200)
	subject=models.CharField(max_length=200)
	message=models.CharField(max_length=200,default="")
	
	
	class Meta:
		db_table="contact"
	def __str__(self):
		return self.name
class registration(models.Model):
	firstname=models.CharField(max_length=200)
	lastname=models.CharField(max_length=200)
	email=models.CharField(max_length=200)
	address=models.CharField(max_length=200)
	course=models.CharField(max_length=200)
	gender=models.CharField(max_length=200)
	dob=models.CharField(max_length=200)
	mobile=models.CharField(max_length=200,default="")
	pic = models.ImageField(upload_to = 'images/',default="")	
	
	
	class Meta:
		db_table="registration"
	def __str__(self):
		return self.name
		
		

class subscribe(models.Model):
	email=models.CharField(max_length=200)
	
	
	class Meta:
		db_table="subscribe"
	def __str__(self):
		return self.email
        

class facility(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=1000)
    pic = models.ImageField(upload_to = 'images/')	
    class Meta:
        db_table="facility"
    def __str__(self):
        return self.title        
        
        
class event(models.Model):
    title=models.CharField(max_length=200)
    edate=models.CharField(max_length=200)
    etime=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    pic = models.ImageField(upload_to = 'images/')	
    class Meta:
        db_table="event"
    def __str__(self):
        return self.title                