from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('contact.html', views.contact, name='contact'),
    path('blog.html', views.blog, name='blog'),
    path('portfolio.html', views.portfolio, name='portfolio'),
    path('appointment.html', views.appointment, name='appointment'),
]