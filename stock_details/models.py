from django.db import models


class Stocks(models.Model):
    stock_name = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Stocks'

    def __str__(self):
        return self.stock_name


class StockUser(models.Model):
    user_name = models.CharField(max_length=200)
    age = models.IntegerField()
    salary = models.PositiveBigIntegerField()
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name

    # MANY 2 ONE RElationship  ====> Many songs in 1 Album

class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Song(models.Model):
    title = models.CharField(max_length=200)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Director(models.Model):  
    name = models.CharField(max_length=20)  
  
    def __str__(self):  
        return self.name  
      
class Movie(models.Model):  
    movie_title = models.CharField(max_length=150)  
    release_year = models.IntegerField()  
    director = models.ForeignKey(Director, on_delete = models.CASCADE, max_length=100)  
      
    def __str__(self):  
        return self.movie_title  
