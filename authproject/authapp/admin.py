from django.contrib import admin
from requests import request
from .models import Book,request_book #,issue_book

# Register your models here.
class librarydmin(admin.ModelAdmin):
    list_display= ["book_name","author","published_date"]
    def __str__(self):
        return self.book_name

admin.site.register(Book,librarydmin)

class request_book_admin(admin.ModelAdmin):
    list_display=["student_name","book_name",'request_date','status']
 
admin.site.register(request_book,request_book_admin)

# class issue_book_admin(admin.ModelAdmin):
#     list_display=['book_name','librarian_name','issue_date','expiry_date']
# admin.site.register(issue_book)
