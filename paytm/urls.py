from django.conf.urls import include, url
from paytm import views


urlpatterns = [
    
    url(r'^$', views.home, name='home'),
    url(r'^payment/', views.payment, name='payment'),
    url(r'^response/', views.response, name='response'),
]
