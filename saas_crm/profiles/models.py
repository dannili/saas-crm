from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE),
    bio = models.TextField(blank=True, null=True),
    phone_number = models.CharField(max_length=15, blank=True, null=True),

    class Meta:
        permissions = [('can_edit', 'Can edit item')]
