from django.contrib import admin
from .models import Film
# Register your models here.
#admin.site.register(Film)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    exclude = [""]
    search_fields = ['tytul', 'opis']
    list_filter = ['rok', 'imdb_rating']