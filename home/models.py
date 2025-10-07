from django.db import models

# Create your models here.
class Message(models.Model):
    title = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField()
    
    def __str__(self):
        return self.title
    
