from django.db import models


class TestSerializerModel(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title


class TestViewModel(models.Model):
    title1 = models.CharField(max_length=100)
    title2 = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title
