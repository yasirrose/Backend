from django.contrib import admin
from .models import Movie, Brand, Tag

# Register your models here.

admin.site.register([Movie, Brand, Tag])
