from django.db import models


class User(models.Model):
    """Represents a person who uses the app."""
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password_hash = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User {self.username} '{self.full_name}'"

    @property
    def formatted_date(self):
        return self.created_at.strftime("%d/%m/%Y")

class Login(models.Model):
    """Represents the login history of an user."""
    user = models.ForeignKey(to=User,
                             on_delete=models.CASCADE,
                             related_name='logins')
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Login at {self.datetime} by user {self.user.username}"

    @property
    def formatted_datetime(self):
        return self.datetime.strftime("%d/%m/%Y a las %H:%M (%Z)")

class Tweet(models.Model):
    """A tweet from an user."""
    message = models.CharField(max_length=249)
    user = models.ForeignKey(to=User,
                             on_delete=models.CASCADE,
                             related_name='tweets')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Tweet by {self.user.username} at {self.created_at}.\n \
                 Message: `{self.message}`"

    @property
    def formatted_created_at(self):
        return self.created_at.strftime("%d/%m/%Y a las %H:%M (%Z)")
