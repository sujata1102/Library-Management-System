from django.contrib import admin
from libapp.models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):

    list_display=['bname','author','price','isbn','desc','is_deleted']
   
#Register model with ModelAdmin class

admin.site.register(Book,BookAdmin)