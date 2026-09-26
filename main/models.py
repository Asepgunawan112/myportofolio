# Create your models here.
import uuid
from django.db import models
from django.contrib.auth.models import User

class Experience(models.Model):
    EXPERIENCE_CHOICES = [
        ('internship', 'Internship'),
        ('research', 'Research'),
        ('volunteer', 'Volunteer'),
        ('part-time', 'Part-Time'),
        ('full-time', 'Full-Time'),
        ('freelance', 'Freelance'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=EXPERIENCE_CHOICES, default='full-time')
    thumbnail = models.URLField(blank=True, null=True)
    started_at = models.DateTimeField(null=True, blank=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    starred_by = models.ManyToManyField(User, related_name='starred_experiences', blank=True)

    def __str__(self):
        return self.title
    
    @property
    def is_ongoing(self):
        return self.ended_at is None

class Certificate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title= models.CharField(max_length=255)
    organization= models.CharField(max_length=255, blank=True)
    date= models.DateField(blank=True)
    thumbnail = models.URLField(blank=True, max_length=500, null=True)
    starred_by = models.ManyToManyField(User, related_name='starred_certificates', blank=True)


    def __str__(self):
        return self.title

class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title= models.CharField(max_length=255)
    author= models.CharField(max_length=255, blank=True)
    year= models.IntegerField(blank=True, null=True)
    sinopsis = models.TextField(blank=True)
    thumbnail = models.URLField(blank=True, max_length=500)
    status = models.CharField(max_length=20, choices=[('available', 'Available'), ('borrowed', 'Borrowed'), ('not allowed', 'Not Allowed')], default='to-read')
    starred_by = models.ManyToManyField(User, related_name='starred_books', blank=True)


    def __str__(self):
        return self.title