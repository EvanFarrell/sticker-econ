from django.shortcuts import render
from .models import *

def home(request):
    stickers = Sticker.objects.all()

    context = {
        "stickers": stickers,
    }

    return render(request, "index.html", context)

# Create your views here.
