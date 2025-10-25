from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})
    
    

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    review = models.CharField(max_length=200)

    def __str__(self):
        return self.review