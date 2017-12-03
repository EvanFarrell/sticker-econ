from django.shortcuts import render, redirect
from .models import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):
    stickers = Sticker.objects.all()
    sticker = stickers.first()

    context = {
        "stickers": stickers,
        "sticker": sticker,
    }

    return render(request, "index.html", context)

@csrf_exempt
def upvote(request, sticker_id):
    sticker = Sticker.objects.get(id=sticker_id)
    sticker.votes += 1
    sticker.save()
    print(sticker.votes)
    return redirect('/')

@csrf_exempt
def downvote(request, sticker_id):
    sticker = Sticker.objects.get(id=sticker_id)
    sticker.votes += 1
    sticker.save()
    return redirect('/')
