from django.contrib import admin
from .models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.core.exceptions import *

@admin.register(Sticker)
class StickerAdmin(admin.ModelAdmin):
    pass
