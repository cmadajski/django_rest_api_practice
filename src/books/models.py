from django.db import models
from uuid import uuid4
from datetime import date

LANGUAGE_CHOICES = [
    ('EN', 'English'),
    ('SP', 'Spanish'),
    ('FR', 'French'),
    ('JP', 'Japanese'),
    ('CH', 'Chinese'),
]

class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, null=False)
    name = models.CharField(max_length=50)
    age = models.IntegerField(default=0)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, null=False)
    name = models.CharField(max_length=50, blank=True, default='')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_published = models.DateField(default=date(2000, 1, 1))
    language = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default='English', )
    num_pages = models.IntegerField(default=0)
    checked_out = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Library(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, null=False)
    address = models.CharField(max_length=50, null=False, default='Not provided')
    city = models.CharField(max_length=30, null=False)
    state = models.CharField(max_length=2, null=False)
