# -*- coding: utf-8 -*-
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    name = models.CharField(max_length=100, blank=True)
    age = models.IntegerField()
    occupation = models.CharField(max_length=100, blank=True)
        
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return super(User, self).__str__()


class Book(models.Model):
    title = models.CharField(max_length=100, blank=True)
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return super(Book, self).__str__()
