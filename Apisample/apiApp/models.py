from django.db import models


# Create your models here.
class Value(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text


class Principle(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text
