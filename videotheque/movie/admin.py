from django.contrib import admin

from movie.models import Director, Movie

# Register your models here.
admin.site.register(Director)
admin.site.register(Movie)