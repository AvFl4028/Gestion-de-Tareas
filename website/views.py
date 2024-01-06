from django.shortcuts import render
from django.contrib import messages

from .models import TestDb


# Create your views here.
def home(request):
    db = TestDb.objects.all()
    return render(request, "home.html", {"data": db})
