from django.urls import path
from Myapp import views

urlpatterns = [
    path('', views.home, name='my_index'),
    path('about/', views.about, name='about'),
    path('appointment/', views.appointment, name='appointment'),
    path('contact/', views.contact, name='contact'),
    path('facility/', views.facility, name='facility'),
    path('classes/', views.classes, name='classes'),
    path('team/', views.team, name='team'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('call_to_action/', views.call_to_action, name='call_to_action'),
    path('error/', views.error, name='404_error')

]
