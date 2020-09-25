from django.db import models

# Create your models here.
#This model is used for demo only
class Snippet(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self) :
        return self.title


#This is the main databse model which will be implemented in our webapp
class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    date = models.DateField()
    author = models.CharField(max_length=100)
    publication = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self) :
        return self.title