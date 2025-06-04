from django.contrib import admin

# Register your models here.
admin.site.site_header = "GiftMate Admin"
admin.site.site_title = "GiftMate Admin Portal"
admin.site.index_title = "Welcome to GiftMate Admin Portal"
from .models import Recommendation
admin.site.register(Recommendation)