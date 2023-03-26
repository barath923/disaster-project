from django.contrib import admin

# Register your models here.
from .models import*

admin.site.site_header="Admin site"

admin.site.register(MyUser)
admin.site.register(officer)