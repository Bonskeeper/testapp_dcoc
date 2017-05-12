from django.db import models

# Model for project
class Data_piece(models.Model):
	region = models.CharField(max_length=255)
	country = models.CharField(max_length=255)
	number = models.SmallIntegerField()