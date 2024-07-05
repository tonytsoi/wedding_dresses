from django.shortcuts import render
# from django.http import HttpResponse
from .models import Brand, Dress, Image, Booking

# Create your views here.
def main(request):
    brand = request.GET.get('brand')
    if brand == None:
        dresses = Dress.objects.all()
    else:
        dresses = Dress.objects.filter(brand__name=brand)
    
    brands = Brand.objects.all()
    images = Image.objects.all()
    
    context = {'brands': brands, 'dresses': dresses, 'images': images}
    
    return render(request, "main.html", context)

def viewDress(request, pk):
    dress = Dress.objects.get(id=pk)
    images = Image.objects.filter(dress=dress)
    bookings = Booking.objects.filter(dress=dress).order_by('start_date')
    
    context = {"dress": dress, "images": images, "bookings": bookings}
    return render(request, "dress.html", context)