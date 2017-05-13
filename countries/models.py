from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
	name = models.CharField(max_length=20)
	about = models.TextField()

	def __str__(self):
		try:
			return "{0}".format(self.name)
		except ObjectDoesNotExist:
			return "[Del: Country instance]"

class WebUser(models.Model):
	user = models.OneToOneField(User)
	password = models.CharField(max_length=50)

	def __str__(self):
		try:
			return "{0}".format(self.user.username + ': ' + self.user.first_name + " " +  self.user.last_name)
		except ObjectDoesNotExist:
			return "[Del: User instance]"

class Comment(models.Model):
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	user = models.ForeignKey(WebUser, on_delete=models.CASCADE)
	body = models.TextField()