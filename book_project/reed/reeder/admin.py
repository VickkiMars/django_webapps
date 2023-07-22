from django.contrib import admin
from .models import Book, Author, comment, Profile
# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(comment)
admin.site.register(Profile)