from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from multiselectfield import MultiSelectField

class date(models.Model):
    month = models.IntegerField(validators=[MaxValueValidator(12)])
    day = models.IntegerField(validators=[MaxValueValidator(31)])
    year = models.IntegerField(validators=[MaxValueValidator(2018)])

    def __str__(self):
        return (str(self.month) + "/" + str(self.day) + "/" + str(self.year))

class category(models.Model):
    category_choices = (
        ('Personal', 'Personal'),
        ('Opinion', 'Opinion'),
        ('News', 'News')
    )
    category = models.CharField(
        max_length = 8,
        choices=category_choices
    )
    
    def __str__(self):
        return self.category

class user(models.Model):
    username = models.CharField(max_length = 30)

    def __str__(self):
        return self.username

class post(models.Model):
    category = models.ForeignKey('category', on_delete=models.DO_NOTHING)
    username = models.ForeignKey('username', on_delete=models.DO_NOTHING)
    date = models.ForeignKey('date', on_delete=models.DO_NOTHING)
    content = models.TextField()
    ID = models.IntegerField(validators=[MaxValueValidator(10)])

    def __str__(self):
        return str(self.category) + "/" + str(self.username) + "/" + str(self.date) + "/" + str(self.ID)