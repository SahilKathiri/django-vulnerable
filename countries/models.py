from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
	name = models.CharField(max_length=20)
	about = models.TextField()

class Comment(models.Model):
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.TextField()

class User(models.Model):
	user = models.OneToOneField(User)
	password = models.CharField(max_length=50)