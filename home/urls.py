from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('property_list/', views.property_list, name="property_list"),
    path('property_type/', views.property_type, name="property_type"),
    path('property_agent/', views.agent, name='agent'),
    path('testimonial/', views.testimonial, name='testimonial'),
    path('error/', views.error, name='error'),
    path('contact/', views.contact, name='contact'),
    path('login_register_user/', views.auth_user, name='auth_user'),
    path('login_register_admin/', views.auth_admin, name='auth_admin'),
    path('logout/', views.logoutPage, name='logout'),
    path('add_tennis/', views.add_tennis, name='add_tennis'),
]
