from django.shortcuts import render
# from django.http import HttpResponse
from .models import Brand, Dress

# Create your views here.
def main(request):
    brand = request.GET.get('brand')
    if brand == None:
        dresses = Dress.objects.all()
    else:
        dresses = Dress.objects.filter(brand__name=brand)
    
    brands = Brand.objects.all()
    
    
    context = {'brands': brands, 'dresses': dresses}
    
    return render(request, "main.html", context)