from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('self-help/', views.self_help, name='self_help'),
    path('services/', views.services, name='services'),
    path('pricing/', views.pricing, name='pricing'),
    path('hours/', views.hours, name='hours'),
    path('book-service/', views.book_service, name='book_service'),
    path('contact/', views.contact, name='contact'),
    path('request-success/', views.request_success, name='request_success'),
    path('faq/', views.faq, name='faq'),
]