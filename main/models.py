from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password_hash = models.CharField(max_length=255)

class Login(models.Model):
    user = models.ForeignKey(to=User,
                             on_delete=models.CASCADE,
                             related_name='logins')
    datetime = models.DateTimeField(auto_now_add=True)

