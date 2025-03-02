from django.shortcuts import render

# Create your views here.

def index_pg(request):
    return render(request,'Pages/index.html')

def aboutus_pg(request):
    return render(request,'Pages/aboutus.html')

def contactus_pg(request):
    return render(request,'Pages/contactus.html')

def pricingplan_pg(request):
    return render(request,'Pages/pricingplan.html')

def servicedetails_pg(request):
    return render(request,'Pages/servicedetails.html')