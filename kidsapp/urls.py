from django.urls import path, include
from kidsapp import views


urlpatterns = [
	path('kindergarten/',views.kindergartenview.as_view()),
	path('about/',views.aboutview.as_view()),
	path('gallery/',views.galleryview.as_view()),
	path('events/',views.eventsview.as_view()),
	path('services/',views.servicesview.as_view()),
	path('contact/',views.contactpageview.as_view()),
	path('insert1',views.insert1),
	path('registration/',views.registrationview.as_view()),
	path('insert2',views.insert2),
	path('programs/',views.programsview.as_view()),
    path('insertsubscribe',views.insertsubscribe),
    path('facilities/',views.facilitiesview.as_view()),
]
