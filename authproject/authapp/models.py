from django.db import models
from django.conf import settings
# Create your models here.
class Book(models.Model):
    book_name=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    published_date= models.DateField()
    book_count = models.IntegerField(default=0)

    def __str__(self):
        return self.book_name

class request_book(models.Model):
    student_name = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    book_name=models.ForeignKey(Book,on_delete=models.CASCADE)
    request_date=models.DateField()
    bookissue_status = [
    ('Pending', 'Pending'),
    ('Cancelled', "Cancelled"),
    ('Approved', 'Approved')]
    status = models.CharField(max_length=20,choices=bookissue_status,default='pending')

    
    def __str__(self):
        return str(self.book_name)

# class issue_book(models.Model):
#     book_name=models.ForeignKey(request_book,on_delete=models.CASCADE)
#     librarian_name=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
#     issue_date=models.DateField()
#     expiry_date=models.DateField()
    
#     def __str__(self):
#         return self.book_name

    
