from django.contrib import admin
from .models import Chirp, Relationship, Like

# Register your models here.

admin.site.register(Chirp)
admin.site.register(Relationship)
admin.site.register(Like)
