from django.shortcuts import render
# from django.http import HttpResponse
from .models import Brand, Dress

# Create your views here.
def main(request):
    brands = Brand.objects.all()
    dresses = Dress.objects.all()
    
    context = {'brands': brands, 'dresses': dresses}
    
    return render(request, "main.html", context)