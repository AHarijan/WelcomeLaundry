from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from App import views



urlpatterns = [
path('',views.index_pg,name='homepage'),
path('aboutUs',views.aboutus_pg,name='aboutus'),
path('contactUs',views.contactus_pg,name='contactus'),
path('pricingPlan',views.pricingplan_pg,name='pricingplan'),
path('serviceDetails',views.servicedetails_pg,name='servicedetails'),

]