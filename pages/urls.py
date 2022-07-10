from django.urls import path, include

from pages import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('services', views.services, name='services'),
    path('contact', views.contact,name='contact'),
    path('portfolio_details', views.portfolio_details,name='portfolio_details'),
]