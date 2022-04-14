# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    course = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.course

class Profile(models.Model):
    YEAR = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE) # Delete profile when user is deleted
    image = models.ImageField(default='chad.jpg', upload_to='profile_pics')
    course = models.ManyToManyField(Course)
    # rating = models.IntegerField
    year = models.CharField(max_length=1, choices=YEAR, blank=True)
    rate = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} Profile' #show how we want it to be displayed