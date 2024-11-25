from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def Action(request):
    return HttpResponse('''<h1>Jailer</h1>
    <h1>Vikram</h1>
    <h1>Leo</h1>''')