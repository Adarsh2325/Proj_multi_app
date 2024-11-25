from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def FeelGood(request):
    return HttpResponse('''<h1>Zindagi Na Milegi Dobara</h1>
    <h1>Barfi</h1>
    <h1>3 idiots</h1>''')
