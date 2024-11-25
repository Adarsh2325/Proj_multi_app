from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Thrillers(request):
    return HttpResponse('''<h1>Kiskinda Kaandam</h1>
    <h1>SookshmaDharshini</h1>
    <h1>Drishyam</h1>''')
