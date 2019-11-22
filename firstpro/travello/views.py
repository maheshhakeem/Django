from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):
    
    dest1=Destination()
    dest1.name="Mumbai"
    dest1.img="destination_1.jpg"
    dest1.price=123
    dest1.desc="The City with More Population"
    dest1.specialoffer=False
    
    dest2=Destination()
    dest2.name="Hyderabad"
    dest2.img='destination_2.jpg'
    dest2.price=321
    dest2.desc="The City of Bangles"
    dest2.specialoffer=True
    
    dest3=Destination()
    dest3.name="Banglore"
    dest3.img='destination_3.jpg'
    dest3.price=456
    dest3.desc="The City of Plants"
    dest3.specialoffer=False
    
    Dests=[dest1,dest2,dest3]
    
    return render(request,'index.html', {'Destinations':Dests})
