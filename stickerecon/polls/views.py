from django.shortcuts import render
from .models import *

def home(request):
    stickers = Sticker.objects.all()

    context = {
        "stickers": stickers,
    }

    return render(request, "index.html", context)

def upvote(request, sticker_id):
    sticker = Sticker.objects.get(id=sticker_ids)
    sticker.votes += 1
    sticker.save()

def upvote(request, sticker_id):
    sticker = Sticker.objects.get(id=sticker_id)
    sticker.votes += 1
    sticker.save()

def downvote(request, sticker_id):
    sticker = Sticker.objects.get(id=sticker_id)
    sticker.votes += 1
    sticker.save()
