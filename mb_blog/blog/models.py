from django.db import models
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    body = models.TextField()
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
    
class contactform(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=1000)
    
    def get_absolute_url(self):
        return reverse("home")
    
    
    def __str__(self):
        return self.name
    

    
    
    

    
