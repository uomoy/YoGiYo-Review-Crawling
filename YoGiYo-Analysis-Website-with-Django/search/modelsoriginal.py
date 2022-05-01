from django.db import models

# Create your models here.

class MenuAnalysis(models.Model):
    restaurant = models.CharField(max_length=100)
    menu = models.CharField(max_length=200)
    order_times = models.IntegerField()
    average = models.FloatField()

    class Meta:
        managed = False
        db_table = 'menu_analysis'


class MenuImg(models.Model):
    restaurant = models.CharField(max_length=100)
    menu = models.CharField(max_length=200)
    img = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'menu_img'


class Wordclouds(models.Model):
    restaurant = models.CharField(max_length=100)
    pn = models.CharField(max_length=10)
    wordcloud = models.TextField()

    class Meta:
        managed = False
        db_table = 'wordclouds'